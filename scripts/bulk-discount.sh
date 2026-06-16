#!/usr/bin/env bash
# bulk-discount.sh — Create multiple offer codes across products
# Usage: ./scripts/bulk-discount.sh <product_id> <percent_off> <code_prefix> <count>
#   Example: ./scripts/bulk-discount.sh abc123 20 LAUNCH 5
#   Creates: LAUNCH1, LAUNCH2, ... LAUNCH5 (all 20% off)

set -euo pipefail

PRODUCT_ID="${1:?Usage: $0 <product_id> <percent_off> <code_prefix> <count>}"
PERCENT_OFF="${2:?}"
PREFIX="${3:?}"
COUNT="${4:?}"

echo "=== Bulk Offer Code Creation ==="
echo "Product: $PRODUCT_ID"
echo "Discount: $PERCENT_OFF% off"
echo "Creating $COUNT codes with prefix '$PREFIX'..."
echo ""

for i in $(seq 1 "$COUNT"); do
  CODE="${PREFIX}${i}"
  echo -n "Creating $CODE... "
  RESULT=$(gumroad offer-codes create \
    --product "$PRODUCT_ID" \
    --name "$CODE" \
    --percent-off "$PERCENT_OFF" \
    --json --no-input)
  CODE_ID=$(echo "$RESULT" | jq -r '.offer_code.id // "error"')
  echo "✅ ID: $CODE_ID"
done

echo ""
echo "Done! All $COUNT codes created."
echo "List them with:"
echo "  gumroad offer-codes list --product $PRODUCT_ID --json --no-input"
