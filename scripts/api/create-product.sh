#!/usr/bin/env bash
# POST /v2/products — Create a new product
# Usage: ./create-product.sh "Product Name" 999 "Description text"
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"

NAME="${1:?Usage: create-product.sh NAME PRICE_CENTS [DESCRIPTION]}"
PRICE="${2:?Provide price in cents (e.g. 999 for \$9.99)}"
DESC="${3:-}"

gumroad_post "products" \
  --data-urlencode "name=$NAME" \
  --data-urlencode "price=$PRICE" \
  --data-urlencode "description=$DESC" | jq .
