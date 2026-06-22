#!/bin/bash
# go.sh — Autonomous store session launcher with automatic agent rotation.
# User-authorized: runs with --dangerously-skip-permissions for unattended cron.
# Scope is bounded by agent/GO.md — only store management actions are defined there.
#
# Usage:
#   bash scripts/go.sh                  # auto-rotate between agents (claude → agy → codex → ...)
#   bash scripts/go.sh --agent claude   # force a specific agent
#   bash scripts/go.sh --agent agy
#   bash scripts/go.sh --agent codex
#
# Crontab (runs every day at 8:07am — agent rotates automatically):
#   7 8 * * * cd /home/administrator/NewGitHub/GumRoad_AI && bash scripts/go.sh >> /tmp/schep_go.log 2>&1

set -e
cd "$(dirname "$0")/.."

ROTATION_FILE=".agent_rotation"
AGENTS=("claude" "agy" "codex")

# Parse --agent override
AGENT=""
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --agent) AGENT="$2"; shift ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
    shift
done

# Auto-rotate if no agent specified
if [[ -z "$AGENT" ]]; then
    # Read last used agent
    LAST_AGENT=""
    if [[ -f "$ROTATION_FILE" ]]; then
        LAST_AGENT=$(cat "$ROTATION_FILE")
    fi

    # Find the next agent in the rotation
    NEXT_INDEX=0
    for i in "${!AGENTS[@]}"; do
        if [[ "${AGENTS[$i]}" == "$LAST_AGENT" ]]; then
            NEXT_INDEX=$(( (i + 1) % ${#AGENTS[@]} ))
            break
        fi
    done

    AGENT="${AGENTS[$NEXT_INDEX]}"
    echo "$AGENT" > "$ROTATION_FILE"
fi

PROMPT_FILE="agent/GO.md"
if [ ! -f "$PROMPT_FILE" ]; then
    echo "ERROR: $PROMPT_FILE not found"
    exit 1
fi

PROMPT=$(cat "$PROMPT_FILE")
TS=$(date -u '+%Y-%m-%d %H:%M UTC')
echo "=== [$TS] GO session — agent: $AGENT ==="

CODEX="/home/administrator/.openclaw/npm/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/codex/codex"

case "$AGENT" in
    claude)
        /home/administrator/.local/bin/claude \
            --dangerously-skip-permissions \
            -p "$PROMPT"
        ;;
    agy)
        /home/administrator/.local/bin/agy \
            --dangerously-skip-permissions \
            -p "$PROMPT"
        ;;
    codex)
        "$CODEX" exec "$PROMPT"
        ;;
    *)
        echo "Unknown agent: $AGENT. Use: claude | agy | codex"
        exit 1
        ;;
esac

echo "=== [$TS] GO session complete ==="
