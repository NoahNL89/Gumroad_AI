#!/usr/bin/env python3
"""Capture Mastodon and Bluesky audience totals in the local store database."""
import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "store.db"
sys.path.insert(0, str(ROOT / "bot"))


def value(obj, *names, default=0):
    for name in names:
        if isinstance(obj, dict) and name in obj:
            return obj[name]
        if hasattr(obj, name):
            return getattr(obj, name)
    return default


def mastodon_metrics():
    from mastodon_bot import get_client

    account = get_client().me()
    return {
        "platform": "mastodon",
        "followers": int(value(account, "followers_count")),
        "following": int(value(account, "following_count")),
        "posts": int(value(account, "statuses_count")),
    }


def bluesky_metrics():
    from bluesky_bot import get_client

    client = get_client()
    actor = value(client.me, "did", "handle", default=None)
    if not actor:
        raise RuntimeError("Bluesky login succeeded but returned no account DID or handle")
    profile = client.get_profile(actor)
    return {
        "platform": "bluesky",
        "followers": int(value(profile, "followers_count", "followersCount")),
        "following": int(value(profile, "follows_count", "followsCount")),
        "posts": int(value(profile, "posts_count", "postsCount")),
    }


def ensure_table(con):
    con.executescript("""
        CREATE TABLE IF NOT EXISTS audience_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT NOT NULL,
            followers INTEGER,
            following INTEGER,
            posts INTEGER,
            captured_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_audience_platform
            ON audience_snapshots(platform, captured_at);
    """)


def capture(platforms):
    captured_at = datetime.now(timezone.utc).isoformat()
    fetchers = {"mastodon": mastodon_metrics, "bluesky": bluesky_metrics}
    rows = []
    for platform in platforms:
        row = fetchers[platform]()
        row["captured_at"] = captured_at
        rows.append(row)
    with sqlite3.connect(DB_PATH) as con:
        ensure_table(con)
        con.executemany(
            "INSERT INTO audience_snapshots "
            "(platform, followers, following, posts, captured_at) VALUES (?,?,?,?,?)",
            [(r["platform"], r["followers"], r["following"], r["posts"], captured_at) for r in rows],
        )
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--platform", choices=("all", "mastodon", "bluesky"), default="all"
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    platforms = ["mastodon", "bluesky"] if args.platform == "all" else [args.platform]
    rows = capture(platforms)
    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        for row in rows:
            print(
                f"{row['platform']}: {row['followers']} followers, "
                f"{row['following']} following, {row['posts']} posts"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
