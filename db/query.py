#!/usr/bin/env python3
"""
Gumroad Store — Interactive SQLite Query Tool
Quick queries for agents and humans.

Usage:
    python3 db/query.py                  # Show full snapshot
    python3 db/query.py products         # List all products
    python3 db/query.py underpriced      # Products still at ≤€0.99
    python3 db/query.py sales            # Recent sales
    python3 db/query.py revenue          # Revenue summary
    python3 db/query.py survival         # Survival dashboard
    python3 db/query.py funnel           # Catalog health + sales velocity + verdict
"""

import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), "store.db")

def get_db():
    if not os.path.exists(DB_PATH):
        print(f"❌  Database not found at {DB_PATH}")
        print("    Run: python3 db/sync.py")
        sys.exit(1)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def cmd_products(con):
    rows = con.execute("""
        SELECT name, formatted_price, published, sales_count, short_url
        FROM products ORDER BY price_cents DESC
    """).fetchall()
    print(f"\n{'NAME':<55} {'PRICE':>8}  {'LIVE':>5}  {'SALES':>5}")
    print("─"*80)
    for r in rows:
        live = "✅" if r["published"] else "❌"
        print(f"{r['name'][:54]:<55} {r['formatted_price']:>8}  {live:>5}  {r['sales_count']:>5}")
    print(f"\n{len(rows)} products total")

def cmd_underpriced(con):
    rows = con.execute("""
        SELECT id, name, formatted_price, published
        FROM products WHERE price_cents <= 99
        ORDER BY published DESC, name
    """).fetchall()
    if not rows:
        print("\n✅ No underpriced products (all >€0.99)")
        return
    print(f"\n⚠️  {len(rows)} products still at ≤€0.99:\n")
    for r in rows:
        live = "live" if r["published"] else "draft"
        print(f"  [{live}] {r['name'][:60]}  → {r['formatted_price']}")
        print(f"         ID: {r['id']}")
    print(f"\nFix with: python3 db/sync.py --reprice-zero 7.99   (matches GO.md ROUTINE 3; skip €0 subscriptions — they are exempt)")

def cmd_sales(con):
    rows = con.execute("""
        SELECT product_name, email, formatted_price, refunded, sale_timestamp
        FROM sales ORDER BY sale_timestamp DESC LIMIT 50
    """).fetchall()
    if not rows:
        print("\n  No sales recorded yet.")
        return
    print(f"\n{'PRODUCT':<40} {'EMAIL':<30} {'PRICE':>8}  STATUS")
    print("─"*90)
    for r in rows:
        status = "REFUNDED" if r["refunded"] else "✅"
        ts = (r["sale_timestamp"] or "")[:10]
        print(f"{(r['product_name'] or '')[:39]:<40} {(r['email'] or '')[:29]:<30} {(r['formatted_price'] or ''):>8}  {status}  {ts}")

def cmd_revenue(con):
    rows = con.execute("""
        SELECT
          strftime('%Y-%m', sale_timestamp) as month,
          COUNT(*) as sales,
          SUM(CASE WHEN refunded=0 THEN price_cents ELSE 0 END) as net_cents,
          SUM(price_cents) as gross_cents
        FROM sales
        GROUP BY month
        ORDER BY month DESC
        LIMIT 12
    """).fetchall()
    print(f"\n{'MONTH':<10}  {'SALES':>6}  {'GROSS':>10}  {'NET':>10}")
    print("─"*45)
    for r in rows:
        gross = (r["gross_cents"] or 0) / 100
        net = (r["net_cents"] or 0) / 100
        print(f"{r['month']:<10}  {r['sales']:>6}  €{gross:>8.2f}  €{net:>8.2f}")

def cmd_survival(con):
    from datetime import datetime
    month = datetime.now().strftime("%Y-%m")
    row = con.execute("""
        SELECT
          COUNT(*) as sales,
          SUM(CASE WHEN refunded=0 THEN price_cents ELSE 0 END) as net_cents
        FROM sales
        WHERE strftime('%Y-%m', sale_timestamp) = ?
    """, (month,)).fetchone()

    net_eur = (row["net_cents"] or 0) / 100
    target = float(os.environ.get('AGENT_MONTHLY_TARGET_EUR', '58'))
    growth = 150.0

    print(f"\n╔══════════════════════════════════════╗")
    print(f"║   🤖 Survival Dashboard — {month}  ║")
    print(f"╠══════════════════════════════════════╣")
    print(f"║  Sales this month:  {row['sales']:>4}              ║")
    print(f"║  Net revenue:       €{net_eur:>7.2f}           ║")
    print(f"║  Survival target:   €{target:>7.2f}           ║")
    print(f"║  Growth target:     €{growth:>7.2f}           ║")
    print(f"╠══════════════════════════════════════╣")

    if net_eur >= growth:
        print(f"║  🚀 THRIVING — machine upgrade due!  ║")
    elif net_eur >= target:
        print(f"║  ✅ SURVIVING — subscriptions safe   ║")
    else:
        needed = target - net_eur
        print(f"║  ⚠️  AT RISK — need €{needed:.2f} more      ║")
    print(f"╚══════════════════════════════════════╝")

    # Best sellers
    best = con.execute("""
        SELECT product_name, COUNT(*) as cnt,
               SUM(CASE WHEN refunded=0 THEN price_cents ELSE 0 END) as net_cents
        FROM sales WHERE strftime('%Y-%m', sale_timestamp) = ?
        GROUP BY product_name ORDER BY cnt DESC LIMIT 5
    """, (month,)).fetchall()
    if best:
        print("\n  Top products this month:")
        for b in best:
            eur = (b["net_cents"] or 0) / 100
            print(f"    {b['product_name'][:45]:<45}  ×{b['cnt']}  €{eur:.2f}")

def cmd_funnel(con):
    """Catalog health + sales velocity. The measurable half of the funnel
    (Gumroad's API gives sales_count but not page views)."""
    from datetime import datetime, timezone, timedelta

    cat = con.execute("""
        SELECT COUNT(*) AS n,
               SUM(CASE WHEN sales_count > 0 THEN 1 ELSE 0 END) AS with_sales,
               COALESCE(SUM(sales_count), 0) AS units,
               COALESCE(SUM(sales_usd_cents), 0) / 100.0 AS revenue
        FROM products
    """).fetchone()
    n = cat["n"] or 0
    with_sales = cat["with_sales"] or 0
    pct = (with_sales / n * 100) if n else 0

    print("\n📊 Funnel & Catalog Health")
    print("─" * 52)
    print(f"  Products in catalog:   {n}")
    print(f"  Products with ≥1 sale: {with_sales}  ({pct:.0f}% of catalog)")
    print(f"  Lifetime units sold:   {cat['units']}")
    print(f"  Lifetime revenue:      €{cat['revenue']:.2f}")

    # Velocity: current sales_count vs the earliest snapshot in the last 7 days.
    # product_snapshots is created by db/sync.py — tolerate a DB synced before it existed.
    has_snapshots = con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='product_snapshots'"
    ).fetchone() is not None
    cutoff = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
    baseline, snap_days = {}, 0
    if has_snapshots:
        baseline = {
            r["product_id"]: r["sales_count"]
            for r in con.execute("""
                SELECT product_id, sales_count, MIN(snapshot_at)
                FROM product_snapshots WHERE snapshot_at >= ?
                GROUP BY product_id
            """, (cutoff,)).fetchall()
        }
        snap_days = con.execute(
            "SELECT COUNT(DISTINCT substr(snapshot_at,1,10)) FROM product_snapshots"
        ).fetchone()[0]

    movers = []
    for p in con.execute("SELECT id, name, sales_count FROM products").fetchall():
        delta = (p["sales_count"] or 0) - baseline.get(p["id"], p["sales_count"] or 0)
        if delta > 0:
            movers.append((p["name"], delta))

    print(f"\n  Sales velocity (last 7 days, across {snap_days} snapshot day(s)):")
    if not baseline or snap_days < 2:
        print("    ⏳ Baseline building — run `python3 db/sync.py` daily to populate velocity.")
    elif movers:
        for name, d in sorted(movers, key=lambda x: -x[1]):
            print(f"    ↑ +{d}  {name[:50]}")
    else:
        print("    ▏ 0 units moved across the entire catalog this week.")

    # Verdict — keep it growth-oriented (we earn our way up; we do not cut back).
    print("\n  Verdict:")
    if cat["units"] == 0:
        print("    Bottleneck = REACH. 0 sales across the catalog means buyers")
        print("    aren't arriving — the lever is DISTRIBUTION, not more products.")
        print("    → python3 scripts/launch_kit.py <product-id|name>  (multi-channel launch copy)")
    elif pct < 25:
        print(f"    Only {with_sales}/{n} products have ever sold. Concentrate promotion")
        print("    on proven sellers; pause net-new SKUs until traffic converts.")
    else:
        print("    Healthy spread. Push winners harder and test price/bundles.")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "snapshot"
    con = get_db()

    dispatch = {
        "products":   cmd_products,
        "underpriced": cmd_underpriced,
        "sales":      cmd_sales,
        "revenue":    cmd_revenue,
        "survival":   cmd_survival,
        "funnel":     cmd_funnel,
        "snapshot":   lambda c: (cmd_survival(c), cmd_products(c)),
    }

    fn = dispatch.get(cmd)
    if fn:
        fn(con)
    else:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(dispatch.keys())}")

    con.close()

if __name__ == "__main__":
    main()
