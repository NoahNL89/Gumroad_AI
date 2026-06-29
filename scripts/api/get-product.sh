#!/usr/bin/env bash
# GET /v2/products/:id — Get a single product by ID
# Usage: ./get-product.sh PRODUCT_ID
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"

PRODUCT_ID="${1:?Usage: get-product.sh PRODUCT_ID}"
gumroad_cli products view "$PRODUCT_ID" | jq .
