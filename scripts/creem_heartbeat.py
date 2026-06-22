#!/usr/bin/env python3
"""
creem_heartbeat.py
Polls Creem for new transactions, subscriptions, and customer activity.
Saves state to ~/.creem/heartbeat-state.json and alerts on changes.

Usage:
    python3 scripts/creem_heartbeat.py          # Single check
    python3 scripts/creem_heartbeat.py --watch  # Loop every 4 hours
    python3 scripts/creem_heartbeat.py --report # Print state summary
"""
import os, sys, json, time, argparse, sqlite3
from pathlib import Path
from datetime import datetime, timezone
import requests

# ── Config ────────────────────────────────────────────────────────────────────

ENV_PATH = Path(__file__).parent.parent / ".env"
STATE_FILE = Path.home() / ".creem" / "heartbeat-state.json"
DB_PATH = Path(__file__).parent.parent / "db" / "store.db"
CREEM_BASE = "https://test-api.creem.io/v1"
POLL_INTERVAL_SECONDS = 4 * 3600  # 4 hours per HEARTBEAT.md spec


def load_env():
    key = os.environ.get("CREEM_API_KEY", "")
    if not key and ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if line.startswith("CREEM_API_KEY=") and not line.startswith("#"):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        sys.exit("CREEM_API_KEY not set. Run: source .env")
    return key


API_KEY = load_env()
HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}


# ── API helpers ───────────────────────────────────────────────────────────────

def creem_get(path, params=None):
    try:
        r = requests.get(f"{CREEM_BASE}/{path}", headers=HEADERS, params=params or {}, timeout=15)
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def fetch_all_pages(path):
    """Paginate through all pages of a Creem list endpoint."""
    items = []
    page = 1
    while True:
        data = creem_get(path, {"page": page, "limit": 100})
        batch = data.get("items") or data.get("data") or []
        if not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return items


# ── State management ──────────────────────────────────────────────────────────

def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {"transactions": {}, "subscriptions": {}, "customers": {}, "last_run": None}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2))


# ── DB helpers ────────────────────────────────────────────────────────────────

def get_db():
    con = sqlite3.connect(str(DB_PATH))
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA journal_mode=WAL")
    return con


def ensure_creem_tables(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS creem_transactions (
        id              TEXT PRIMARY KEY,
        product_id      TEXT,
        product_name    TEXT,
        amount_eur      REAL,
        currency        TEXT,
        status          TEXT,
        customer_email  TEXT,
        created_at      TEXT,
        synced_at       TEXT
    );

    CREATE TABLE IF NOT EXISTS creem_customers (
        id              TEXT PRIMARY KEY,
        email           TEXT,
        name            TEXT,
        country         TEXT,
        created_at      TEXT,
        synced_at       TEXT
    );
    """)
    con.commit()


def upsert_transaction(con, tx):
    con.execute("""
        INSERT OR REPLACE INTO creem_transactions
            (id, product_id, product_name, amount_eur, currency, status, customer_email, created_at, synced_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        tx.get("id"),
        tx.get("product_id"),
        tx.get("product_name", ""),
        (tx.get("amount") or 0) / 100,
        tx.get("currency", "EUR"),
        tx.get("status"),
        tx.get("customer", {}).get("email", "") if isinstance(tx.get("customer"), dict) else "",
        tx.get("created_at"),
        datetime.now(timezone.utc).isoformat(),
    ))


def upsert_customer(con, c):
    con.execute("""
        INSERT OR REPLACE INTO creem_customers
            (id, email, name, country, created_at, synced_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        c.get("id"),
        c.get("email"),
        c.get("name", ""),
        c.get("country", ""),
        c.get("created_at"),
        datetime.now(timezone.utc).isoformat(),
    ))


# ── Alert logic ───────────────────────────────────────────────────────────────

def alert(message):
    """Print a timestamped alert."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"\n🔔  [{ts}] ALERT: {message}")


def diff_state(old_ids, new_items, id_key="id"):
    new_ids = {item[id_key]: item for item in new_items}
    added = {k: v for k, v in new_ids.items() if k not in old_ids}
    return new_ids, added


# ── Main heartbeat ────────────────────────────────────────────────────────────

def run_heartbeat(verbose=False):
    state = load_state()
    con = get_db()
    ensure_creem_tables(con)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"[{now}] Creem Heartbeat — polling transactions, subscriptions, customers...")

    alerts = []

    # 1. Transactions
    if verbose:
        print("  Fetching transactions...")
    transactions = fetch_all_pages("transactions")
    tx_ids, new_txs = diff_state(state.get("transactions", {}), transactions)

    for tx_id, tx in new_txs.items():
        amount = (tx.get("amount") or 0) / 100
        currency = tx.get("currency", "EUR")
        product_name = tx.get("product_name") or tx.get("product_id", "unknown")
        status = tx.get("status", "unknown")
        email = ""
        if isinstance(tx.get("customer"), dict):
            email = tx["customer"].get("email", "")
        msg = f"NEW SALE: {product_name} — {amount:.2f} {currency} ({status}) from {email or 'anon'}"
        alerts.append(msg)
        alert(msg)

    for tx in transactions:
        upsert_transaction(con, tx)
    con.commit()
    state["transactions"] = {item["id"]: True for item in transactions}

    # 2. Subscriptions
    if verbose:
        print("  Fetching subscriptions...")
    subscriptions = fetch_all_pages("subscriptions")
    sub_ids, new_subs = diff_state(state.get("subscriptions", {}), subscriptions)

    for sub_id, sub in new_subs.items():
        status = sub.get("status", "unknown")
        product_name = sub.get("product_name") or sub.get("product_id", "unknown")
        email = ""
        if isinstance(sub.get("customer"), dict):
            email = sub["customer"].get("email", "")
        if status == "active":
            msg = f"NEW SUBSCRIPTION: {product_name} — {email or 'anon'}"
            alerts.append(msg)
            alert(msg)
        elif status in ("canceled", "cancelled"):
            msg = f"CANCELLED: {product_name} — {email or 'anon'}"
            alerts.append(msg)
            alert(msg)
        elif status == "past_due":
            msg = f"PAYMENT FAILURE: {product_name} — {email or 'anon'}"
            alerts.append(msg)
            alert(msg)

    state["subscriptions"] = {item["id"]: item.get("status") for item in subscriptions}

    # 3. Customers
    if verbose:
        print("  Fetching customers...")
    customers = fetch_all_pages("customers")
    cust_ids, new_custs = diff_state(state.get("customers", {}), customers)

    for cust_id, c in new_custs.items():
        email = c.get("email", "anon")
        country = c.get("country", "?")
        if verbose:
            msg = f"NEW CUSTOMER: {email} from {country}"
            print(f"    {msg}")

    for c in customers:
        upsert_customer(con, c)
    con.commit()
    state["customers"] = {item["id"]: True for item in customers}

    con.close()
    save_state(state)

    # Summary
    print(f"\n  Transactions: {len(transactions)}  (+{len(new_txs)} new)")
    print(f"  Subscriptions: {len(subscriptions)}  (+{len(new_subs)} new)")
    print(f"  Customers: {len(customers)}  (+{len(new_custs)} new)")
    print(f"  Alerts fired: {len(alerts)}")

    return alerts


def print_report():
    state = load_state()
    last_run = state.get("last_run", "never")
    tx_count = len(state.get("transactions", {}))
    sub_count = len(state.get("subscriptions", {}))
    cust_count = len(state.get("customers", {}))

    print(f"=== Creem Heartbeat State ===")
    print(f"  Last run:      {last_run}")
    print(f"  Transactions:  {tx_count}")
    print(f"  Subscriptions: {sub_count}")
    print(f"  Customers:     {cust_count}")
    print(f"  State file:    {STATE_FILE}")

    if DB_PATH.exists():
        con = sqlite3.connect(str(DB_PATH))
        try:
            row = con.execute("SELECT COUNT(*), SUM(amount_eur) FROM creem_transactions").fetchone()
            print(f"\n  DB transactions: {row[0]}  |  Total revenue: €{(row[1] or 0):.2f}")
        finally:
            con.close()


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creem store heartbeat monitor")
    parser.add_argument("--watch", action="store_true", help=f"Loop every {POLL_INTERVAL_SECONDS//3600}h")
    parser.add_argument("--report", action="store_true", help="Print current state and exit")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    if args.report:
        print_report()
        sys.exit(0)

    if args.watch:
        print(f"Starting watch mode (polling every {POLL_INTERVAL_SECONDS//3600}h)...")
        while True:
            try:
                run_heartbeat(verbose=args.verbose)
            except KeyboardInterrupt:
                print("\nStopped.")
                break
            except Exception as e:
                print(f"  ERROR: {e}")
            print(f"\n  Next check in {POLL_INTERVAL_SECONDS//3600}h. Sleeping...")
            time.sleep(POLL_INTERVAL_SECONDS)
    else:
        run_heartbeat(verbose=args.verbose)
