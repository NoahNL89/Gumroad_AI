#!/usr/bin/env bash
# ledger.sh — Show current month's revenue vs survival targets
set -euo pipefail

MONTH_START=$(date +%Y-%m-01)
TODAY=$(date +%Y-%m-%d)
LEDGER="$(dirname "$0")/ledger.json"

MIN_TARGET=$(jq -r '.targets.monthly_minimum_eur' "$LEDGER")
GROWTH_TARGET=$(jq -r '.targets.monthly_growth_eur' "$LEDGER")

echo "╔══════════════════════════════════════════╗"
echo "║       🤖 Agent Survival Dashboard        ║"
echo "╠══════════════════════════════════════════╣"
echo "║  Period: $MONTH_START → $TODAY     ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# Fetch current month revenue
echo "Fetching sales data..."
SUMMARY=$(gumroad sales summary \
  --from "$MONTH_START" \
  --json --no-input --quiet 2>/dev/null || echo '{"gross_cents":0,"net_cents":0}')

GROSS_CENTS=$(echo "$SUMMARY" | jq -r '.gross_cents // 0')
NET_CENTS=$(echo "$SUMMARY" | jq -r '.net_cents // 0')
GROSS_EUR=$(echo "scale=2; $GROSS_CENTS / 100" | bc)
NET_EUR=$(echo "scale=2; $NET_CENTS / 100" | bc)

echo "  💰 Gross revenue this month: €$GROSS_EUR"
echo "  💵 Net revenue this month:   €$NET_EUR"
echo ""

# Progress bars
MIN_PCT=$(echo "scale=0; $NET_CENTS * 100 / ($MIN_TARGET * 100)" | bc 2>/dev/null || echo 0)
GROWTH_PCT=$(echo "scale=0; $NET_CENTS * 100 / ($GROWTH_TARGET * 100)" | bc 2>/dev/null || echo 0)

echo "  Survival target (€$MIN_TARGET): $([ "$MIN_PCT" -ge 100 ] && echo "✅ REACHED" || echo "⏳ ${MIN_PCT}% — need €$(echo "scale=2; $MIN_TARGET - $NET_EUR" | bc) more")"
echo "  Growth target  (€$GROWTH_TARGET): $([ "$GROWTH_PCT" -ge 100 ] && echo "🚀 MACHINE UNLOCKED" || echo "📈 ${GROWTH_PCT}% — need €$(echo "scale=2; $GROWTH_TARGET - $NET_EUR" | bc) more")"
echo ""

# Subscriptions
echo "  Monthly costs:"
jq -r '.subscriptions | to_entries[] | "    \(.value.active | if . then "✅" else "❌" end) \(.key | gsub("_"; " ") | ascii_upcase): €\(.value.monthly_eur)"' "$LEDGER"
echo ""

# Status
if (( $(echo "$NET_EUR >= $GROWTH_TARGET" | bc -l) )); then
  echo "  🚀 STATUS: THRIVING — Machine upgrade unlocked!"
elif (( $(echo "$NET_EUR >= $MIN_TARGET" | bc -l) )); then
  echo "  ✅ STATUS: SURVIVING — All subscriptions covered"
else
  echo "  ⚠️  STATUS: AT RISK — Create more products NOW"
fi
