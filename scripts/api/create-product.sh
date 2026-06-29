#!/usr/bin/env bash
# Create a new product through the Gumroad CLI.
# Usage: ./create-product.sh "Product Name" 999 "Description text"
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"

NAME="${1:?Usage: create-product.sh NAME PRICE_CENTS [DESCRIPTION]}"
PRICE_CENTS="${2:?Provide price in cents (e.g. 999 for \$9.99)}"
DESC="${3:-}"
PRICE="$(awk -v cents="$PRICE_CENTS" 'BEGIN { printf "%.2f", cents / 100 }')"

gumroad_cli products create --name "$NAME" --price "$PRICE" --description "$DESC" | jq .
