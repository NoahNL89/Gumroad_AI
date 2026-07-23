#!/usr/bin/env bash
# go.sh — Autonomous Codex store session launcher.
# Scope is bounded by agent/GO.md — only store management actions are defined there.
#
# Usage:
#   bash scripts/go.sh
#   bash scripts/go.sh --agent codex    # accepted for backwards compatibility
#
# Crontab (runs Codex every morning and evening, UTC):
#   7 8 * * * cd /home/administrator/NewGitHub/GumRoad_AI && bash scripts/go.sh >> /tmp/schep_go.log 2>&1
#   7 18 * * * cd /home/administrator/NewGitHub/GumRoad_AI && bash scripts/go.sh >> /tmp/schep_go.log 2>&1

set -euo pipefail
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/bin:$PATH"
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

# Codex is the only permitted unattended agent. Keep the old --agent codex
# spelling working so existing service definitions do not need a coordinated
# migration, but reject every other agent explicitly.
AGENT="codex"
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --agent)
            [[ "$#" -ge 2 ]] || { echo "ERROR: --agent requires codex"; exit 1; }
            [[ "$2" == "codex" ]] || { echo "ERROR: only Codex is permitted for GO runs"; exit 1; }
            shift
            ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
    shift
done

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

if [[ -z "$CODEX" || ! -x "$CODEX" ]]; then
    echo "ERROR: Codex CLI not found. Install it on PATH or set CODEX_BIN to its executable path."
    exit 1
fi
echo "Using Codex CLI: $CODEX ($("$CODEX" --version 2>/dev/null || echo "version unknown"))"
"$CODEX" exec "$PROMPT"

# Deterministic fallback: if the agent did not close a due experiment, snapshot
# the measurable funnel and save a decision. Before the due date this is a no-op.
python3 scripts/evaluate_experiment.py
python3 scripts/ops_notify.py go-summary --before-head "$BEFORE_HEAD" || true

echo "=== [$TS] GO session complete ==="
