# Pinterest Retail Catalog Setup

## Current public feed URL

Use this URL in Pinterest's **Catalogs → Data sources → Add data source → URL**:

```text
https://raw.githubusercontent.com/NoahNL89/GumRoad_AI/main/catalog/pinterest_catalog.csv
```

The feed is now committed in the repository, so it has a stable, public HTTPS URL
without a paid server, Docker container, Cloudflare Tunnel, or Basic Auth.

## Refresh workflow

```bash
source .env
scripts/update_pinterest_catalog.sh
git add catalog/pinterest_catalog.csv
git commit -m "agent: refresh Pinterest catalog"
git push
```

The normal GO workflow commits meaningful repository changes, so catalog changes
become visible at the same raw GitHub URL after the push. Pinterest can fetch it on
its configured schedule.

The feed generator reads `PINTEREST_CLAIMED_STORE_URL=https://store.schep.dev` and
uses that claimed Gumroad custom domain for each product destination. It excludes
free products and subscriptions, and includes Pinterest's required retail fields.

## Pinterest UI change

Replacing the URL in this repository does not modify an existing Pinterest data
source. In Pinterest, replace any old `catalog.schep.dev` or `store.schep.dev`
catalog-file URL with the raw GitHub URL above. No username or password is required.

## Legacy local server

`compose.catalog.yml` remains available for local feed validation, now serving the
same tracked `catalog/pinterest_catalog.csv` file at:

```text
http://127.0.0.1:9000/pinterest_catalog.csv
```

It is not the production feed source.
