#!/usr/bin/env python3
"""Small, idempotent Pushover client for Schep Digital automation."""
import json
import os
import sqlite3
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
DB_PATH = ROOT / "db" / "store.db"
API_URL = "https://api.pushover.net/1/messages.json"


def load_env():
    if not ENV_PATH.exists():
        return
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def ensure_table(con):
    con.execute("""
        CREATE TABLE IF NOT EXISTS notification_events (
            event_key TEXT PRIMARY KEY,
            title TEXT,
            sent_at TEXT,
            provider TEXT,
            provider_request_id TEXT
        )
    """)


def send_message(title, message, priority=0, url=None, url_title=None, dry_run=False):
    """Send one message without ever printing credential values."""
    payload = {
        "title": str(title)[:250],
        "message": str(message)[:1024],
        "priority": str(priority),
    }
    if url:
        payload["url"] = str(url)[:512]
    if url_title:
        payload["url_title"] = str(url_title)[:100]
    if dry_run:
        return {"status": 1, "dry_run": True, "payload": payload}

    load_env()
    user = os.environ.get("PUSHOVER_USERKEY")
    token = os.environ.get("PUSHOVER_APPKEY")
    if not user or not token:
        raise RuntimeError("PUSHOVER_USERKEY or PUSHOVER_APPKEY is missing from .env")
    body = urllib.parse.urlencode({"user": user, "token": token, **payload}).encode()
    request = urllib.request.Request(
        API_URL,
        data=body,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            result = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        raise RuntimeError(f"Pushover rejected the notification: HTTP {exc.code} {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Pushover request failed: {exc.reason}") from exc
    if result.get("status") != 1:
        raise RuntimeError(f"Pushover returned an error: {result.get('errors', ['unknown error'])}")
    return result


def send_once(event_key, title, message, priority=0, url=None, url_title=None, dry_run=False):
    """Send an event once; successful sends are deduplicated in the local DB."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as con:
        ensure_table(con)
        if con.execute(
            "SELECT 1 FROM notification_events WHERE event_key=?", (event_key,)
        ).fetchone():
            return {"status": 1, "duplicate": True, "event_key": event_key}
        result = send_message(title, message, priority, url, url_title, dry_run=dry_run)
        if not dry_run:
            con.execute(
                "INSERT INTO notification_events "
                "(event_key, title, sent_at, provider, provider_request_id) VALUES (?,?,?,?,?)",
                (
                    event_key,
                    title,
                    datetime.now(timezone.utc).isoformat(),
                    "pushover",
                    result.get("request"),
                ),
            )
    return result
