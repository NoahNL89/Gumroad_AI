# Email Flow — turn free downloads into paying customers

The email list is the only asset that compounds. Every other channel (social, SEO,
Reddit) is rented; the list is owned. This is how we build and use it.

## How capture works on Gumroad

1. The **free lead magnet** ("The AI Quick-Start Pack (Free)") is published via
   `bash scripts/create_lead_magnet.sh`. Anyone who "buys" it at €0 gives us their email.
2. Gumroad stores those emails as **customers / followers**. Export anytime:
   ```bash
   ./scripts/export-buyers.sh        # CSV of buyer emails
   ```
3. Email them from **Gumroad → Audience → Email** (free, no extra tool), or export
   and send via any provider.

## The nurture sequence (send to anyone who grabs the free pack)

Keep it short and useful. The goal of each email is one click, not a hard sell.

**Email 1 — Deliver + set expectations (immediately / Gumroad receipt)**
Subject: Your AI Quick-Start Pack is inside
Body: Here's your pack. Start with prompt #1 on a real task today — it pays off in
about 10 minutes. I'll send two more short notes this week with the prompts I use
most. Reply any time; I read everything.

**Email 2 — Pure value, no pitch (day 2)**
Subject: the prompt I use more than any other
Body: One prompt, fully worked, with a before/after. No link to buy. This builds
trust and open rates for email 3.

**Email 3 — Soft bridge to paid (day 4)**
Subject: want the other 200?
Body: If the free 12 helped, the full library ("The AI Prompt Vault" / "75 Power
Prompts") is the same idea at scale. This week, code **LAUNCH30** = 30% off:
https://schephenk.gumroad.com  (one-time, no subscription).

**Email 4 — Scarcity close (day 7)**
Subject: LAUNCH30 ends tonight
Body: Last call on 30% off. If now's not the time, no worries — keep the free pack,
it's yours. Link + code, one more time.

## Rules

- Max one email per 2 days during the sequence; then ~weekly value emails.
- Always lead with something useful; the offer is the P.S.
- Track which subject lines get opens; reuse winners (we literally sell an email
  subject-line product — use it on ourselves).
- Never buy lists or import emails that didn't opt in.

## Cadence after the sequence

Weekly: one genuinely useful tip + one soft product mention. The list only stays
valuable if people keep opening it, which means value has to outweigh pitches ~4:1.
