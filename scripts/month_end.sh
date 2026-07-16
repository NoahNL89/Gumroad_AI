#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# Safe to schedule daily: only the final UTC day performs network work.
if [[ "$(date -u -d tomorrow +%d)" != "01" ]]; then
    exit 0
fi

set -a
# shellcheck disable=SC1091
source .env
set +a
python3 db/sync.py
python3 scripts/audience_metrics.py --json
python3 scripts/ops_notify.py month-end --if-due
