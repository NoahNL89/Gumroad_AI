#!/usr/bin/env bash
# GET /v2/sales — List sales (optional: product_id, after, before, email)
# Usage: ./list-sales.sh [product_id] [after_date] [before_date]
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIR/_base.sh"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"

ARGS=()
[ -n "${1:-}" ] && ARGS+=(--data-urlencode "product_id=$1")
[ -n "${2:-}" ] && ARGS+=(--data-urlencode "after=$2")
[ -n "${3:-}" ] && ARGS+=(--data-urlencode "before=$3")
gumroad_get "sales" "${ARGS[@]}" | jq .
