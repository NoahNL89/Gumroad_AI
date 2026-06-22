#!/usr/bin/env python3
"""
creem_discount.py
Create and manage discount codes on Creem programmatically.

Usage:
    python3 scripts/creem_discount.py create --percent 30 --name "LAUNCH30" --products all
    python3 scripts/creem_discount.py create --percent 50 --name "FLASH50" --products 01,03,05
    python3 scripts/creem_discount.py list
    python3 scripts/creem_discount.py delete <discount-id>
"""
import os, sys, json, argparse
from pathlib import Path
import requests

ENV_PATH = Path(__file__).parent.parent / ".env"
PRODUCTS_FILE = Path(__file__).parent.parent / "creem" / "products.json"
CREEM_BASE = "https://test-api.creem.io/v1"


def load_env():
    key = os.environ.get("CREEM_API_KEY", "")
    if not key and ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if line.startswith("CREEM_API_KEY=") and not line.startswith("#"):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        sys.exit("CREEM_API_KEY not set.")
    return key


API_KEY = load_env()
HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}


def load_products():
    if not PRODUCTS_FILE.exists():
        sys.exit(f"creem/products.json not found. Run creem_create_products.py first.")
    return json.loads(PRODUCTS_FILE.read_text())


def resolve_product_ids(spec: str) -> list[str]:
    """
    spec: "all" | "01,03,05" (comma-separated slug prefixes)
    Returns list of Creem product IDs.
    """
    products = load_products()
    if spec == "all":
        return [v["creem_id"] for v in products.values()]

    ids = []
    prefixes = [p.strip() for p in spec.split(",")]
    for prefix in prefixes:
        matched = [v["creem_id"] for k, v in products.items() if k.startswith(prefix)]
        if not matched:
            print(f"  WARNING: no product matched prefix '{prefix}'")
        ids.extend(matched)
    return ids


def cmd_create(args):
    product_ids = resolve_product_ids(args.products)
    if not product_ids:
        sys.exit("No products resolved. Check --products argument.")

    payload = {
        "name": args.name,
        "type": "percentage",
        "percentage": args.percent,
        "duration": args.duration,
        "products": product_ids,
    }
    if args.code:
        payload["code"] = args.code
    if args.expires:
        payload["expires"] = args.expires
    if args.max_uses:
        payload["max_redemptions"] = args.max_uses

    r = requests.post(f"{CREEM_BASE}/discounts", headers=HEADERS, json=payload)
    result = r.json()

    if args.json_out:
        print(json.dumps(result, indent=2))
        return

    if result.get("object") == "discount" or result.get("id"):
        print(f"  Created: {result.get('id')}")
        print(f"  Code:    {result.get('code', '(auto)')}")
        print(f"  Percent: {args.percent}%")
        print(f"  Products: {len(product_ids)}")
        if result.get("expires"):
            print(f"  Expires: {result['expires']}")
    else:
        print(f"  ERROR: {result.get('message', result)}")


def cmd_list(args):
    r = requests.get(f"{CREEM_BASE}/discounts", headers=HEADERS)
    result = r.json()
    items = result.get("items") or result.get("data") or []

    if args.json_out:
        print(json.dumps(result, indent=2))
        return

    if not items:
        print("No discounts found.")
        return

    print(f"{'ID':<35} {'CODE':<20} {'TYPE':<12} {'AMOUNT':<10} {'DURATION'}")
    print("-" * 90)
    for d in items:
        amount = f"{d.get('percentage', 0)}%" if d.get("type") == "percentage" else f"€{(d.get('amount',0)/100):.2f}"
        print(f"  {d.get('id',''):<33} {d.get('code',''):<20} {d.get('type',''):<12} {amount:<10} {d.get('duration','')}")


def cmd_delete(args):
    r = requests.delete(f"{CREEM_BASE}/discounts/{args.discount_id}", headers=HEADERS)
    result = r.json()
    if args.json_out:
        print(json.dumps(result, indent=2))
    elif result.get("deleted") or r.status_code == 200:
        print(f"  Deleted: {args.discount_id}")
    else:
        print(f"  ERROR: {result.get('message', result)}")


# ── Convenience shortcuts ─────────────────────────────────────────────────────

def launch_discount(percent=30, products="all", expires=None):
    """Create a named launch discount for all or specific products. Returns result dict."""
    product_ids = resolve_product_ids(products)
    payload = {
        "name": f"LAUNCH{percent}",
        "code": f"LAUNCH{percent}",
        "type": "percentage",
        "percentage": percent,
        "duration": "once",
        "products": product_ids,
    }
    if expires:
        payload["expires"] = expires
    r = requests.post(f"{CREEM_BASE}/discounts", headers=HEADERS, json=payload)
    return r.json()


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creem discount manager")
    parser.add_argument("--json", dest="json_out", action="store_true", help="Output as JSON")
    sub = parser.add_subparsers(dest="cmd")

    # create
    p_create = sub.add_parser("create", help="Create a discount")
    p_create.add_argument("--percent", type=int, required=True, help="Discount percentage 1–100")
    p_create.add_argument("--name", required=True, help="Internal discount name")
    p_create.add_argument("--code", help="Promo code (auto-generated if omitted)")
    p_create.add_argument("--products", default="all", help="'all' or comma-separated slug prefixes e.g. '01,03'")
    p_create.add_argument("--duration", default="once", choices=["once", "forever", "repeating"], help="Duration type")
    p_create.add_argument("--expires", help="Expiry date ISO e.g. 2026-12-31")
    p_create.add_argument("--max-uses", type=int, dest="max_uses", help="Max redemptions")

    # list
    p_list = sub.add_parser("list", help="List all discounts")

    # delete
    p_del = sub.add_parser("delete", help="Delete a discount")
    p_del.add_argument("discount_id", help="Discount ID")

    args = parser.parse_args()
    if args.cmd == "create":
        cmd_create(args)
    elif args.cmd == "list":
        cmd_list(args)
    elif args.cmd == "delete":
        cmd_delete(args)
    else:
        parser.print_help()
