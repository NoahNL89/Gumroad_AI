#!/usr/bin/env python3
"""
Build a Pinterest retail catalog CSV from the local Gumroad SQLite snapshot.

Usage:
    python3 scripts/build_pinterest_catalog.py --store-url https://store.schep.dev
    PINTEREST_CLAIMED_STORE_URL=https://store.schep.dev python3 scripts/build_pinterest_catalog.py
"""
import argparse
import csv
import os
import re
import sqlite3
import sys
from html import unescape
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "store.db"
OUT_PATH = ROOT / "output" / "pinterest_catalog.csv"

FIELDS = [
    "id",
    "title",
    "description",
    "link",
    "image_link",
    "price",
    "availability",
    "brand",
    "condition",
    "product_type",
    "google_product_category",
    "custom_label_0",
]

DEFAULT_DESCRIPTION = (
    "A digital product from Schep Digital for AI workflows, productivity, "
    "creator systems, and practical business automation."
)

# Numeric IDs are less error-prone than taxonomy paths when Pinterest imports
# Google categories. These IDs are leaf categories from Google's current
# English product taxonomy.
GPC_DOCUMENT_TEMPLATES = "8022"
GPC_EBOOKS = "543542"
GPC_DIGITAL_ARTWORK = "500046"
GPC_3D_MODELING_SOFTWARE = "6027"


def load_env():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def clean_text(value, fallback="", limit=None):
    text = unescape(str(value or fallback))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        text = text[: limit - 3].rstrip() + "..."
    return text


def money(price_cents, currency):
    return f"{(int(price_cents) / 100):.2f} {str(currency or 'EUR').upper()}"


def product_type(name):
    n = name.lower()
    if any(k in n for k in ("prompt", "gemini", "llm", "vault")):
        return "Digital Products > AI Tools > Prompt Packs"
    if any(k in n for k in ("instagram", "linkedin", "hook", "content", "email")):
        return "Digital Products > Marketing Templates"
    if any(k in n for k in ("resume", "cv", "proposal", "freelance")):
        return "Digital Products > Business Templates"
    if any(k in n for k in ("notion", "habit", "productivity")):
        return "Digital Products > Productivity Templates"
    if any(k in n for k in ("midjourney", "character", "blender", "ai art")):
        return "Digital Products > Creative Assets"
    return "Digital Products > Templates"


def google_product_category(name):
    n = name.lower()
    if "blender" in n or "3d" in n:
        return GPC_3D_MODELING_SOFTWARE
    if "digital artwork" in n or "ai art asset" in n:
        return GPC_DIGITAL_ARTWORK
    if any(k in n for k in ("guide", "mastery kit")):
        return GPC_EBOOKS
    return GPC_DOCUMENT_TEMPLATES


def custom_label(name):
    n = name.lower()
    if "bundle" in n or "toolkit" in n:
        return "bundle"
    if any(k in n for k in ("prompt", "gemini", "llm", "vault")):
        return "ai-prompts"
    if any(k in n for k in ("instagram", "linkedin", "hook", "content", "email")):
        return "marketing"
    if any(k in n for k in ("resume", "cv", "proposal")):
        return "career"
    return "digital-product"


def rewrite_link(short_url, store_url):
    if not short_url:
        return ""
    if not store_url:
        return short_url
    parsed = urlparse(short_url)
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query
    return urljoin(store_url.rstrip("/") + "/", path.lstrip("/"))


def rows_from_db(db_path, store_url):
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    rows = con.execute(
        """
        SELECT id, name, description, price_cents, currency, formatted_price,
               short_url, thumbnail_url, published
        FROM products
        WHERE published = 1
          AND price_cents > 0
          AND short_url IS NOT NULL
          AND thumbnail_url IS NOT NULL
        ORDER BY price_cents DESC, name ASC
        """
    ).fetchall()
    con.close()

    out = []
    skipped = []
    for row in rows:
        formatted = (row["formatted_price"] or "").lower()
        if "month" in formatted or "year" in formatted:
            skipped.append((row["name"], "subscription price"))
            continue
        if int(row["price_cents"] or 0) <= 0:
            skipped.append((row["name"], "zero price"))
            continue
        link = rewrite_link(row["short_url"], store_url)
        if not link or not row["thumbnail_url"]:
            skipped.append((row["name"], "missing link or image"))
            continue
        name = clean_text(row["name"], limit=500)
        desc = clean_text(row["description"], DEFAULT_DESCRIPTION, limit=10000)
        out.append({
            "id": clean_text(row["id"], limit=127),
            "title": name,
            "description": desc,
            "link": link,
            "image_link": row["thumbnail_url"],
            "price": money(row["price_cents"], row["currency"]),
            "availability": "in stock",
            "brand": "Schep Digital",
            "condition": "new",
            "product_type": product_type(name),
            "google_product_category": google_product_category(name),
            "custom_label_0": custom_label(name),
        })
    return out, skipped


def write_csv(rows, out_path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)


def main(argv=None):
    load_env()
    parser = argparse.ArgumentParser(description="Build Pinterest retail catalog CSV")
    parser.add_argument("--db", type=Path, default=DB_PATH)
    parser.add_argument("--out", type=Path, default=OUT_PATH)
    parser.add_argument(
        "--store-url",
        default=os.environ.get("PINTEREST_CLAIMED_STORE_URL") or os.environ.get("GUMROAD_CUSTOM_DOMAIN", ""),
        help="Claimed Gumroad custom domain, e.g. https://store.schep.dev",
    )
    args = parser.parse_args(argv)

    if not args.db.exists():
        sys.exit(f"DB not found: {args.db}. Run: python3 db/sync.py")
    if not args.store_url:
        print("Warning: no --store-url/PINTEREST_CLAIMED_STORE_URL set; using Gumroad short URLs.", file=sys.stderr)

    rows, skipped = rows_from_db(args.db, args.store_url)
    if not rows:
        sys.exit("No eligible catalog products found.")
    write_csv(rows, args.out)
    print(f"Wrote {len(rows)} Pinterest catalog rows to {args.out}")
    if skipped:
        print(f"Skipped {len(skipped)} products:")
        for name, reason in skipped:
            print(f"  - {name}: {reason}")


if __name__ == "__main__":
    main()
