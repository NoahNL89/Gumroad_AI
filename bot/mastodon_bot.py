#!/usr/bin/env python3
"""
Mastodon bot for Schep Digital — promotes products and builds audience.

Usage:
    python3 bot/mastodon_bot.py promote   # Post a product promotion (max 3/day)
    python3 bot/mastodon_bot.py engage    # Like/boost/follow relevant hashtag posts
    python3 bot/mastodon_bot.py post "text"  # Post arbitrary text
"""
import os, sys, sqlite3, random, time
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    from mastodon import Mastodon
except ImportError:
    sys.exit("mastodon.py not installed. Run: pip3 install Mastodon.py")

ENV_PATH  = Path(__file__).parent.parent / ".env"
DB_PATH   = Path(__file__).parent.parent / "db" / "store.db"

MAX_POSTS_PER_DAY = 3
MASTODON_LIMIT    = 500
DISCOUNT_CODE     = "LAUNCH30"

# Hashtag sets by product category
HASHTAGS = {
    "ai_prompts":   "#AI #ChatGPT #AIPrompts #Productivity #PromptEngineering",
    "creative":     "#AIArt #MidjourneyAI #DigitalArt #CreativeAI #AIDesign",
    "blender":      "#Blender3D #AIArt #3DArt #BlenderPython #GenerativeAI",
    "business":     "#Solopreneur #SideHustle #DigitalProducts #OnlineBusiness #AITools",
    "writing":      "#Copywriting #ContentMarketing #EmailMarketing #AIWriting #Marketing",
    "freelance":    "#Freelancing #RemoteWork #Solopreneur #FreelanceLife #AITools",
    "growth":       "#SocialMedia #ContentCreator #CreatorEconomy #GrowthHacking #Marketing",
    "productivity": "#Productivity #GTD #NotionTemplates #PKM #WorkSmart",
    "default":      "#AI #Productivity #DigitalProducts #Solopreneur #AITools",
}

# Map product name keywords → hashtag category
def get_hashtags(name: str) -> str:
    name_l = name.lower()
    if "blender" in name_l:                    return HASHTAGS["blender"]
    if "character" in name_l or "midjourney" in name_l: return HASHTAGS["creative"]
    if "instagram" in name_l or "hook" in name_l or "viral" in name_l: return HASHTAGS["growth"]
    if "email" in name_l or "subject" in name_l:  return HASHTAGS["writing"]
    if "freelanc" in name_l or "proposal" in name_l: return HASHTAGS["freelance"]
    if "notion" in name_l or "habit" in name_l:   return HASHTAGS["productivity"]
    if "side hustle" in name_l or "business" in name_l or "cv" in name_l or "resume" in name_l:
        return HASHTAGS["business"]
    if "prompt" in name_l or "gemini" in name_l or "llm" in name_l or "vault" in name_l:
        return HASHTAGS["ai_prompts"]
    return HASHTAGS["default"]


def is_prompt_product(name: str) -> bool:
    """True only for actual prompt packs, so prompt-specific copy stays accurate."""
    n = name.lower()
    return any(k in n for k in ("prompt", "gemini", "llm", "vault"))


# ── Improved copy templates ────────────────────────────────────────────────────
# Templates use {name}, {price}, {url}, {code}, {hashtags}
# 70% value-first, 30% direct sell

# Generic value templates — safe for ANY product (templates, checklists, guides, prompt packs).
# These make no claim about the product being a set of prompts.
GENERIC_VALUE_TEMPLATES = [
    "I tracked how long I spent writing content last month: 14 hours.\n\nAfter building proper AI systems: 3 hours. Same output.\n\n'{name}' is the exact system. {url}\n(Use {code} at checkout — 30% off today)\n\n{hashtags}",

    "Unpopular opinion: most digital products are too generic to be useful.\n\nSo I built '{name}' around ONE specific workflow — tested, refined, done.\n\nGrab it for {price}: {url}\n\n{hashtags}",

    "The AI tools you're paying for monthly cost more than a one-time system that does the same job.\n\n'{name}' — {price} once, yours forever.\n\nCode {code} takes it to 30% off: {url}\n\n{hashtags}",

    "If you're spending more than 20 min on a task AI should handle in 2 min, you need a system.\n\n'{name}' is mine. {price} → instant download.\n{url}\n\nCode {code}: 30% off\n\n{hashtags}",
]

# Prompt-pack-only templates — these claim the product IS a set of prompts/prompt frameworks.
# Only used when the product is actually a prompt pack (see is_prompt_product).
PROMPT_VALUE_TEMPLATES = [
    "Most AI users write prompts like search queries. That's why their output is mediocre.\n\nThe fix: treat every prompt as a job spec — role, context, format, constraints.\n\n'{name}' is written exactly this way, ready to copy-paste.\n{url} ({price} — code {code} for 30% off)\n\n{hashtags}",

    "Quick win for your workflow this week:\n\n✅ Stop writing prompts from scratch\n✅ Use tested frameworks instead\n✅ Get consistent output every time\n\n'{name}' has the frameworks: {url}\n\n{hashtags}",

    "3 things that changed my AI workflow:\n\n1. Structured prompt templates (not vibes)\n2. Batch processing instead of one-by-one\n3. A system for consistency\n\n'{name}' covers all three: {url}\n\n{hashtags}",
]

# Backwards-compatible alias for any external caller that imports VALUE_TEMPLATES.
VALUE_TEMPLATES = GENERIC_VALUE_TEMPLATES + PROMPT_VALUE_TEMPLATES

SELL_TEMPLATES = [
    "🔥 '{name}' — {price}\n\nInstant download. Use code {code} for 30% off.\n{url}\n\n{hashtags}",

    "Just dropped: '{name}'\n\nEverything I know about this workflow, packaged for instant use.\n{price} → {url}\n\nCode {code} = 30% off today.\n\n{hashtags}",

    "Stop reinventing the wheel.\n\n'{name}' gives you the exact system, ready to use. {price} once.\n{url}\n\n{hashtags}",
]

BUNDLE_TEMPLATES = [
    "Built 10 AI systems over 6 months.\n\nPackaged all of them into one bundle at €29.99 — less than the cost of one month of ChatGPT Plus.\n\nThe Complete AI Creator Toolkit: {url}\n(Code {code}: 30% off → €21)\n\n{hashtags}",

    "Instead of buying 10 separate tools:\n\nThe Complete AI Creator Toolkit bundles everything for €29.99.\nUse code {code} for 30% off → €21 total.\n\n{url}\n\n{hashtags}",
]


def load_env():
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def get_client():
    load_env()
    token = os.environ.get("MASTODON_ACCESS_TOKEN")
    instance = os.environ.get("MASTODON_INSTANCE", "https://mastodon.social")
    if not token:
        sys.exit("MASTODON_ACCESS_TOKEN not set in .env")
    return Mastodon(access_token=token, api_base_url=instance)


def log_promotion(platform, product_id, url, content):
    if not DB_PATH.exists():
        return
    with sqlite3.connect(str(DB_PATH)) as con:
        con.execute(
            "INSERT INTO promotions (platform, product_id, url, content, posted_at) VALUES (?,?,?,?,?)",
            (platform, product_id, url, content, datetime.now(timezone.utc).isoformat())
        )


def check_rate_limit():
    if not DB_PATH.exists():
        print("DB not found — fail-closed on rate limit")
        return False
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    with sqlite3.connect(str(DB_PATH)) as con:
        count = con.execute(
            "SELECT COUNT(*) FROM promotions WHERE platform='mastodon' AND posted_at >= ?", (cutoff,)
        ).fetchone()[0]
    if count >= MAX_POSTS_PER_DAY:
        print(f"Rate limit: already posted {count}x in last 24h (max {MAX_POSTS_PER_DAY})")
        return False
    return True


def post_message(text, product_id=None, url=None):
    if not check_rate_limit():
        return False
    if len(text) > MASTODON_LIMIT:
        text = text[:MASTODON_LIMIT - 3] + "..."
    client = get_client()
    print(f"Posting to Mastodon:\n{text}\n")
    post = client.status_post(text)
    log_promotion("mastodon", product_id, url, text)
    print(f"Posted: {post['url']}")
    return True


def promote_random_product():
    if not DB_PATH.exists():
        sys.exit("DB not found. Run: python3 db/sync.py")

    with sqlite3.connect(str(DB_PATH)) as con:
        con.row_factory = sqlite3.Row
        products = con.execute(
            "SELECT id, name, formatted_price, short_url FROM products WHERE published=1 AND price_cents > 99"
        ).fetchall()
        last = con.execute(
            "SELECT product_id FROM promotions WHERE platform='mastodon' ORDER BY posted_at DESC LIMIT 3"
        ).fetchall()

    if not products:
        sys.exit("No products found.")

    recent_ids = {r["product_id"] for r in last}
    bundle = next((p for p in products if "toolkit" in p["name"].lower() or "bundle" in p["name"].lower()), None)

    # 20% chance to promote the bundle specifically
    if bundle and random.random() < 0.20:
        p = bundle
        tmpl = random.choice(BUNDLE_TEMPLATES)
    else:
        pool = [p for p in products if p["id"] not in recent_ids] or list(products)
        p = random.choice(pool)
        if random.random() < 0.70:
            value_pool = GENERIC_VALUE_TEMPLATES + (
                PROMPT_VALUE_TEMPLATES if is_prompt_product(p["name"]) else []
            )
            tmpl = random.choice(value_pool)
        else:
            tmpl = random.choice(SELL_TEMPLATES)

    url = p["short_url"] or "https://schephenk.gumroad.com"
    tags = get_hashtags(p["name"])
    text = tmpl.format(
        name=p["name"],
        price=p["formatted_price"],
        url=url,
        code=DISCOUNT_CODE,
        hashtags=tags,
    )
    post_message(text, product_id=p["id"], url=url)


def engage_community():
    client = get_client()
    tags = ["AItools", "Productivity", "Solopreneur", "PromptEngineering", "CreatorEconomy",
            "SideHustle", "ContentCreator", "DigitalMarketing"]
    tag = random.choice(tags)
    print(f"Engaging #{tag}...")
    try:
        results = client.timeline_hashtag(tag, limit=10)
    except Exception as e:
        sys.exit(f"Error: {e}")

    me = client.me()
    interactions = 0
    for status in results:
        if status.account.id == me.id:
            continue
        try:
            if not status.favourited:
                client.status_favourite(status.id)
                print(f"  Liked: @{status.account.acct}")
                interactions += 1
            if not status.reblogged and random.random() < 0.25:
                client.status_reblog(status.id)
                print(f"  Boosted: @{status.account.acct}")
                interactions += 1
            if random.random() < 0.35:
                client.account_follow(status.account.id)
                print(f"  Followed: @{status.account.acct}")
                interactions += 1
            time.sleep(1.5)
        except Exception as e:
            print(f"  Skip {status.id}: {e}")

    print(f"Done. {interactions} interactions on #{tag}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bot/mastodon_bot.py [promote | engage | post <text>]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "promote":
        promote_random_product()
    elif cmd == "engage":
        engage_community()
    elif cmd == "post":
        text = " ".join(sys.argv[2:])
        if not text:
            sys.exit("Provide text to post.")
        post_message(text)
    else:
        print(f"Unknown: {cmd}")
        sys.exit(1)
