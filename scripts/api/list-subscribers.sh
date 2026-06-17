#!/usr/bin/env bash
# GET /v2/products/:product_id/subscribers — List subscribers for a product
# Usage: ./list-subscribers.sh <product_id>
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"
PRODUCT_ID="${1:?Provide product_id}"
gumroad_get "products/$PRODUCT_ID/subscribers" | jq .
