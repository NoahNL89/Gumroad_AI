#!/usr/bin/env python3
"""Report the focused campaign's measurable acquisition and sales funnel."""
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
from campaign import (  # noqa: E402
    BUNDLE_PRODUCT_ID,
    BUNDLE_PRODUCT_NAME,
    CAMPAIGN,
    CAMPAIGN_PRODUCT_ID,
    FOCUS_PRODUCT_ID,
    FOCUS_PRODUCT_NAME,
    LEAD_PRODUCT_ID,
    LEAD_PRODUCT_NAME,
)

EXPERIMENT_PATH = ROOT / "agent" / "growth_experiments.json"
FALLBACK_SINCE = "2026-07-30T08:11:17+00:00"


def active_since():
    try:
        active = json.loads(EXPERIMENT_PATH.read_text()).get("active") or {}
        return active.get("started_at") or FALLBACK_SINCE
    except (OSError, json.JSONDecodeError):
        return FALLBACK_SINCE


def valid_sales(con, product_id, since):
    return con.execute(
        "SELECT price_cents, sale_timestamp FROM sales "
        "WHERE product_id=? AND sale_timestamp>=? "
        "AND COALESCE(refunded,0)=0 AND COALESCE(disputed,0)=0 "
        "ORDER BY sale_timestamp",
        (product_id, since),
    ).fetchall()


def audience_change(con, since):
    exists = con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='audience_snapshots'"
    ).fetchone()
    if not exists:
        return {}
    changes = {}
    for platform in ("mastodon", "bluesky"):
        latest = con.execute(
            "SELECT followers, following, posts, captured_at FROM audience_snapshots "
            "WHERE platform=? ORDER BY captured_at DESC LIMIT 1", (platform,)
        ).fetchone()
        if not latest:
            continue
        baseline = con.execute(
            "SELECT followers, following, posts, captured_at FROM audience_snapshots "
            "WHERE platform=? AND captured_at>=? ORDER BY captured_at LIMIT 1",
            (platform, since),
        ).fetchone() or latest
        changes[platform] = {
            "followers": latest["followers"],
            "follower_change": latest["followers"] - baseline["followers"],
            "following": latest["following"],
            "posts": latest["posts"],
            "baseline_at": baseline["captured_at"],
            "latest_at": latest["captured_at"],
        }
    return changes


def collect(con, since):
    con.row_factory = sqlite3.Row
    posts = con.execute(
        "SELECT platform, url, posted_at FROM promotions "
        "WHERE product_id=? AND posted_at>=? ORDER BY posted_at",
        (CAMPAIGN_PRODUCT_ID, since),
    ).fetchall()
    leads = valid_sales(con, LEAD_PRODUCT_ID, since)
    focus_sales = valid_sales(con, FOCUS_PRODUCT_ID, since)
    bundle_sales = valid_sales(con, BUNDLE_PRODUCT_ID, since)

    platforms = Counter(row["platform"] for row in posts)
    variants = Counter()
    tracked = 0
    for row in posts:
        query = parse_qs(urlsplit(row["url"] or "").query)
        if query.get("utm_campaign", [""])[0] == CAMPAIGN:
            tracked += 1
            variants[query.get("utm_content", ["unknown"])[0]] += 1

    paid_sales = len(focus_sales) + len(bundle_sales)
    revenue_cents = sum(row["price_cents"] or 0 for row in focus_sales + bundle_sales)
    return {
        "campaign": CAMPAIGN,
        "since": since,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "products": {
            "lead": LEAD_PRODUCT_NAME,
            "core": FOCUS_PRODUCT_NAME,
            "upgrade": BUNDLE_PRODUCT_NAME,
        },
        "posts": len(posts),
        "tracked_posts": tracked,
        "posts_by_platform": dict(sorted(platforms.items())),
        "variants": dict(sorted(variants.items())),
        "free_downloads": len(leads),
        "core_sales": len(focus_sales),
        "bundle_sales": len(bundle_sales),
        "paid_sales": paid_sales,
        "period_lead_to_paid_ratio_pct": round(paid_sales / len(leads) * 100, 1) if leads else None,
        "gross_revenue_eur": round(revenue_cents / 100, 2),
        "audience": audience_change(con, since),
        "latest_post_at": posts[-1]["posted_at"] if posts else None,
        "analytics_note": (
            "Enter Gumroad UTM page views in agent/growth_experiments.json at review time; "
            "the CLI does not expose page views or identify whether a bundle sale came through an upsell. "
            "The lead-to-paid figure is a campaign-period ratio, not cohort attribution."
        ),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", default=active_since(), help="ISO-8601 campaign start")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)
    if not DB_PATH.exists():
        parser.error("db/store.db missing; run python3 db/sync.py")
    with sqlite3.connect(DB_PATH) as con:
        report = collect(con, args.since)
    if args.json:
        print(json.dumps(report, indent=2))
        return 0
    print(f"Campaign: {report['campaign']} | since {report['since']}")
    print(f"Posts: {report['posts']} ({report['tracked_posts']} tracked) | {report['posts_by_platform'] or 'none'}")
    print(f"Variants: {report['variants'] or 'none'}")
    print(
        f"Funnel: {report['free_downloads']} free downloads → "
        f"{report['core_sales']} core sales → {report['bundle_sales']} bundle sales"
    )
    rate = "n/a" if report["period_lead_to_paid_ratio_pct"] is None else f"{report['period_lead_to_paid_ratio_pct']}%"
    print(f"Period lead/paid ratio: {rate} | Revenue: €{report['gross_revenue_eur']:.2f}")
    for platform, row in report["audience"].items():
        print(f"{platform}: {row['followers']} followers ({row['follower_change']:+d})")
    print(f"Note: {report['analytics_note']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
