# Project: GumRoad_AI Optimization

## Architecture
- SQLite database `store.db` serves as the local source of truth for Gumroad products.
- Scripts in `scripts/` folder provide wrappers for direct API calls to Gumroad.
- The `gumroad` CLI tool (`~/.local/bin/gumroad`) is available for store actions.
- Local `downloads/` directory contains downloaded cover image assets for each product.
- Cover assets audit outputs to `cover_audit_report.md` in the workspace root.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Exploration & Verification | Sync database, verify connection, locate download assets | None | DONE |
| 2 | Strategy & Copy Optimization | Design copy structure, generate optimized descriptions in dry-run | M1 | DONE |
| 3 | Gumroad Publishing Execution | Programmatically update product descriptions using API/CLI (dry-run/real depending on demo mode) | M2 | DONE |
| 4 | Cover Asset Quality Audit | Evaluate downloaded covers in `downloads/`, generate audit report | M1 | DONE |
| 5 | End-to-End Verification & Audit | Validate all updates, run final integrity audit checks, compile summary | M3, M4 | DONE |

## Interface Contracts
- API Scripts/CLI require valid GUMROAD_ACCESS_TOKEN.
- Database: sqlite3 database at `store.db` contains table `products` with columns `id`, `name`, `description`, etc.
- Output report format: Markdown file `cover_audit_report.md` with structured tables listing cover replacement recommendations.
