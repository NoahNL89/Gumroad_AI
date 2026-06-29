#!/usr/bin/env bash
# Update an existing product through the Gumroad CLI.
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
    --name) ARGS+=(--name "$2"); shift 2 ;;
    --price)
      PRICE="$(awk -v cents="$2" 'BEGIN { printf "%.2f", cents / 100 }')"
      ARGS+=(--price "$PRICE")
      shift 2
      ;;
    --description) ARGS+=(--description "$2"); shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

gumroad_cli products update "$PRODUCT_ID" "${ARGS[@]}" --yes | jq .
