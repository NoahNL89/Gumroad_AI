# Project Plan - Sales Copy Optimization & Visual Asset Audit

## Objective
Autonomously rewrite and publish optimized sales copy directly to Gumroad for 27 existing products on `schephenk.gumroad.com` and audit existing cover assets in the `downloads/` directory, outputting a markdown report `cover_audit_report.md` at the workspace root.

## Key Constraints & Parameters
- **Integrity Mode**: demo (must verify that the auditor and tests run in demo mode safely)
- **Safe Execution**: DO NOT run social media promotions via `mastodon_bot.py` or `bluesky_bot.py`.
- **Global Path**: `/home/administrator/NewGitHub/GumRoad_AI`
- **Output Report**: `/home/administrator/NewGitHub/GumRoad_AI/cover_audit_report.md`
- **Agent Dir**: `/home/administrator/NewGitHub/GumRoad_AI/.agents/orchestrator`

## Phases & Milestones
1. **Milestone 1: Exploration & Verification**
   - Explore existing codebase, database schema, downloads folder, and API scripts.
   - Run initial environment validation scripts (load env, check auth, sync local DB).
   - Verify product counts, SQLite db schema, and available assets.

2. **Milestone 2: Copywriting Strategy & Verification (Dry Run)**
   - Analyze original copy of 27 products from `store.db` or API.
   - Design copywriting strategy (benefits, hook, formatting) optimized for AI/templates/digital products.
   - Generate optimized descriptions and save them to a local JSON/draft store without publishing yet (dry run).
   - Verify descriptions are significantly modified.

3. **Milestone 3: Gumroad Publishing Execution**
   - Write/run script to publish descriptions to Gumroad via API/CLI in demo mode.
   - Verify changes are reflected in database or API responses.

4. **Milestone 4: Cover Asset Quality Evaluation & Audit**
   - Verify presence of images in `downloads/` folder.
   - Evaluate visual/metadata quality of each cover asset (file size, presence, resolution/content indicators if programmatically readable, names, formats).
   - Generate `cover_audit_report.md` detailing which products need human replacement covers and reasons.

5. **Milestone 5: End-to-End Verification & Audit**
   - Run Forensic Integrity Audit.
   - Generate summary report.
   - Handoff results.
