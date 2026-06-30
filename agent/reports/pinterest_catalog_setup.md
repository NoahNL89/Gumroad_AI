# Pinterest Retail Catalog Setup

## Recommended Option

Use **Add a retail catalog data source -> Provide a URL link**.

The workspace can generate the feed file:

```bash
python3 db/sync.py
PINTEREST_CLAIMED_STORE_URL=https://store.schep.dev \
  python3 scripts/build_pinterest_catalog.py
```

Output:

```text
output/pinterest_catalog.csv
```

## Feed Hosting

Pinterest needs a public HTTPS URL for that CSV. Good options:

- Cloudflare Pages static file
- Cloudflare R2 public object
- Any public HTTPS host under the claimed domain

Example final URL:

```text
https://store.schep.dev/pinterest_catalog.csv
```

In Pinterest, paste that URL into **Provide a URL link** and choose daily ingestion.

For the current Schep Digital store, use:

```text
https://store.schep.dev/pinterest_catalog.csv
```

## Product Link Requirement

Product `link` values should use the claimed domain, not the raw Gumroad subdomain:

```text
https://store.schep.dev/l/product-slug
```

Set `PINTEREST_CLAIMED_STORE_URL` in `.env` so the generator rewrites Gumroad links automatically.

## Included Fields

The generated CSV includes:

- `id`
- `title`
- `description`
- `link`
- `image_link`
- `price`
- `availability`
- `brand`
- `condition`
- `product_type`
- `google_product_category`
- `custom_label_0`

The generator skips free products and monthly subscription products because Pinterest retail feeds expect concrete product prices, not zero-price lead magnets or subscription cadence text.
