#!/usr/bin/env bash
# POST /v2/licenses/verify — Verify a license key
# Usage: ./verify-license.sh <product_id> <license_key> [increment_uses_count]
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIR/_base.sh"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
PRODUCT_ID="${1:?Provide product_id (permalink)}"
LICENSE_KEY="${2:?Provide license_key}"
INCREMENT="${3:-false}"
gumroad_post "licenses/verify" \
  --data-urlencode "product_id=$PRODUCT_ID" \
  --data-urlencode "license_key=$LICENSE_KEY" \
  --data-urlencode "increment_uses_count=$INCREMENT" | jq .
