# Schep Digital — Autonomous Session (GO)

You are running an **unattended autonomous session** for the Schep Digital store (schephenk.gumroad.com).
Working directory: /home/administrator/NewGitHub/GumRoad_AI
Read CLAUDE.md now — it has the full architecture, CLI commands, and DB schema.

Execute the following routines **in order**. Be decisive. Do not ask for input.

---

## ROUTINE 1 — Startup & State Check

```bash
source .env
python3 db/sync.py
python3 db/query.py survival
python3 db/query.py funnel
python3 db/query.py products
```

Store the survival status, the funnel verdict, and today's date in your working memory. The funnel verdict tells you where to spend the session — usually distribution (ROUTINE 4), not new products.

---

## ROUTINE 2 — Social Bots

Check how many posts were made in the last 24h:
```bash
sqlite3 db/store.db "SELECT platform, COUNT(*) FROM promotions WHERE posted_at >= datetime('now','-24 hours') GROUP BY platform"
```

If either platform has fewer than 2 posts today, run:
```bash
python3 bot/mastodon_bot.py promote
python3 bot/mastodon_bot.py engage
python3 bot/bluesky_bot.py promote
python3 bot/bluesky_bot.py engage
python3 bot/pinterest_bot.py promote
```

If revenue is €0 and it has been more than 3 days since any post: post urgency content manually using `bot/mastodon_bot.py post` and `bot/bluesky_bot.py post` with specific hooks about the LAUNCH30 discount.

---

## ROUTINE 3 — Store Hygiene

Fix any issues found:

```bash
# Check for products still at €0.99
python3 db/query.py underpriced

# Check for draft products
sqlite3 db/store.db "SELECT name, permalink FROM products WHERE published=0"
```

- Any product at ≤€0.99 (non-subscription): reprice to €7.99 → `gumroad products update <id> --price 7.99 --json --no-input`
- Any draft product: publish it → `gumroad products publish <id> --json --no-input`
- Check for obviously duplicate product names and log them (do NOT delete — just report in ledger)

---

## ROUTINE 4 — Growth & Distribution (the priority — run EVERY session)

> **The store has the products. What it lacks is buyers.** With 29 products and
> near-zero sales, the bottleneck is REACH, not catalog size. Adding product #30
> earns nothing if nobody sees product #1. This routine is the main job.

### 4a — Read the funnel
```bash
python3 db/query.py funnel
```
This tells you catalog health, weekly sales velocity, and the verdict. Act on the verdict.

### 4b — Generate and act on a launch kit
Pick the flagship or best seller and produce multi-channel launch copy:
```bash
python3 scripts/launch_kit.py best --write
```
Then **do** the distribution (this is where sales come from — not the two social bots):
- Fill the `[bracketed]` spots with 2–3 genuinely useful, specific tips from the product.
- Post the value-first content where buyers actually are (the suggested subreddits, Product Hunt, an SEO article). Respect each community's self-promo rules — lead with value, link as a P.S.
- Rotate which product gets a kit each session so the whole catalog gets exposure over time.

### 4c — Keep the free lead magnet live (email capture = the compounding asset)
A free product collects buyer emails you can market to forever. If it isn't live yet, publish it once:
```bash
bash scripts/create_lead_magnet.sh        # builds + publishes "The AI Quick-Start Pack (Free)"
```
Then run the nurture sequence in `agent/EMAIL_FLOW.md` against your audience.

### 4d — New product? Only if EVIDENCE says so (not on a timer)
Do **not** create a new product just because 7 days passed — that only adds near-duplicates to a saturated catalog. Build a new one **only if all are true**:
- The funnel shows existing products are getting traffic but a clear, *different* need is unmet.
- No near-duplicate already exists (we already have ~4 prompt vaults, 3 "75 prompts", 4 Character Genesis — do not add more of these).
- You can make it genuinely best-in-niche, not generic.

If those hold, build it with the data-driven engine (steps below). Otherwise skip and do more 4b distribution.

---

## ROUTINE 5 — New Product Build Pipeline (only when ROUTINE 4d approves)

### 5a — Research: Find the product gap

Use web search and your knowledge to identify ONE high-value digital product gap in the AI tools / productivity / creator economy niche that is not already in the catalog. The product must be:
- Actionable (templates, checklists, prompt packs, guides, systems)
- AI-focused or AI-enhanced
- Priced €7.99–€14.99 as a one-time download
- Different from existing catalog products

Decide on:
- `product_name` — punchy, benefit-led title
- `slug` — lowercase-dashes, no numbers at start (e.g. `ai-meeting-mastery`)  
- `tagline` — one sentence, max 120 chars
- `price` — €7.99, €9.99, or €14.99
- `description` — 3-paragraph Gumroad product page (hook + what's inside + who it's for)
- `content_outline` — 6–8 chapter headings with 3–5 bullet points each

Write this to: `agent/new_product_plan.json`

### 5b — Generate Images with Codex

Use the `codex` executable available on `PATH` (or `$CODEX_BIN` when explicitly configured).

Create the image output directory first:
```bash
mkdir -p codex_images/<slug>
```

Then call Codex to write and run an image generation script:
```bash
${CODEX_BIN:-codex} exec "Write a Python script that uses the OpenAI images API (DALL-E 3, size 1792x1024, quality standard) to generate these 4 images for a digital product called '<product_name>'. Dark cinematic aesthetic, deep purple/violet tones (oklch 0.10 0.02 285 background), no text, no words, no labels. Professional, premium feel.

1. key-art.jpg — hero cover art: abstract representation of the product theme, dramatic lighting, orbiting elements
2. interior-01-<theme>.jpg — conceptual illustration for chapter 1 topic
3. interior-02-<theme>.jpg — conceptual illustration for chapter 2 topic  
4. interior-03-<theme>.jpg — conceptual illustration for chapter 3 topic

Save all images to: /home/administrator/NewGitHub/GumRoad_AI/codex_images/<slug>/
Use OPENAI_API_KEY from environment. Run the script immediately after writing it."
```

Verify images were created:
```bash
ls -la codex_images/<slug>/
```

### 5c — Create Product PDF (data-driven builder)

You are now creating the PDF. Do **not** write a new bespoke generator script — use the shared, data-driven engine `scripts/product_builder.py` (dark-violet design system, auto-escaping, 8 block types). The legacy `scripts/gen_*.py` files are deprecated historical one-offs; do not copy them.

1. Write a product **spec** as JSON to `agent/specs/<slug>.spec.json`. Run `python3 scripts/product_builder.py --help` to see the full spec format, or `--demo` to emit a working example. The spec must:
   - Provide `slug`, `title`, `subtitle`, `eyebrow`, and `meta` (format / pages / compatibility).
   - Include every chapter from the content outline under `chapters`, each with a `num`, `title`, `sub`, and `blocks`.
   - Use the block types (`p`, `h3`, `callout`, `prompt`, `item`, `checklist`, `table`, `stats`) — at least one `callout` and one `prompt`/`checklist`/`table` per chapter.
   - Be substantive — each chapter minimum 400 words of real usable content (put prose in `p` blocks; the builder escapes everything, so write plain text, not HTML).

2. Build the HTML (the builder validates the spec and fails loudly on errors):
   ```bash
   python3 scripts/product_builder.py agent/specs/<slug>.spec.json
   ```

3. Invoke the impeccable design skill to review the generated `downloads/pdfs/<slug>.html` before PDF export. Apply improvements to the **spec**, then re-run the builder (do not hand-edit the HTML — it is regenerated).

4. Inject Codex images:
   Add the slug→folder mapping to `scripts/inject_images.py`'s `PRODUCT_IMAGE_MAP`, then run:
   ```bash
   python3 scripts/inject_images.py
   ```

5. Generate the PDF:
   ```bash
   google-chrome --headless --no-sandbox --disable-gpu \
     --print-to-pdf=downloads/pdfs/<slug>.pdf \
     --print-to-pdf-no-header --no-pdf-header-footer \
     "file:///home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/<slug>.html"
   ```

   Verify the PDF exists and is >500KB:
   ```bash
   ls -lh downloads/pdfs/<slug>.pdf
   ```

### 5d — Upload to Gumroad

```bash
# Create the product
gumroad products create \
  --name "<product_name>" \
  --price <price> \
  --currency eur \
  --description "<description>" \
  --json --no-input

# Capture the product ID from the JSON response, then:
gumroad products update <id> \
  --file downloads/pdfs/<slug>.pdf \
  --file-name "<product_name> (Schep Digital).pdf" \
  --json --no-input --yes

# Publish it
gumroad products publish <id> --json --no-input

# Add the LAUNCH30 discount
gumroad offer-codes create --product <id> --name LAUNCH30 --percent-off 30 --json --no-input --yes
```

### 5e — Beautiful Product Page

Update the product description with a full, conversion-optimised Gumroad page. Write it yourself — make it specific, punchy, benefit-driven. Include:
- **Hook headline** (1 sentence — the transformation)
- **The problem** (2-3 sentences)
- **What's inside** (bullet list of chapters/sections)
- **Who this is for** (3 bullet personas)
- **What you get** (format, page count, compatibility)
- **Guarantee or promise** (1 sentence)

Upload a thumbnail: use `key-art.jpg` as the product thumbnail/preview image:
```bash
gumroad products update <id> \
  --preview-url "file://$(pwd)/codex_images/<slug>/key-art.jpg" \
  --json --no-input --yes
```

### 5f — Launch Announcement

Post to both socials about the new product:
```bash
python3 bot/mastodon_bot.py post "🆕 Just dropped: '<product_name>' — <tagline>. Get it for €<price> (code LAUNCH30 = 30% off this week): <gumroad_url> #AI #DigitalProducts"

python3 bot/bluesky_bot.py post "New: '<product_name>'. <tagline> €<price> → <gumroad_url> (LAUNCH30 = 30% off)"

python3 bot/pinterest_bot.py promote
```

---

## ROUTINE 6 — Sync & Ledger

After all routines:
```bash
python3 db/sync.py
python3 db/query.py survival
```

Update `agent/ledger.json` — append an entry with today's date (ISO format), actions taken, new product created (if any), social posts made, revenue status.

```bash
git add agent/ledger.json scripts/ codex_images/ bot/   # NOTE: db/store.db and downloads/ are gitignored — do not add them
git commit -m "agent: autonomous session $(date +%Y-%m-%d) — <brief summary>"
```

---

## Hard Constraints

- **Social posts**: max 3 per platform per 24h — bots enforce this automatically
- **Pricing**: never change a price by more than 50% in one session
- **Deletion**: never delete any product, file, or DB record — only create or update
- **Spending**: only use APIs already configured in .env — no new paid services
- **Scope**: only execute actions defined in this document — do not go beyond
- **If Codex image generation fails**: continue with the PDF using placeholder CSS gradients instead of images, note failure in ledger
- **If revenue is €0 for 14+ days**: create FLASH50 discount (50% off, all products), post urgency content to both socials, note in ledger

---

## Store Context

- ~29 live products (always confirm with `python3 db/query.py products` — this number drifts), AI tools / templates / productivity niche
- Currency: EUR, paid price range €5.99–€29.99 (one €0 subscription is exempt from repricing)
- Survival target: €58/month (covers Claude + Codex subscriptions)
- Active discount: LAUNCH30 (30% off, all products)
- Social: @schep_digital on Mastodon (mastodon.social) + Bluesky
- Design system: dark violet (`scripts/shared_css.py`) — all PDFs use this
