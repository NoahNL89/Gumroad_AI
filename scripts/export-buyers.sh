#!/usr/bin/env bash
# export-buyers.sh — Export buyer email list to CSV
# Usage: ./scripts/export-buyers.sh [product_id]
#   With product_id: exports buyers of that product only
#   Without:         exports all buyers across all products

set -euo pipefail

PRODUCT_ID="${1:-}"
OUTPUT_FILE="buyers-$(date +%Y%m%d-%H%M%S).csv"

echo "=== Export Buyer Emails ==="

if [[ -n "$PRODUCT_ID" ]]; then
  echo "Product: $PRODUCT_ID"
  FLAGS="--product $PRODUCT_ID"
else
  echo "Scope: all products"
  FLAGS=""
fi

echo "Output: $OUTPUT_FILE"
echo ""
echo "Fetching sales..."

# Write CSV header
echo "email,name,product,price,date,sale_id" > "$OUTPUT_FILE"

# Fetch all sales and extract buyer data
# shellcheck disable=SC2086
gumroad sales list \
  $FLAGS \
  --all \
  --page-delay 200ms \
  --json --no-input | jq -r '
    .sales[] |
    [
      (.email // ""),
      (.full_name // ""),
      (.product_name // ""),
      (.formatted_display_price // ""),
      (.created_at // ""),
      (.id // "")
    ] | @csv
  ' >> "$OUTPUT_FILE"

COUNT=$(tail -n +2 "$OUTPUT_FILE" | wc -l | tr -d ' ')
echo "✅ Exported $COUNT buyers to $OUTPUT_FILE"
