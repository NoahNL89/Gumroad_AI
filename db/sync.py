#!/usr/bin/env python3
"""
Gumroad SQLite Sync
Fetches ALL products (via permalink discovery), sales, and subscribers
and stores them in store.db for easy local access and agent tracking.

Usage:
    python3 db/sync.py                  # Sync everything
    python3 db/sync.py --products-only  # Only sync products
    python3 db/sync.py --reprice-all 9.99  # Reprice all €0.99 products
"""

import sqlite3
import urllib.request
import urllib.parse
import json
import os
import sys
import time
import argparse
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────

DB_PATH = os.path.join(os.path.dirname(__file__), "store.db")
ENV_PATH = os.path.join(os.path.dirname(__file__), "../.env")
API_BASE = "https://api.gumroad.com/v2"

def load_token():
    token = os.environ.get("GUMROAD_ACCESS_TOKEN", "")
    if not token and os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GUMROAD_ACCESS_TOKEN=") and not line.startswith("#"):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not token:
        print("❌  GUMROAD_ACCESS_TOKEN not set. Run: source .env")
        sys.exit(1)
    return token

TOKEN = load_token()

# ── HTTP helpers ──────────────────────────────────────────────────────────────

def api_get(path, params=None):
    p = {"access_token": TOKEN}
    if params:
        p.update(params)
    url = f"{API_BASE}/{path}?{urllib.parse.urlencode(p)}"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return json.loads(r.read())
    except Exception as e:
        return {"success": False, "error": str(e)}

def api_put(path, data):
    data["access_token"] = TOKEN
    encoded = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(f"{API_BASE}/{path}", data=encoded, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except Exception as e:
        return {"success": False, "error": str(e)}

# ── DB setup ──────────────────────────────────────────────────────────────────

def get_db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA foreign_keys=ON")
    return con

def init_db(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS products (
        id              TEXT PRIMARY KEY,
        permalink       TEXT,
        name            TEXT NOT NULL,
        price_cents     INTEGER,
        currency        TEXT DEFAULT 'eur',
        formatted_price TEXT,
        published       INTEGER DEFAULT 0,
        description     TEXT,
        tags            TEXT,
        sales_count     INTEGER DEFAULT 0,
        sales_usd_cents REAL DEFAULT 0,
        short_url       TEXT,
        thumbnail_url   TEXT,
        created_at      TEXT,
        synced_at       TEXT
    );

    CREATE TABLE IF NOT EXISTS sales (
        id              TEXT PRIMARY KEY,
        product_id      TEXT,
        product_name    TEXT,
        email           TEXT,
        full_name       TEXT,
        price_cents     INTEGER,
        currency        TEXT,
        formatted_price TEXT,
        refunded        INTEGER DEFAULT 0,
        disputed        INTEGER DEFAULT 0,
        sale_timestamp  TEXT,
        synced_at       TEXT
    );

    CREATE TABLE IF NOT EXISTS subscribers (
        id              TEXT PRIMARY KEY,
        product_id      TEXT,
        product_name    TEXT,
        email           TEXT,
        status          TEXT,
        created_at      TEXT,
        cancelled_at    TEXT,
        synced_at       TEXT
    );

    CREATE TABLE IF NOT EXISTS payouts (
        id              TEXT PRIMARY KEY,
        amount_cents    INTEGER,
        currency        TEXT,
        formatted_amount TEXT,
        date            TEXT,
        state           TEXT,
        synced_at       TEXT
    );

    CREATE TABLE IF NOT EXISTS offer_codes (
        id              TEXT PRIMARY KEY,
        product_id      TEXT,
        name            TEXT,
        offer_type      TEXT,
        amount_off      INTEGER,
        universal       INTEGER DEFAULT 0,
        times_used      INTEGER DEFAULT 0,
        max_purchase_count INTEGER,
        synced_at       TEXT
    );

    CREATE TABLE IF NOT EXISTS promotions (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        platform        TEXT,
        product_id      TEXT,
        url             TEXT,
        content         TEXT,
        posted_at       TEXT
    );

    CREATE TABLE IF NOT EXISTS sync_log (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        synced_at       TEXT,
        entity          TEXT,
        count           INTEGER,
        notes           TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_sales_product ON sales(product_id);
    CREATE INDEX IF NOT EXISTS idx_sales_email   ON sales(email);
    CREATE INDEX IF NOT EXISTS idx_subs_product  ON subscribers(product_id);
    CREATE INDEX IF NOT EXISTS idx_sales_timestamp ON sales(sale_timestamp);
    CREATE INDEX IF NOT EXISTS idx_products_published ON products(published);
    CREATE INDEX IF NOT EXISTS idx_promotions_platform ON promotions(platform, posted_at);
    """)
    con.commit()

# ── Sync: Products (all, via permalink discovery) ─────────────────────────────

def sync_products(con):
    now = datetime.now(timezone.utc).isoformat()
    print("\n📦 Syncing products...")

    # Step 1: Get known products from /products endpoint
    data = api_get("products")
    if data.get("success") is False:
        print(f"   ⚠️  API error fetching products: {data.get('error', 'unknown')}")
        return []
    products = data.get("products", [])

    # Step 2: Get all product permalinks from user.links
    user_data = api_get("user")
    if user_data.get("success") is False:
        print(f"   ⚠️  API error fetching user links: {user_data.get('error', 'unknown')}")
        print(f"   Continuing with {len(products)} products from /products endpoint only.")
        permalinks = []
    else:
        permalinks = user_data.get("user", {}).get("links", [])
    print(f"   /products API returned: {len(products)}")
    print(f"   User links (all permalinks): {len(permalinks)}")

    # Step 3: For each permalink not already in product list, fetch individually
    known_ids = {p["id"] for p in products}
    extra_fetched = 0

    for permalink in permalinks:
        # Try to find in known products by permalink
        already_known = any(
            p.get("custom_permalink") == permalink or
            (p.get("short_url") or "").endswith(f"/{permalink}")
            for p in products
        )
        if already_known:
            continue

        # Fetch product by permalink
        r = api_get(f"products/{permalink}")
        if r.get("success") and r.get("product"):
            prod = r["product"]
            if prod["id"] not in known_ids:
                products.append(prod)
                known_ids.add(prod["id"])
                extra_fetched += 1
        time.sleep(0.15)

    print(f"   Extra products fetched by permalink: {extra_fetched}")
    print(f"   Total products discovered: {len(products)}")

    # Step 4: Upsert all into DB
    for p in products:
        tags = json.dumps(p.get("tags", []))
        con.execute("""
            INSERT INTO products
              (id, permalink, name, price_cents, currency, formatted_price,
               published, description, tags, sales_count, sales_usd_cents,
               short_url, thumbnail_url, synced_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
              permalink=excluded.permalink,
              name=excluded.name,
              price_cents=excluded.price_cents,
              currency=excluded.currency,
              formatted_price=excluded.formatted_price,
              published=excluded.published,
              description=excluded.description,
              tags=excluded.tags,
              sales_count=excluded.sales_count,
              sales_usd_cents=excluded.sales_usd_cents,
              short_url=excluded.short_url,
              thumbnail_url=excluded.thumbnail_url,
              synced_at=excluded.synced_at
        """, (
            p["id"],
            p.get("custom_permalink"),
            p.get("name", ""),
            p.get("price"),
            p.get("currency", "eur"),
            p.get("formatted_price"),
            1 if p.get("published") else 0,
            p.get("description", ""),
            tags,
            p.get("sales_count", 0),
            p.get("sales_usd_cents", 0),
            p.get("short_url"),
            p.get("thumbnail_url"),
            now,
        ))

    con.execute("INSERT INTO sync_log (synced_at,entity,count) VALUES (?,?,?)",
                (now, "products", len(products)))
    con.commit()
    print(f"   ✅ {len(products)} products saved to DB")
    return products

# ── Sync: Sales ───────────────────────────────────────────────────────────────

def sync_sales(con):
    now = datetime.now(timezone.utc).isoformat()
    print("\n💰 Syncing sales...")

    all_sales = []
    page_key = None
    page = 1

    while True:
        params = {}
        if page_key:
            params["page_key"] = page_key

        data = api_get("sales", params)
        if data.get("success") is False:
            print(f"   ⚠️  API error fetching sales page {page}: {data.get('error', 'unknown')}")
            break
        sales = data.get("sales", [])
        if not sales:
            break

        all_sales.extend(sales)
        print(f"   Page {page}: {len(sales)} sales (total so far: {len(all_sales)})")

        page_key = data.get("next_page_key") or data.get("next_page_url")
        if not page_key or len(sales) == 0:
            break
        page += 1
        time.sleep(0.2)

    for s in all_sales:
        con.execute("""
            INSERT INTO sales
              (id, product_id, product_name, email, full_name,
               price_cents, currency, formatted_price,
               refunded, disputed, sale_timestamp, synced_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
              refunded=excluded.refunded,
              disputed=excluded.disputed,
              synced_at=excluded.synced_at
        """, (
            s.get("id"),
            s.get("product_id"),
            s.get("product_name"),
            s.get("email"),
            s.get("full_name"),
            s.get("price_cents"),
            s.get("currency"),
            s.get("formatted_display_price"),
            1 if s.get("refunded") else 0,
            1 if s.get("disputed") else 0,
            s.get("created_at"),
            now,
        ))

    con.execute("INSERT INTO sync_log (synced_at,entity,count) VALUES (?,?,?)",
                (now, "sales", len(all_sales)))
    con.commit()
    print(f"   ✅ {len(all_sales)} sales saved to DB")
    return all_sales

# ── Sync: Subscribers ─────────────────────────────────────────────────────────

def sync_subscribers(con):
    now = datetime.now(timezone.utc).isoformat()
    print("\n👥 Syncing subscribers...")

    # Get all membership products
    products = con.execute(
        "SELECT id, name FROM products WHERE published=1"
    ).fetchall()

    total = 0
    for prod in products:
        prod_id = prod["id"]
        page_key = None

        while True:
            params = {}
            if page_key:
                params["page_key"] = page_key

            data = api_get(f"products/{prod_id}/subscribers", params)
            if data.get("success") is False:
                print(f"   ⚠️  API error fetching subscribers for {prod_id}: {data.get('error', 'unknown')}")
                break
            subs = data.get("subscribers", [])
            if not subs:
                break

            for s in subs:
                con.execute("""
                    INSERT INTO subscribers
                      (id, product_id, product_name, email, status,
                       created_at, cancelled_at, synced_at)
                    VALUES (?,?,?,?,?,?,?,?)
                    ON CONFLICT(id) DO UPDATE SET
                      status=excluded.status,
                      cancelled_at=excluded.cancelled_at,
                      synced_at=excluded.synced_at
                """, (
                    s.get("id"),
                    prod_id,
                    prod["name"],
                    s.get("email"),
                    s.get("status"),
                    s.get("created_at"),
                    s.get("cancelled_at"),
                    now,
                ))
            total += len(subs)

            page_key = data.get("next_page_key")
            if not page_key:
                break
            time.sleep(0.2)

    con.execute("INSERT INTO sync_log (synced_at,entity,count) VALUES (?,?,?)",
                (now, "subscribers", total))
    con.commit()
    print(f"   ✅ {total} subscribers saved to DB")

# ── Sync: Payouts ─────────────────────────────────────────────────────────────

def sync_payouts(con):
    now = datetime.now(timezone.utc).isoformat()
    print("\n💳 Syncing payouts...")

    data = api_get("payouts")
    if data.get("success") is False:
        print(f"   ⚠️  API error fetching payouts: {data.get('error', 'unknown')}")
        return
    payouts = data.get("payouts", [])

    for p in payouts:
        con.execute("""
            INSERT INTO payouts (id, amount_cents, currency, formatted_amount, date, state, synced_at)
            VALUES (?,?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET state=excluded.state, synced_at=excluded.synced_at
        """, (
            p.get("id"),
            p.get("amount_cents"),
            p.get("currency"),
            p.get("amount_formatted"),
            p.get("date"),
            p.get("state"),
            now,
        ))

    con.execute("INSERT INTO sync_log (synced_at,entity,count) VALUES (?,?,?)",
                (now, "payouts", len(payouts)))
    con.commit()
    print(f"   ✅ {len(payouts)} payouts saved to DB")

# ── Sync: Offer Codes ─────────────────────────────────────────────────────────

def sync_offer_codes(con):
    now = datetime.now(timezone.utc).isoformat()
    print("\n🏷️  Syncing offer codes...")

    products = con.execute("SELECT id FROM products WHERE published=1").fetchall()
    total = 0

    for prod in products:
        prod_id = prod["id"]
        data = api_get(f"products/{prod_id}/offer_codes")
        if data.get("success") is False:
            print(f"   ⚠️  API error fetching offer codes for {prod_id}: {data.get('error', 'unknown')}")
            continue
        codes = data.get("offer_codes", [])

        for c in codes:
            con.execute("""
                INSERT INTO offer_codes
                  (id, product_id, name, offer_type, amount_off,
                   universal, times_used, max_purchase_count, synced_at)
                VALUES (?,?,?,?,?,?,?,?,?)
                ON CONFLICT(id) DO UPDATE SET
                  times_used=excluded.times_used,
                  synced_at=excluded.synced_at
            """, (
                c.get("id"),
                prod_id,
                c.get("name"),
                c.get("offer_type"),
                c.get("amount_off"),
                1 if c.get("universal") else 0,
                c.get("times_used", 0),
                c.get("max_purchase_count"),
                now,
            ))
        total += len(codes)
        time.sleep(0.1)

    con.execute("INSERT INTO sync_log (synced_at,entity,count) VALUES (?,?,?)",
                (now, "offer_codes", total))
    con.commit()
    print(f"   ✅ {total} offer codes saved to DB")

# ── Report ────────────────────────────────────────────────────────────────────

def print_report(con):
    print("\n" + "═"*55)
    print("  📊 STORE SNAPSHOT")
    print("═"*55)

    # Products summary
    rows = con.execute("""
        SELECT
          COUNT(*) as total,
          SUM(published) as live,
          COUNT(*) - SUM(published) as draft,
          COUNT(CASE WHEN price_cents <= 99 THEN 1 END) as underpriced,
          COUNT(CASE WHEN price_cents > 99 THEN 1 END) as properly_priced
        FROM products
    """).fetchone()
    print(f"\n  📦 Products:  {rows['total']} total  |  {rows['live']} live  |  {rows['draft']} draft")
    if rows['underpriced'] > 0:
        print(f"  ⚠️  Still at ≤€0.99: {rows['underpriced']} products — NEEDS REPRICING")
    print(f"  ✅ Properly priced (>€0.99): {rows['properly_priced']} products")

    # List underpriced
    under = con.execute(
        "SELECT name, formatted_price FROM products WHERE price_cents <= 99 ORDER BY name"
    ).fetchall()
    for u in under:
        print(f"     • {u['name'][:50]}  → {u['formatted_price']}")

    # Price breakdown
    print("\n  💶 Price breakdown:")
    tiers = con.execute("""
        SELECT formatted_price, COUNT(*) as cnt, SUM(published) as live
        FROM products
        GROUP BY formatted_price
        ORDER BY price_cents DESC
    """).fetchall()
    for t in tiers:
        print(f"     {t['formatted_price']:>8}  ×{t['cnt']}  ({t['live']} live)")

    # Sales
    sales_rows = con.execute("""
        SELECT
          COUNT(*) as total,
          SUM(CASE WHEN refunded=0 THEN 1 ELSE 0 END) as valid,
          SUM(CASE WHEN refunded=1 THEN 1 ELSE 0 END) as refunded,
          SUM(CASE WHEN refunded=0 THEN price_cents ELSE 0 END) as net_cents
        FROM sales
    """).fetchone()
    net_eur = (sales_rows['net_cents'] or 0) / 100
    print(f"\n  💰 Sales:     {sales_rows['total']} total  |  {sales_rows['valid']} valid  |  €{net_eur:.2f} net revenue")

    # Subscribers
    sub_count = con.execute("SELECT COUNT(*) FROM subscribers WHERE status='active'").fetchone()[0]
    print(f"  👥 Subscribers: {sub_count} active")

    # Survival status
    target = float(os.environ.get('AGENT_MONTHLY_TARGET_EUR', '58'))
    print(f"\n  🎯 Survival target:  €{target:.2f}/month")
    print(f"  💵 Net revenue:      €{net_eur:.2f}")
    if net_eur >= target:
        print("  ✅ STATUS: SURVIVING")
    else:
        needed = target - net_eur
        print(f"  ⚠️  STATUS: NEED €{needed:.2f} MORE THIS MONTH")

    print("\n" + "═"*55)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Gumroad SQLite Sync")
    parser.add_argument("--products-only", action="store_true")
    parser.add_argument("--report-only",   action="store_true")
    parser.add_argument("--reprice-zero",  type=float, metavar="PRICE",
                        help="Reprice all ≤€0.99 products to PRICE via API")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    con = get_db()
    init_db(con)

    if args.report_only:
        print_report(con)
        con.close()
        return

    products = sync_products(con)

    if not args.products_only:
        sync_sales(con)
        sync_subscribers(con)
        sync_payouts(con)
        sync_offer_codes(con)

    # Reprice underpriced products via direct API
    if args.reprice_zero:
        target_price = args.reprice_zero
        under = con.execute(
            "SELECT id, name, formatted_price FROM products WHERE price_cents <= 99 AND published=1"
        ).fetchall()
        print(f"\n🔧 Repricing {len(under)} products to €{target_price}...")
        for p in under:
            print(f"   → {p['name'][:50]}  ({p['formatted_price']} → €{target_price})")
            cents = int(target_price * 100)
            result = api_put(f"products/{p['id']}", {"price": str(cents), "currency": "eur"})
            if result.get("success"):
                new_cents = int(target_price * 100)
                con.execute(
                    "UPDATE products SET price_cents=?, formatted_price=? WHERE id=?",
                    (new_cents, f"€{target_price:.2f}", p["id"])
                )
                print(f"     ✅ Done")
            else:
                print(f"     ❌ Failed: {result.get('message', result)}")
            time.sleep(0.3)
        con.commit()

    print_report(con)
    con.close()
    print(f"\n✅ Database: {DB_PATH}")
    print("   Query with: sqlite3 db/store.db")

if __name__ == "__main__":
    main()
