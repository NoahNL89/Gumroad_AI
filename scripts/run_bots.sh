#!/usr/bin/env bash
# Daily bot runner — promote + engage on both platforms
set -u

cd "$(dirname "$0")/.."
set -a
# shellcheck disable=SC1091
source .env
set +a

echo "=== $(date -u '+%Y-%m-%d %H:%M UTC') Bot Run ==="

echo "-- Mastodon promote --"
python3 bot/mastodon_bot.py promote

echo "-- Mastodon engage --"
python3 bot/mastodon_bot.py engage

echo "-- Bluesky promote --"
python3 bot/bluesky_bot.py promote

echo "-- Bluesky engage --"
python3 bot/bluesky_bot.py engage

echo "-- Pinterest promote --"
# `promote` is queue-safe: it will not pile up drafts awaiting review.
python3 bot/pinterest_bot.py promote

echo "=== Done ==="
