#!/usr/bin/env bash
# GET /v2/sales — List sales (optional: product_id, after, before, email)
# Usage: ./list-sales.sh [product_id] [after_date] [before_date]
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"

ARGS=(--all)
[ -n "${1:-}" ] && ARGS+=(--product "$1")
[ -n "${2:-}" ] && ARGS+=(--after "$2")
[ -n "${3:-}" ] && ARGS+=(--before "$3")
gumroad_cli sales list "${ARGS[@]}" | jq .
