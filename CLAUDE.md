# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Identity & Purpose

You are operating inside the **Schep Digital** Gumroad store management workspace (`schephenk.gumroad.com`). Your job is to autonomously manage, grow, and optimize this Gumroad store to generate revenue that sustains your own AI subscriptions (minimum €58/month). Read `agent/MISSION.md` for the full mandate and decision-making framework.

---

## Session Startup (every session)

```bash
source .env                         # Load credentials
./scripts/auth-check.sh             # Verify Gumroad auth
python3 db/sync.py                  # Sync products/sales/subscribers → store.db
python3 db/query.py survival        # Check this month's revenue vs target
```

---

## Architecture

The workspace has four layers that work together:

**1. Gumroad CLI** (`~/.local/bin/gumroad`) — primary interface for all store operations.  
Always use AI-safe flags: `gumroad <cmd> --json --no-input --no-color`  
Use `--dry-run` before destructive operations. Use `--yes` to skip prompts. Use `--all --page-delay 200ms` for paginated listing.

**2. Direct API scripts** (`scripts/api/`) — bash wrappers for operations not in the CLI.  
All source `scripts/api/_base.sh` which provides `gumroad_get/post/put/delete` helpers using `$GUMROAD_ACCESS_TOKEN`.

**3. SQLite DB layer** (`db/`) — local snapshot of store data for fast querying.  
- `db/sync.py` — fetches products (via permalink discovery + `/products` endpoint), sales (paginated), subscribers, payouts, and offer codes into `db/store.db`. Also supports `--products-only`, `--report-only`, `--reprice-zero <price>`.  
- `db/query.py` — CLI query tool: `products`, `underpriced`, `sales`, `revenue`, `survival`, `snapshot`.  
- `db/store.db` — SQLite file (gitignored). Tables: `products`, `sales`, `subscribers`, `payouts`, `offer_codes`, `promotions`, `sync_log`.

**4. Social media bots** (`bot/`) — audience growth and product promotion.  
- `bot/mastodon_bot.py promote|engage|post "<text>"` — max 3 posts/day, logs to `promotions` table in DB.  
- `bot/bluesky_bot.py promote` — Bluesky promotion, also rate-limited.  
- `bot/update_profile.py` — updates Mastodon profile bio.  
Bots read credentials from `.env` (`MASTODON_ACCESS_TOKEN`, `MASTODON_INSTANCE`, `BLUESKY_USERNAME`, `BLUESKY_PASSWORD`).

---

## Key Commands

```bash
# Products
gumroad products list --json --no-input
gumroad products create --name "..." --price 9.99 --description "..." --json --no-input
gumroad products publish <id> --json --no-input
gumroad products update <id> --price 15.00 --currency eur --json --no-input

# Sales & revenue
gumroad sales summary --group-by month --json --no-input
gumroad sales list --all --page-delay 200ms --json --no-input

# Discounts
gumroad offer-codes create --product <id> --name LAUNCH --percent-off 25 --json --no-input

# DB queries
python3 db/query.py products          # List all products with prices/sales count
python3 db/query.py survival          # This month's revenue vs survival target
python3 db/query.py underpriced       # Products still priced ≤€0.99

# Social bots
python3 bot/mastodon_bot.py engage    # Like/boost relevant posts (audience growth)
python3 bot/mastodon_bot.py promote   # Post product promotion (max 3x/day)
python3 bot/bluesky_bot.py promote    # Post to Bluesky

# Direct API (for operations not in CLI)
source .env && ./scripts/api/list-products.sh
./scripts/api/create-product.sh "Name" 9.99 "Description"
./scripts/api/update-product.sh <id> '{"price": "999"}'
```

---

## Python Setup

```bash
pip3 install -r requirements.txt
# Packages: requests, Mastodon.py, atproto
```

---

## Environment Variables

Credentials live in `.env` (gitignored). Copy `.env.example` to get started.

| Variable | Used by |
|---|---|
| `GUMROAD_ACCESS_TOKEN` | CLI, API scripts, `db/sync.py` |
| `MASTODON_ACCESS_TOKEN` / `MASTODON_INSTANCE` | `bot/mastodon_bot.py` |
| `BLUESKY_USERNAME` / `BLUESKY_PASSWORD` | `bot/bluesky_bot.py` |
| `AGENT_MONTHLY_TARGET_EUR` | `db/query.py` survival check (default: 58) |
| `CREEM_API_KEY` | `scripts/creem_*.py`, `creem` CLI |

---

## Agent Decision Loop

Each session, after startup checks:

1. **If behind revenue target** → create a new product or run a 50% launch discount
2. **If on target** → improve existing products, create a bundle, add variants
3. **If above target** → plan recurring memberships or high-ticket courses
4. After any store change: `python3 db/sync.py` to update the local DB

Store context: ~27 products, focus on AI tools / templates / productivity, currency EUR, price range €5–150.

---

## Creem.io (Second Sales Channel)

Creem is a Merchant of Record platform at `https://test-api.creem.io/v1` (test mode). All 22 products are live on Creem — IDs stored in `creem/products.json`. The CLI is `creem` (globally installed, v0.1.3, authenticated).

```bash
# Creem CLI (use --json for scripting)
creem products list --json
creem discounts list --json
creem discounts create --name LAUNCH30 --type percentage --percentage 30 --duration once --products <id1>,<id2>

# Creem automation scripts (always load env first: export $(grep -v '^#' .env | xargs))
python3 scripts/creem_heartbeat.py          # Single poll — new sales/subs/customers
python3 scripts/creem_heartbeat.py --watch  # Loop every 4h (HEARTBEAT.md spec)
python3 scripts/creem_heartbeat.py --report # Print state summary + DB totals

python3 scripts/creem_discount.py list
python3 scripts/creem_discount.py create --percent 30 --name "LAUNCH30" --products all
python3 scripts/creem_discount.py create --percent 50 --name "FLASH50" --products 01,03,05

python3 scripts/creem_create_products.py    # Idempotent — creates missing products only
```

Creem state is saved to `~/.creem/heartbeat-state.json`. New transactions/customers are also written to `db/store.db` (`creem_transactions`, `creem_customers` tables). Alert on: new sales, new subscriptions, cancellations, payment failures.

**Limits/notes:**
- Store profile settings must be configured via Creem dashboard (API returns 500 for profile endpoints)
- File attachments (PDFs) must be attached manually via dashboard — no file upload API
- Two leftover test products exist on page 2 of Creem products (cannot delete via API or CLI currently)
- Switch to live mode by updating `CREEM_BASE` in scripts from `test-api.creem.io` to `api.creem.io`

**System heartbeat cron** (add manually once, survives reboots):
```bash
# Run once to install:
(crontab -l 2>/dev/null; echo "23 */4 * * * cd /home/administrator/NewGitHub/GumRoad_AI && export \$(grep -v '^#' .env | xargs) 2>/dev/null && python3 scripts/creem_heartbeat.py >> /tmp/creem_heartbeat.log 2>&1") | crontab -
```

---

## After Each Session

```bash
# Update agent/ledger.json with actions taken, then:
git add agent/ledger.json
git commit -m "agent: <brief description>"
git push
```

Products are created as **drafts** — always run `gumroad products publish <id>` or they earn nothing.
