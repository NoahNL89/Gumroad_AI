# 🛍️ GumRoad AI Workspace

> A fully configured, AI-agent-ready workspace for the [Gumroad CLI](https://github.com/antiwork/gumroad-cli) — manage your Gumroad store from the terminal with powerful scripting, automation, and AI integration.

---

## ⚡ Quick Setup

### 1. Authenticate

```bash
# Interactive (opens browser for device approval)
gumroad auth login

# CI / Agents: set env var (no login needed)
export GUMROAD_ACCESS_TOKEN=your-token

# Pipe a token in directly
echo "your-token" | gumroad auth login --with-token
```

### 2. Verify auth

```bash
gumroad auth status --json --no-input
gumroad user --json --no-input
```

### 3. Explore

```bash
gumroad products list
gumroad sales list --json --jq '.sales[0]'
gumroad sales summary --group-by month
```

---

## 📦 Installation

The CLI is already installed at `~/.local/bin/gumroad` (v0.8.1+).

To update to the latest version:
```bash
curl -fsSL https://gumroad.com/install-cli.sh | bash
# or via Go
go install github.com/antiwork/gumroad-cli/cmd/gumroad@latest
```

---

## 🔐 Environment Variables

| Variable | Purpose |
|---|---|
| `GUMROAD_ACCESS_TOKEN` | Seller API token (preferred for CI/agents) |
| `GUMROAD_ADMIN_TOKEN` | Admin API token (for `gumroad admin` commands) |
| `GUMROAD_ADMIN_API_BASE_URL` | Override admin API base URL (local testing) |

Store your token in `.env` (already gitignored):

```bash
cp .env.example .env
# Edit .env and set GUMROAD_ACCESS_TOKEN=your-token
source .env
```

Get your token at: https://app.gumroad.com/settings/advanced → Generate Access Token

---

## 🗂️ Command Reference

### 🔑 Authentication
```bash
gumroad auth login              # Device authorization (default)
gumroad auth login --web        # Local browser OAuth (PKCE)
gumroad auth login --with-token # Pipe token from stdin
gumroad auth status             # Check current auth state
gumroad auth token              # Print active token
gumroad auth logout             # Revoke stored tokens
```

### 👤 Account
```bash
gumroad user --json --no-input
gumroad refund-policy view --json --no-input
gumroad refund-policy set --period 30 --fine-print "Reviewed in 2 business days."
```

### 📦 Products
```bash
gumroad products list --json --no-input
gumroad products view <id> --json --no-input
gumroad products create --name "My Product" --price 9.99 --json --no-input
gumroad products create --name "Course" --type course --price 49.99 --json --no-input
gumroad products create --name "Newsletter" --type membership --subscription-duration monthly --json --no-input
gumroad products update <id> --name "New Name" --json --no-input
gumroad products update <id> --price 15.00 --currency eur --json --no-input
gumroad products update <id> --file ./pack.zip --json --no-input
gumroad products publish <id> --json --no-input
gumroad products unpublish <id> --json --no-input
gumroad products delete <id> --yes --json --no-input
gumroad products skus <id> --json --no-input
```

**Product types:** `digital` | `course` | `ebook` | `membership` | `bundle` | `coffee` | `call` | `commission`

> ⚠️ Products are created as **drafts** — use `gumroad products publish <id>` to make them live.

### 📁 Files
```bash
gumroad files upload ./product.zip --json --no-input
gumroad files upload ./product.zip --name "My File.zip" --json --no-input
# Recover a failed upload
gumroad files complete --recovery recovery.json --yes --json --no-input
# Abort an orphaned multipart upload
gumroad files abort --upload-id <id> --key <s3-key> --yes --json --no-input
```

### 💰 Sales
```bash
gumroad sales list --json --no-input
gumroad sales list --product <id> --after 2024-01-01 --json --no-input
gumroad sales list --email user@example.com --json --no-input
gumroad sales list --all --page-delay 200ms --json --no-input
gumroad sales view <id> --json --no-input
gumroad sales refund <id> --yes --json --no-input
gumroad sales refund <id> --amount 5.00 --dry-run --json --no-input
gumroad sales resend-receipt <id> --json --no-input
gumroad sales ship <id> --json --no-input
gumroad sales summary --group-by month --from 2026-01-01 --json --no-input
```

### 💳 Payouts
```bash
gumroad payouts list --json --no-input
gumroad payouts list --all --page-delay 200ms --json --no-input
gumroad payouts view <id> --json --no-input
gumroad payouts view <id> --include-transactions --json --no-input
gumroad payouts upcoming --json --no-input
```

### 👥 Subscribers
```bash
gumroad subscribers list --product <id> --json --no-input
gumroad subscribers list --product <id> --all --json --no-input
gumroad subscribers view <id> --json --no-input
```

### 🔑 Licenses
> **Always pass license keys via stdin — never as CLI arguments.**

```bash
echo "$LICENSE_KEY" | gumroad licenses verify --product <id> --no-increment --json --no-input
echo "$LICENSE_KEY" | gumroad licenses verify --product <id> --json --no-input
echo "$LICENSE_KEY" | gumroad licenses enable --product <id> --json --no-input
echo "$LICENSE_KEY" | gumroad licenses disable --product <id> --json --no-input
echo "$LICENSE_KEY" | gumroad licenses decrement --product <id> --json --no-input
echo "$LICENSE_KEY" | gumroad licenses rotate --product <id> --json --no-input
```

### 🏷️ Offer Codes (Discounts)
```bash
gumroad offer-codes list --product <id> --json --no-input
gumroad offer-codes create --product <id> --name SAVE10 --percent-off 10 --json --no-input
gumroad offer-codes create --product <id> --name FLAT5 --amount 5.00 --json --no-input
gumroad offer-codes view <code_id> --product <id> --json --no-input
gumroad offer-codes update <code_id> --product <id> --max-purchase-count 100 --json --no-input
gumroad offer-codes delete <code_id> --product <id> --yes --json --no-input
```

**Create flags:** `--name` (required), `--percent-off` OR `--amount`, `--max-purchase-count`, `--universal`

### 🎛️ Variants & Categories
```bash
gumroad variant-categories list --product <id> --json --no-input
gumroad variant-categories create --product <id> --title "Size" --json --no-input
gumroad variant-categories view <cat_id> --product <id> --json --no-input
gumroad variant-categories update <cat_id> --product <id> --title "Color" --json --no-input
gumroad variant-categories delete <cat_id> --product <id> --yes --json --no-input

gumroad variants list --product <id> --category <cat_id> --json --no-input
gumroad variants create --product <id> --category <cat_id> --name "Large" --json --no-input
gumroad variants create --product <id> --category <cat_id> --name "XL" --price-difference 5.00 --json --no-input
gumroad variants update <var_id> --product <id> --category <cat_id> --name "Medium" --json --no-input
gumroad variants delete <var_id> --product <id> --category <cat_id> --yes --json --no-input
```

### 📝 Custom Fields
```bash
gumroad custom-fields list --product <id> --json --no-input
gumroad custom-fields create --product <id> --name "Company" --required --json --no-input
gumroad custom-fields update --product <id> --name "Company" --required --json --no-input
gumroad custom-fields delete --product <id> --name "Company" --yes --json --no-input
```

### 🪝 Webhooks
```bash
gumroad webhooks list --resource sale --json --no-input
gumroad webhooks create --resource sale --url https://example.com/hook --json --no-input
gumroad webhooks delete <id> --yes --json --no-input
```

---

## 🎛️ Global Flags

| Flag | Description |
|---|---|
| `--json` | Output as JSON |
| `--jq <expr>` | Filter JSON with a jq expression |
| `--plain` | Tab-separated output (pipe to `awk`, `cut`) |
| `--no-input` | Disable interactive prompts (AI/CI safe) |
| `--non-interactive` | Explicit CI/agent mode |
| `--yes` | Skip all confirmation prompts |
| `--dry-run` | Preview mutating requests without executing |
| `--quiet` / `-q` | Suppress spinners and status messages |
| `--all` | Fetch all pages (paginated commands) |
| `--page-delay 200ms` | Slow down pagination to avoid rate limits |
| `--debug` | Enable debug logging to stderr |

---

## 🤖 AI Agent Mode

This CLI is designed for AI agents:
- Use `--json --no-input --non-interactive` for all commands
- Set `GUMROAD_ACCESS_TOKEN` env var — no interactive login needed
- Use `--jq` to extract exactly the fields you need
- Use `--dry-run` to preview destructive operations first
- Use `--yes` to skip confirmation prompts
- Use `--page-delay 200ms` with `--all` to avoid rate limits

The embedded agent skill file is at `skills/gumroad/SKILL.md`.

Install the skill for your AI tool:
```bash
gumroad skill  # interactive installer
```

---

## 📁 Workspace Structure

```
GumRoad_AI/
├── README.md                  # Full command reference (this file)
├── AGENTS.md                  # AI agent configuration (Antigravity/Codex)
├── CLAUDE.md                  # AI agent configuration (Claude Code)
├── PROJECT.md                 # Project overview and goals
├── SchepDigital-Privacy-Policy.md  # Privacy policy (Pinterest API)
├── .env.example               # Environment variable template
├── .env                       # Your secrets (gitignored)
├── .gitignore                 # Ignores secrets, DB, and build artifacts
├── requirements.txt           # Python dependencies
├── agent/
│   ├── MISSION.md             # AI agent mandate and survival targets
│   ├── ledger.json            # Session log of all agent actions
│   ├── ledger.sh              # Quick ledger viewer
│   └── reports/               # Archived audit reports
├── bot/
│   ├── bluesky_bot.py         # Bluesky promotion + posting bot
│   ├── mastodon_bot.py        # Mastodon promotion, posting + engagement bot
│   └── update_profile.py      # Mastodon profile updater
├── db/
│   ├── sync.py                # Gumroad → SQLite sync (products, sales, subs)
│   ├── query.py               # CLI for querying store data + survival status
│   └── store.db               # SQLite database (gitignored, generated)
├── scripts/
│   ├── auth-check.sh          # Quick auth status check
│   ├── oauth-exchange.sh      # OAuth code → token exchange
│   ├── download_files.py      # Download product cover assets
│   ├── upload_cover.py        # Upload cover images via API
│   ├── upload_thumbnails.py   # Batch upload thumbnails via GitHub URLs
│   └── api/                   # Direct Gumroad API wrappers (16 scripts)
│       ├── _base.sh           # Shared helpers (gumroad_get/post/put/delete)
│       ├── get-user.sh        # GET /v2/user
│       ├── list-products.sh   # GET /v2/products
│       ├── list-sales.sh      # GET /v2/sales
│       └── ...                # create-product, update-product, etc.
├── assets/
│   └── thumbnails/            # AI-generated product thumbnails
├── skills/
│   └── gumroad/
│       └── SKILL.md           # AI agent skill definition
└── examples/
    ├── jq-recipes.md          # Useful jq filter recipes
    └── automation.md          # Common automation patterns
```

---

## 🔗 Resources

- [Gumroad CLI GitHub](https://github.com/antiwork/gumroad-cli)
- [Gumroad API Docs](https://app.gumroad.com/api)
- [Gumroad Token Generator](https://app.gumroad.com/settings/advanced)
- [jq Manual](https://jqlang.org/manual/) — For `--jq` expressions
