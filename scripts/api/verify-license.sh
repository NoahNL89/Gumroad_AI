#!/usr/bin/env bash
# POST /v2/licenses/verify — Verify a license key
# Usage: ./verify-license.sh <product_id> <license_key> [increment_uses_count]
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"
PRODUCT_ID="${1:?Provide product_id (permalink)}"
LICENSE_KEY="${2:?Provide license_key}"
INCREMENT="${3:-false}"
ARGS=(--product "$PRODUCT_ID")
[ "$INCREMENT" = "true" ] || ARGS+=(--no-increment)
printf '%s\n' "$LICENSE_KEY" | gumroad_cli licenses verify "${ARGS[@]}" | jq .
