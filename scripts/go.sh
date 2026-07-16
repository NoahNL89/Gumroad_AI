#!/usr/bin/env bash
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

set -euo pipefail
cd "$(dirname "$0")/.."
BEFORE_HEAD=$(git rev-parse HEAD 2>/dev/null || echo unknown)

notify_failure() {
    local code=$?
    local line=${1:-unknown}
    trap - ERR
    python3 scripts/ops_notify.py failure \
        --message "GO failed on line ${line} with exit code ${code}. Check /tmp/schep_go.log." || true
    exit "$code"
}
trap 'notify_failure $LINENO' ERR

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

EVALUATION_CONTEXT=$(python3 scripts/evaluate_experiment.py --status)
PROMPT="$(cat "$PROMPT_FILE")

AUTOMATIC EXPERIMENT DATE GATE
${EVALUATION_CONTEXT}
Use this machine-generated gate. If due=true, perform the evaluation now without
asking the user or waiting for manual page-view data."
TS=$(date -u '+%Y-%m-%d %H:%M UTC')
echo "=== [$TS] GO session — agent: $AGENT ==="

CODEX="${CODEX_BIN:-}"
if [[ -z "$CODEX" ]]; then
    CODEX=$(command -v codex 2>/dev/null || true)
fi
if [[ -z "$CODEX" && -x "/home/administrator/.local/bin/codex" ]]; then
    CODEX="/home/administrator/.local/bin/codex"
fi

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
        if [[ -z "$CODEX" || ! -x "$CODEX" ]]; then
            echo "ERROR: Codex CLI not found. Install it on PATH or set CODEX_BIN to its executable path."
            exit 1
        fi
        echo "Using Codex CLI: $CODEX ($("$CODEX" --version 2>/dev/null || echo "version unknown"))"
        "$CODEX" exec "$PROMPT"
        ;;
    *)
        echo "Unknown agent: $AGENT. Use: claude | agy | codex"
        exit 1
        ;;
esac

# Deterministic fallback: if the agent did not close a due experiment, snapshot
# the measurable funnel and save a decision. Before the due date this is a no-op.
python3 scripts/evaluate_experiment.py
python3 scripts/ops_notify.py go-summary --before-head "$BEFORE_HEAD" || true

echo "=== [$TS] GO session complete ==="
