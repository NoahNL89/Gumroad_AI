#!/bin/bash
# Daily bot runner — promote + engage on both platforms
# Add to crontab: 37 9 * * * cd /home/administrator/NewGitHub/GumRoad_AI && bash scripts/run_bots.sh >> /tmp/schep_bots.log 2>&1
# And afternoon:  13 15 * * * cd /home/administrator/NewGitHub/GumRoad_AI && bash scripts/run_bots.sh >> /tmp/schep_bots.log 2>&1

cd "$(dirname "$0")/.."
export $(grep -v '^#' .env | xargs) 2>/dev/null

echo "=== $(date -u '+%Y-%m-%d %H:%M UTC') Bot Run ==="

echo "-- Mastodon promote --"
python3 bot/mastodon_bot.py promote

echo "-- Mastodon engage --"
python3 bot/mastodon_bot.py engage

echo "-- Bluesky promote --"
python3 bot/bluesky_bot.py promote

echo "-- Bluesky engage --"
python3 bot/bluesky_bot.py engage

echo "=== Done ==="
