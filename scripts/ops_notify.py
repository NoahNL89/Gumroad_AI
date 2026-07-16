#!/usr/bin/env python3
"""Operational Pushover alerts for GO runs, failures, and month-end reports."""
import argparse
import json
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "store.db"
sys.path.insert(0, str(ROOT / "scripts"))
from campaign_report import collect  # noqa: E402
from pushover_notify import send_message, send_once  # noqa: E402

STORE_URL = "https://schephenk.gumroad.com"


def git_value(*args):
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def db_totals(con, month=None):
    where = "WHERE COALESCE(refunded,0)=0 AND COALESCE(disputed,0)=0"
    params = []
    if month:
        where += " AND substr(sale_timestamp,1,7)=?"
        params.append(month)
    row = con.execute(
        f"SELECT COUNT(*), COALESCE(SUM(price_cents),0) FROM sales {where}", params
    ).fetchone()
    return int(row[0]), round((row[1] or 0) / 100, 2)


def go_summary(before_head=None, dry_run=False):
    head = git_value("rev-parse", "HEAD")
    subject = git_value("log", "-1", "--pretty=%s")
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        sales, revenue = db_totals(con)
        report = collect(con, "2026-07-16T00:00:00+00:00")
    changed = not before_head or head != before_head
    event_key = f"go:{head}:{sales}:{revenue:.2f}"
    if not changed and sales == 0:
        return {"status": 1, "skipped": True, "reason": "no important change"}
    message = (
        f"{subject}\n"
        f"Lifetime: {sales} sales · €{revenue:.2f}\n"
        f"Campaign: {report['free_downloads']} free · {report['core_sales']} core · "
        f"{report['bundle_sales']} bundle · €{report['gross_revenue_eur']:.2f}"
    )
    return send_once(
        event_key,
        "Schep Digital GO completed",
        message,
        priority=0 if sales == 0 else 1,
        url=STORE_URL,
        url_title="Open store",
        dry_run=dry_run,
    )


def is_last_day(day=None):
    day = day or datetime.now(timezone.utc).date()
    return (day + timedelta(days=1)).month != day.month


def month_end(if_due=False, dry_run=False):
    now = datetime.now(timezone.utc)
    if if_due and not is_last_day(now.date()):
        return {"status": 1, "skipped": True, "reason": "not the last UTC day of month"}
    month = now.strftime("%Y-%m")
    with sqlite3.connect(DB_PATH) as con:
        sales, revenue = db_totals(con, month)
        live_products = con.execute(
            "SELECT COUNT(*) FROM products WHERE published=1"
        ).fetchone()[0]
        followers = {}
        table = con.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='audience_snapshots'"
        ).fetchone()
        if table:
            for platform in ("mastodon", "bluesky"):
                row = con.execute(
                    "SELECT followers FROM audience_snapshots WHERE platform=? "
                    "ORDER BY captured_at DESC LIMIT 1", (platform,)
                ).fetchone()
                if row:
                    followers[platform] = row[0]
    target = 58.0
    gap = max(0, target - revenue)
    audience = " · ".join(f"{k} {v}" for k, v in followers.items()) or "not captured"
    message = (
        f"{month}: {sales} sales · €{revenue:.2f}\n"
        f"Target: €{target:.2f} · gap €{gap:.2f}\n"
        f"Live products: {live_products}\nAudience: {audience}"
    )
    return send_once(
        f"month_end:{month}",
        f"Schep Digital month-end · {month}",
        message,
        priority=1 if revenue < target else 0,
        url=STORE_URL,
        url_title="Open store",
        dry_run=dry_run,
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    go = sub.add_parser("go-summary")
    go.add_argument("--before-head")
    go.add_argument("--dry-run", action="store_true")
    failure = sub.add_parser("failure")
    failure.add_argument("--message", required=True)
    failure.add_argument("--dry-run", action="store_true")
    month = sub.add_parser("month-end")
    month.add_argument("--if-due", action="store_true")
    month.add_argument("--dry-run", action="store_true")
    test = sub.add_parser("test")
    test.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if args.command == "go-summary":
        result = go_summary(args.before_head, args.dry_run)
    elif args.command == "failure":
        result = send_once(
            f"go_failure:{datetime.now(timezone.utc).strftime('%Y%m%d%H')}:{args.message[:80]}",
            "Schep Digital automation failed",
            args.message,
            priority=1,
            url=STORE_URL,
            url_title="Open store",
            dry_run=args.dry_run,
        )
    elif args.command == "month-end":
        result = month_end(args.if_due, args.dry_run)
    else:
        result = send_message(
            "Schep Digital notifications active",
            "Pushover is connected. Important GO actions, experiment dates, failures, Pinterest drafts, and month-end results can now reach this device.",
            url=STORE_URL,
            url_title="Open store",
            dry_run=args.dry_run,
        )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
