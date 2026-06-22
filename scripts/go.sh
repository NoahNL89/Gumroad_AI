#!/bin/bash
# go.sh — Autonomous store session launcher.
# Runs agent/GO.md through your chosen AI agent.
#
# Usage:
#   bash scripts/go.sh                  # default: claude
#   bash scripts/go.sh --agent claude
#   bash scripts/go.sh --agent agy
#   bash scripts/go.sh --agent codex
#
# Crontab (runs every day at 8:07am):
#   7 8 * * * cd /home/administrator/NewGitHub/GumRoad_AI && bash scripts/go.sh --agent claude >> /tmp/schep_go.log 2>&1

set -e
cd "$(dirname "$0")/.."

AGENT="claude"
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --agent) AGENT="$2"; shift ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
    shift
done

PROMPT_FILE="agent/GO.md"
if [ ! -f "$PROMPT_FILE" ]; then
    echo "ERROR: $PROMPT_FILE not found"
    exit 1
fi

PROMPT=$(cat "$PROMPT_FILE")
TS=$(date -u '+%Y-%m-%d %H:%M UTC')
echo "=== [$TS] GO session — agent: $AGENT ==="

case "$AGENT" in
    claude)
        /home/administrator/.local/bin/claude \
            -p "$PROMPT"
        ;;
    agy)
        /home/administrator/.local/bin/agy \
            -p "$PROMPT"
        ;;
    codex)
        /home/administrator/.openclaw/npm/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex/codex \
            exec "$PROMPT"
        ;;
    *)
        echo "Unknown agent: $AGENT. Use: claude | agy | codex"
        exit 1
        ;;
esac

echo "=== [$TS] GO session complete ==="
