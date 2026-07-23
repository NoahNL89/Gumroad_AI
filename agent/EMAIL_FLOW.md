# Lifecycle Flow — free download to paid customer

The current customer path is:

`Free Private AI Readiness Kit → Private AI on Your Computer (€7) → Complete Toolkit (€24)`

## Stage 0: current account, before Gumroad's email gate

Gumroad Emails and automated Workflows are unavailable until the account has earned
at least $100 after fees and received a payout. Until that condition is verified,
do not claim that a sequence was scheduled or sent and do not export buyers into an
unapproved bulk-mail system.

Use the conversion surfaces that are available now:

1. The free product receipt delivers the promised asset and offers one relevant
   next step: the €7 Private AI guide.
2. The free-product upsell offers that same guide. Keep message-match tight; do not
   send a local-AI lead to a generic prompt-vault pitch.
3. The paid guide's content page tells the buyer where to start, gives support
   contact details, and asks for an honest review when Gumroad prompts them.
4. The paid-guide upsell replaces the guide with the complete toolkit at a 20%
   upgrade discount, avoiding a duplicate charge for the guide.
5. Gumroad automatically requests a rating after purchase; never ask for a positive
   rating or offer compensation for one.

Measure free downloads, paid-guide sales, toolkit sales, and revenue with
`python3 scripts/campaign_report.py`. Page views and UTM breakdowns must be read in
Gumroad Analytics and recorded in `agent/growth_experiments.json`.

## Stage 1: after $100 and a payout are verified

Create one Gumroad Workflow for free-pack customers, then test it with an internal
address before activation:

- Immediately — delivery/orientation: one concrete way to use the free pack today.
- Day 2 — pure value: a worked local-AI privacy or model-choice lesson, no pitch.
- Day 4 — relevant bridge: explain who benefits from running AI locally and link to
  the €7 guide with the normal offer.
- Day 7 — objection handling: hardware, privacy, and setup expectations; no invented
  scarcity. Mention a discount only when its end date is truly configured.

After the sequence, send at most one useful update per week. Honor unsubscribes,
never buy lists, and do not email people who did not consent.

## Promotion rules

- One primary click per message.
- Specific teaching before a product mention.
- No evergreen “ends tonight” language.
- No claims of total privacy, zero compliance risk, guaranteed income, or model
  performance without observed evidence.
- Compare opens/clicks only after the workflow is actually unlocked and active.
