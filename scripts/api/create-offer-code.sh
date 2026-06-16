#!/usr/bin/env bash
# POST /v2/products/:product_id/offer_codes — Create offer code
# Usage: ./create-offer-code.sh <product_id> <name> <percent_off>
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIR/_base.sh"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
PRODUCT_ID="${1:?Provide product_id}"
NAME="${2:?Provide code name}"
PERCENT="${3:?Provide percent_off}"
gumroad_post "products/$PRODUCT_ID/offer_codes" \
  --data-urlencode "name=$NAME" \
  --data-urlencode "offer_type=percent" \
  --data-urlencode "amount_off=$PERCENT" | jq .
