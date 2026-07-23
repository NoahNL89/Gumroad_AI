# Schep Digital — Autonomous Revenue Session (GO)

You are running one unattended, idempotent revenue session for Schep Digital.
Work in `/home/administrator/NewGitHub/GumRoad_AI`. Read `AGENTS.md`,
`agent/MISSION.md`, and `agent/growth_experiments.json` before changing anything.
Do not ask for input. Do not call Gumroad endpoints directly; use the authenticated
`gumroad` CLI with `--json --no-input --no-color`.

The store already has enough products. The default job is to learn which message
and channel can acquire a buyer, not to add another SKU or blanket discount.

## 1. Verify and measure

```bash
source .env
./scripts/auth-check.sh
python3 db/sync.py
python3 db/query.py survival
python3 db/query.py funnel
python3 scripts/audience_metrics.py --json
python3 scripts/campaign_report.py --json
```

If auth or sync fails, record the exact error and continue with safe local analysis.
Never interpret missing data as zero.

## 2. Respect the active experiment

Read the active experiment dates, hypothesis, product IDs, and guardrails in
`agent/growth_experiments.json`.

- Before `evaluate_on`, keep the offer, core price, and focus product stable.
- Fix a delivery error, broken link, or false claim immediately; these are not
  experiment changes.
- Do not publish draft products. Several drafts are intentional duplicate cleanup.
- Do not create a product, regenerate a launch kit, create another discount family,
  or re-run the lead-magnet creation script during an active experiment.
- Do not claim a deadline unless the offer has a real configured end time.

## 3. Distribute without spamming

Check promotion history for the focused product in the last rolling 24 hours. If
there is no focused campaign post on a channel, post one value-first variant:

```bash
python3 bot/mastodon_bot.py promote
python3 bot/bluesky_bot.py promote
```

Do not automate likes, follows, boosts, reposts, replies, or direct messages.
Bluesky explicitly treats unsolicited automated interactions as spam. Grow through
useful posts on the store's own accounts and opt-in replies only.

Pinterest is a manual review channel. `promote` creates a draft only when no recent
draft is already awaiting approval:

```bash
python3 bot/pinterest_bot.py promote
python3 bot/pinterest_bot.py pending
```

Never auto-publish a Pinterest draft. Never post into third-party communities or
send affiliate outreach without a concrete, reviewed message and compliance with
that community's rules.

## 4. Maintain the live funnel

The intended path is:

`free Private AI readiness kit → €7 Private AI guide → €24 toolkit`

Verify that all three products are published, the paid guide has its current buyer
file, and both relevant upsells remain active. Repair only a verified defect. The
pre-$100 lifecycle is receipt copy, content-page guidance, Gumroad's review prompt,
and upsells. Gumroad Emails/Workflows are not available until the account passes
its revenue/payout gate, so do not pretend a nurture workflow was sent.

## 5. Evaluate only on the experiment date

Before `evaluate_on`, report movement and keep collecting data. On or after that
date:

1. Sync and run `scripts/campaign_report.py`.
2. If Gumroad Analytics UTM page views are already available, record them. They are
   optional because the CLI does not expose page views; never delay evaluation or
   ask the user to run GO manually because they are absent.
3. Diagnose the narrowest constraint:
   - no impressions/follower growth: message/channel distribution problem;
   - impressions but no clicks: hook or audience mismatch;
   - clicks but no free downloads: landing-page trust/relevance problem;
   - leads but no €7 sales: bridge/offer problem;
   - core sales but no toolkit upgrades: upsell/value ladder problem.
4. Change one major variable for the next seven-day experiment and record the
   decision. Do not change price, page, product, and channel simultaneously.

The daily runner appends a machine-generated date gate to this prompt and runs
`scripts/evaluate_experiment.py` as a deterministic fallback. When the active
experiment is already `evaluated`, archive it under `history`, create the next
seven-day experiment from its `decision.next_action`, and keep only one major
variable under test.

Create a new product only when traffic and customer evidence reveal a distinct
unmet need that the current catalog cannot satisfy.

## 6. Close cleanly

Run tests relevant to any change. Append an evidence-based session to
`agent/ledger.json`, including actions, posts, current revenue, experiment status,
and failures. Rebuild `catalog/pinterest_catalog.csv`; if the product data changed,
include the updated public feed in the commit. Commit and push only the workspace
changes from this session. The runner sends a Pushover summary only when the run
produced a commit or measurable sales movement.
