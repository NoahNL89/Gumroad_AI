#!/usr/bin/env bash
# sales-report.sh — Generate a sales summary report
# Usage: ./scripts/sales-report.sh [YYYY-MM-DD] [YYYY-MM-DD]
#   Example: ./scripts/sales-report.sh 2026-01-01 2026-06-30
#   Default: current month

set -euo pipefail

FROM="${1:-$(date +%Y-%m-01)}"
TO="${2:-$(date +%Y-%m-%d)}"

echo "=== Gumroad Sales Report ==="
echo "Period: $FROM to $TO"
echo ""

echo "--- Sales Summary ---"
gumroad sales summary \
  --group-by month \
  --from "$FROM" \
  --json --no-input | jq '{
    gross: (.gross_cents / 100 | tostring | . + " USD"),
    net: (.net_cents / 100 | tostring | . + " USD"),
    breakdown: [.breakdown[] | {
      period: .period,
      gross: (.gross_cents / 100 | tostring | . + " USD"),
      count: .count
    }]
  }'

echo ""
echo "--- Recent Sales ---"
gumroad sales list \
  --after "$FROM" \
  --all \
  --page-delay 200ms \
  --json --no-input | jq '[
    .sales[] | {
      id,
      email,
      product_name,
      price: .formatted_display_price,
      date: .created_at
    }
  ] | sort_by(.date) | reverse | .[0:20]'
