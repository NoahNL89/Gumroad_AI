#!/usr/bin/env bash
# POST /v2/products/:product_id/offer_codes — Create offer code
# Usage: ./create-offer-code.sh <product_id> <name> <percent_off>
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"
PRODUCT_ID="${1:?Provide product_id}"
NAME="${2:?Provide code name}"
PERCENT="${3:?Provide percent_off}"
gumroad_cli offer-codes create \
  --product "$PRODUCT_ID" --name "$NAME" --percent-off "$PERCENT" --yes | jq .
