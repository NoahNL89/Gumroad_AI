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

Pinterest needs a public HTTPS URL for that CSV. The easiest self-hosted option
for this workspace is the Docker catalog server plus a Cloudflare Tunnel public
hostname.

Run locally:

```bash
source .env
python3 scripts/build_pinterest_catalog.py
docker compose -f compose.catalog.yml up -d --build
curl -u "$CATALOG_BASIC_USER:$CATALOG_BASIC_PASSWORD" \
  http://127.0.0.1:9000/pinterest_catalog.csv
```

Cloudflare Zero Trust setup:

1. Go to **Zero Trust -> Networks -> Tunnels**.
2. Use an existing tunnel on this machine, or create one.
3. Add a **Public Hostname**:
   - Subdomain: `catalog`
   - Domain: `schep.dev`
   - Service type: `HTTP`
   - URL: `localhost:9000`
4. Do not enable Cloudflare Access for this hostname unless Pinterest can pass
   that Access policy. Use the container Basic Auth credentials instead.

Final URL:

```text
https://catalog.schep.dev/pinterest_catalog.csv
```

In Pinterest, paste that URL into **Provide a URL link**, enter the feed username
and password from `CATALOG_BASIC_USER` / `CATALOG_BASIC_PASSWORD`, and choose the
6-hour ingestion schedule.

For the current Schep Digital store, use:

```text
https://catalog.schep.dev/pinterest_catalog.csv
```

To refresh the file manually:

```bash
scripts/update_pinterest_catalog.sh
```

The container bind-mounts `output/` read-only, so every regenerated
`output/pinterest_catalog.csv` is served on the next Pinterest fetch without a
container restart.

The compose service publishes port `9000` on all host interfaces, so local LAN
checks can use:

```text
http://192.168.1.11:9000/pinterest_catalog.csv
```

Cloudflare Tunnel can still point to `http://localhost:9000`.

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
