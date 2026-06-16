# jq Recipes for Gumroad CLI

Common `--jq` filters for extracting and transforming Gumroad data.

---

## Products

```bash
# List product names and IDs
gumroad products list --json --no-input --jq '[.products[] | {id, name, price: .formatted_price}]'

# Get a product's file list
gumroad products view <id> --json --no-input --jq '.product.files'

# List only published products
gumroad products list --json --no-input --jq '[.products[] | select(.published == true)]'

# List products sorted by price
gumroad products list --json --no-input | jq '[.products[] | {id, name, cents: .price_cents}] | sort_by(.cents)'
```

---

## Sales

```bash
# Get emails of recent buyers
gumroad sales list --json --no-input --jq '[.sales[].email]'

# Find a sale by email
gumroad sales list --json --no-input --jq '.sales[] | select(.email == "buyer@example.com")'

# Calculate total revenue from a batch
gumroad sales list --all --json --no-input | jq '[.sales[].price_cents] | add / 100'

# List sales with product name and date
gumroad sales list --json --no-input --jq '[.sales[] | {email, product_name, price: .formatted_display_price, date: .created_at}]'

# Count sales per product
gumroad sales list --all --json --no-input | jq '
  [.sales[] | .product_name] | 
  group_by(.) | 
  map({product: .[0], count: length}) | 
  sort_by(.count) | reverse'

# Get refunded sales only
gumroad sales list --all --json --no-input --jq '[.sales[] | select(.refunded == true)]'
```

---

## Payouts

```bash
# Total paid out (all time)
gumroad payouts list --all --json --no-input | jq '[.payouts[].amount_cents] | add / 100'

# Most recent payout amount
gumroad payouts list --json --no-input --jq '.payouts[0] | {date: .date, amount: .amount_formatted}'

# List payouts with cents
gumroad payouts list --json --no-input --jq '[.payouts[] | {id, date, amount_cents, status: .state}]'
```

---

## Subscribers

```bash
# Get subscriber emails for a product
gumroad subscribers list --product <id> --all --json --no-input --jq '[.subscribers[].email]'

# Count active subscribers
gumroad subscribers list --product <id> --all --json --no-input --jq '[.subscribers[] | select(.status == "active")] | length'

# Subscriber join dates
gumroad subscribers list --product <id> --json --no-input --jq '[.subscribers[] | {email, created_at}]'
```

---

## Offer Codes

```bash
# List codes with discount amount
gumroad offer-codes list --product <id> --json --no-input --jq '[.offer_codes[] | {name, percent_off, amount_cents, uses: .times_used}]'

# Find unused codes
gumroad offer-codes list --product <id> --json --no-input --jq '[.offer_codes[] | select(.times_used == 0) | .name]'
```

---

## Licenses

```bash
# Verify and extract purchase info
echo "$KEY" | gumroad licenses verify --product <id> --no-increment --json --no-input \
  --jq '{email: .purchase.email, uses: .purchase.uses, active: (.purchase.refunded | not)}'
```

---

## Tips

- Chain `--jq` filters with `|` for multi-step transformations
- Use `select()` to filter arrays
- Use `@csv` to export as CSV: `[.sales[] | [.email, .product_name]] | .[] | @csv`
- Use `length` to count results
- Use `sort_by(.field)` and `reverse` to sort
- Use `group_by(.field)` + `map()` for aggregation
