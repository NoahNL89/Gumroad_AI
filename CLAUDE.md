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

**2. CLI compatibility scripts** (`scripts/api/`) — legacy bash entry points that delegate to the authenticated Gumroad CLI.
All source `scripts/api/_base.sh`, which provides the machine-safe `gumroad_cli` helper.

**3. SQLite DB layer** (`db/`) — local snapshot of store data for fast querying.  
- `db/sync.py` — fetches products (via CLI permalink discovery), sales, subscribers, payouts, and offer codes into `db/store.db`. Also supports `--products-only`, `--report-only`, `--reprice-zero <price>`.
- `db/query.py` — CLI query tool: `products`, `underpriced`, `sales`, `revenue`, `survival`, `snapshot`.  
- `db/store.db` — SQLite file (gitignored). Tables: `products`, `sales`, `subscribers`, `payouts`, `offer_codes`, `promotions`, `sync_log`.

**4. Social media bots** (`bot/`) — audience growth and product promotion.  
- `bot/mastodon_bot.py promote|engage|post "<text>"` — max 3 posts/day, logs to `promotions` table in DB.  
- `bot/bluesky_bot.py promote` — Bluesky promotion, also rate-limited.  
- `scripts/pinterest login|exchange|status|boards|draft|review|publish|standard-brief` — personal Pinterest CLI for OAuth plus manual review-and-publish product Pin workflow.
- `bot/update_profile.py` — updates Mastodon profile bio.  
Bots read credentials from `.env` (`MASTODON_ACCESS_TOKEN`, `MASTODON_INSTANCE`, `BLUESKY_USERNAME`, `BLUESKY_PASSWORD`, `PINTEREST_*`).

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
scripts/pinterest promote  # Draft a Pinterest product Pin for manual review
scripts/pinterest publish agent/pinterest_queue/<draft>.json  # Publish one approved draft

# CLI compatibility wrappers
source .env && ./scripts/api/list-products.sh
./scripts/api/create-product.sh "Name" 9.99 "Description"
./scripts/api/update-product.sh <id> --price 9.99
```

---

## Python Setup

```bash
pip3 install -r requirements.txt
# Packages: requests, Mastodon.py, atproto
```

## Testing

```bash
python3 tests/test_smoke.py        # no-dep smoke suite (builder, bot copy + rate limits, revenue math)
```

Run this after editing `bot/`, `db/query.py`, or `scripts/product_builder.py`. CI (`.github/workflows/ci.yml`) runs it on every push. New products use the data-driven engine — write a JSON spec and run `python3 scripts/product_builder.py <spec.json>` (see `--help`); do not author bespoke `gen_*.py` scripts (the existing ones are deprecated one-offs).

---

## Environment Variables

Credentials live in `.env` (gitignored). Copy `.env.example` to get started.

| Variable | Used by |
|---|---|
| Gumroad CLI auth | All Gumroad reads and writes; run `gumroad auth login` |
| `MASTODON_ACCESS_TOKEN` / `MASTODON_INSTANCE` | `bot/mastodon_bot.py` |
| `BLUESKY_USERNAME` / `BLUESKY_PASSWORD` | `bot/bluesky_bot.py` |
| `PINTEREST_APP_ID` / `PINTEREST_APP_SECRET` / `PINTEREST_ACCESS_TOKEN` / `PINTEREST_REFRESH_TOKEN` | `bot/pinterest_bot.py` |
| `AGENT_MONTHLY_TARGET_EUR` | `db/query.py` survival check (default: 58) |

Pinterest Trial-access apps must use the sandbox API for test Pin creation. Production Pin creation requires Pinterest Standard access and must go through the explicit draft review/approve flow.

---

## Agent Decision Loop

Each session, after startup checks:

1. **If behind revenue target** → create a new product or run a 50% launch discount
2. **If on target** → improve existing products, create a bundle, add variants
3. **If above target** → plan recurring memberships or high-ticket courses
4. After any store change: `python3 db/sync.py` to update the local DB

Store context: ~29 products (run `python3 db/query.py products` for the live count — do not trust this number, it drifts as products are added), focus on AI tools / templates / productivity, currency EUR, paid price range €5.99–€29.99 (one €0 subscription is exempt from repricing).

---

## After Each Session

```bash
# Update agent/ledger.json with actions taken, then:
git add agent/ledger.json
git commit -m "agent: <brief description>"
git push
```

Products are created as **drafts** — always run `gumroad products publish <id>` or they earn nothing.
