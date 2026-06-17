#!/usr/bin/env bash
# GET /v2/payouts — List all payouts
# Usage: ./list-payouts.sh
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"

gumroad_get "payouts" | jq .
