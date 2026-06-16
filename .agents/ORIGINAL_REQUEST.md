# Original User Request

## Initial Request — 2026-06-16T11:36:23Z

An autonomous AI team will review the portfolio of 27 existing Gumroad products on the `schephenk.gumroad.com` store. The team will autonomously rewrite and publish optimized sales copy directly to Gumroad and evaluate existing cover assets, flagging any that require human replacement.

Working directory: /home/administrator/NewGitHub/GumRoad_AI
Integrity mode: demo

## Requirements

### R1. Sales Copy Overhaul
The team must review the existing product descriptions (using the local SQLite database or the Gumroad API) and apply conversion-focused copywriting best practices. The new, optimized descriptions must be published directly back to the Gumroad store via the API. 

### R2. Visual Asset Audit
The team must evaluate the visual quality of the downloaded product covers in the `downloads/` directory. Instead of autonomously generating new covers, the team must compile a markdown report detailing which specific products require new human-made cover designs and briefly explain why.

### R3. Safe Execution Scope
The team is permitted to run Python API scripts to update products, but must NOT trigger the social media bots (`mastodon_bot.py` or `bluesky_bot.py`) to broadcast promotions for the updated products during this phase.

## Acceptance Criteria

### Sales Copy Update Verification
- [ ] Programmatic check: Querying `store.db` or the Gumroad API confirms that the `description` fields for the targeted products have been significantly modified compared to their original state.
- [ ] A summary list is provided detailing which products received description updates.

### Visual Audit Report
- [ ] A file named `cover_audit_report.md` exists in the workspace.
- [ ] The report clearly lists products that need cover replacements along with the specific reasons (e.g., "resolution too low", "generic text").
