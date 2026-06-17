#!/usr/bin/env bash
# PUT /v2/products/:id — Update an existing product
# Usage: ./update-product.sh PRODUCT_ID [--name "Name"] [--price 999] [--description "Desc"]
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"

PRODUCT_ID="${1:?Usage: update-product.sh PRODUCT_ID [--name NAME] [--price CENTS] [--description DESC]}"
shift

ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --name) ARGS+=(--data-urlencode "name=$2"); shift 2 ;;
    --price) ARGS+=(--data-urlencode "price=$2"); shift 2 ;;
    --description) ARGS+=(--data-urlencode "description=$2"); shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

gumroad_put "products/$PRODUCT_ID" "${ARGS[@]}" | jq .
