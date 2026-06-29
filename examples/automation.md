# Gumroad CLI Automation Patterns

Common automation and scripting patterns using the Gumroad CLI.

---

## CI/CD Integration

### Environment Setup
```bash
# Always set this in your CI environment
export GUMROAD_ACCESS_TOKEN="${{ secrets.GUMROAD_ACCESS_TOKEN }}"

# Validate token before running jobs
gumroad auth status --json --no-input --quiet
```

### Flag Checklist for CI/Agents
Every command in CI/agent contexts should use:
```bash
gumroad <command> \
  --json \           # Machine-readable output
  --no-input \       # Never block on prompts
  --non-interactive \ # Explicit agent mode
  --quiet            # Suppress spinners
```

Add `--yes` for commands that normally prompt for confirmation.
Add `--dry-run` to preview destructive commands first.

---

## Product Lifecycle

### Create, configure, and publish a product
```bash
# 1. Create as draft
PRODUCT_ID=$(gumroad products create \
  --name "My Course" \
  --price 49.99 \
  --type course \
  --description "Learn everything." \
  --json --no-input | jq -r '.id')

# 2. Upload content file
gumroad files upload ./course-content.zip --json --no-input

# 3. Create a discount for early access
gumroad offer-codes create \
  --product "$PRODUCT_ID" \
  --name EARLYBIRD \
  --percent-off 30 \
  --max-purchase-count 50 \
  --json --no-input

# 4. Publish
gumroad products publish "$PRODUCT_ID" --json --no-input

echo "Published: https://gumroad.com/l/$PRODUCT_ID"
```

### Bulk update prices (10% increase)
```bash
gumroad products list --json --no-input | jq -r '.products[] | "\(.id) \(.price_cents)"' | \
while read -r id cents; do
  new_price=$(echo "scale=2; $cents * 1.10 / 100" | bc)
  echo "Updating $id to \$$new_price..."
  gumroad products update "$id" --price "$new_price" --json --no-input --quiet
done
```

---

## Sales Management

### Daily sales digest
```bash
#!/usr/bin/env bash
# Run via cron: 0 9 * * * /path/to/daily-digest.sh

TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)

echo "=== Sales: $YESTERDAY ==="

gumroad sales list \
  --after "$YESTERDAY" \
  --before "$TODAY" \
  --all \
  --json --no-input | jq '{
    total_sales: (.sales | length),
    revenue: ([.sales[].price_cents] | add // 0 | . / 100),
    products: ([.sales[].product_name] | unique)
  }'
```

### Refund all sales for a specific buyer
```bash
BUYER_EMAIL="refund-me@example.com"

gumroad sales list \
  --email "$BUYER_EMAIL" \
  --all \
  --json --no-input | jq -r '.sales[] | select(.refunded == false) | .id' | \
while read -r sale_id; do
  echo "Refunding $sale_id..."
  gumroad sales refund "$sale_id" --yes --json --no-input --quiet
done
```

---

## Webhook Management

### Reset all sale webhooks
```bash
NEW_URL="https://your-server.com/webhooks/gumroad"

# Delete existing
gumroad webhooks list --resource sale --json --no-input | \
  jq -r '.resource_subscriptions[].id' | \
while read -r id; do
  gumroad webhooks delete "$id" --yes --json --no-input --quiet
done

# Create new
gumroad webhooks create \
  --resource sale \
  --url "$NEW_URL" \
  --json --no-input
```

---

## License Verification Service

### Batch verify licenses from a file
```bash
#!/usr/bin/env bash
# verify-licenses.sh <product_id> <keys_file>
# keys_file: one license key per line

PRODUCT_ID="${1:?Need product ID}"
KEYS_FILE="${2:?Need keys file}"

while IFS= read -r key; do
  RESULT=$(echo "$key" | gumroad licenses verify \
    --product "$PRODUCT_ID" \
    --no-increment \
    --json --no-input 2>&1)

  if echo "$RESULT" | jq -e '.success' > /dev/null 2>&1; then
    EMAIL=$(echo "$RESULT" | jq -r '.purchase.email')
    echo "✅ $key → $EMAIL"
  else
    echo "❌ $key → INVALID"
  fi
done < "$KEYS_FILE"
```

---

## Data Export

### Export all data to JSON files
```bash
#!/usr/bin/env bash
OUTPUT_DIR="./gumroad-export-$(date +%Y%m%d)"
mkdir -p "$OUTPUT_DIR"

echo "Exporting products..."
gumroad products list --all --json --no-input > "$OUTPUT_DIR/products.json"

echo "Exporting sales..."
gumroad sales list --all --page-delay 200ms --json --no-input > "$OUTPUT_DIR/sales.json"

echo "Exporting payouts..."
gumroad payouts list --all --json --no-input > "$OUTPUT_DIR/payouts.json"

echo "Done! Data in $OUTPUT_DIR/"
ls -lh "$OUTPUT_DIR/"
```

---

## Error Handling

### Check auth before running
```bash
#!/usr/bin/env bash
set -euo pipefail

# Fail fast if not authenticated
if ! gumroad auth status --json --no-input 2>/dev/null | jq -e '.seller' > /dev/null 2>&1; then
  echo "Error: Not authenticated. Run 'gumroad auth login' or configure the CLI token in CI."
  exit 1
fi

# Your automation here...
```

### Handle rate limits
```bash
# Use --page-delay for large paginated fetches
gumroad sales list --all --page-delay 500ms --json --no-input

# Or add manual delays in loops
for id in $PRODUCT_IDS; do
  gumroad products view "$id" --json --no-input
  sleep 0.3
done
```
