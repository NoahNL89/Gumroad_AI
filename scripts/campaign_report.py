#!/usr/bin/env python3
"""Report focused-campaign posts and resulting product sales from the local DB.

Gumroad's CLI does not expose product page-view counts. Source-specific UTM links
preserve that attribution in Gumroad analytics; this report covers the data we can
verify locally: posts, variants, sales, and net revenue since campaign launch.
"""
import argparse
import json
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "store.db"
sys.path.insert(0, str(ROOT / "bot"))
from campaign import CAMPAIGN, FOCUS_PRODUCT_ID, FOCUS_PRODUCT_NAME  # noqa: E402

DEFAULT_SINCE = "2026-07-16T00:00:00+00:00"


def collect(con, since: str):
    con.row_factory = sqlite3.Row
    posts = con.execute(
        "SELECT platform, url, posted_at FROM promotions "
        "WHERE product_id=? AND posted_at>=? ORDER BY posted_at",
        (FOCUS_PRODUCT_ID, since),
    ).fetchall()
    sales = con.execute(
        "SELECT price_cents, refunded, disputed, sale_timestamp FROM sales "
        "WHERE product_id=? AND sale_timestamp>=? ORDER BY sale_timestamp",
        (FOCUS_PRODUCT_ID, since),
    ).fetchall()

    platforms = Counter(row["platform"] for row in posts)
    variants = Counter()
    tracked = 0
    for row in posts:
        query = parse_qs(urlsplit(row["url"] or "").query)
        if query.get("utm_campaign", [""])[0] == CAMPAIGN:
            tracked += 1
            variants[query.get("utm_content", ["unknown"])[0]] += 1

    valid_sales = [s for s in sales if not s["refunded"] and not s["disputed"]]
    return {
        "campaign": CAMPAIGN,
        "product": FOCUS_PRODUCT_NAME,
        "since": since,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "posts": len(posts),
        "tracked_posts": tracked,
        "posts_by_platform": dict(sorted(platforms.items())),
        "variants": dict(sorted(variants.items())),
        "sales": len(valid_sales),
        "gross_revenue_eur": round(sum(s["price_cents"] or 0 for s in valid_sales) / 100, 2),
        "refunds_or_disputes": len(sales) - len(valid_sales),
        "latest_post_at": posts[-1]["posted_at"] if posts else None,
        "latest_sale_at": sales[-1]["sale_timestamp"] if sales else None,
        "analytics_note": "Open Gumroad Analytics to compare page views by UTM source; the CLI does not expose views.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", default=DEFAULT_SINCE, help="ISO-8601 campaign start")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)
    if not DB_PATH.exists():
        parser.error("db/store.db missing; run python3 db/sync.py")
    with sqlite3.connect(DB_PATH) as con:
        report = collect(con, args.since)
    if args.json:
        print(json.dumps(report, indent=2))
        return 0
    print(f"Campaign: {report['campaign']}")
    print(f"Product:  {report['product']}")
    print(f"Since:    {report['since']}")
    print(f"Posts:    {report['posts']} ({report['tracked_posts']} campaign-tracked)")
    print(f"Channels: {report['posts_by_platform'] or 'none yet'}")
    print(f"Variants: {report['variants'] or 'none yet'}")
    print(f"Sales:    {report['sales']} | Revenue: €{report['gross_revenue_eur']:.2f}")
    print(f"Note:     {report['analytics_note']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
