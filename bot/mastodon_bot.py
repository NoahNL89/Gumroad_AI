#!/usr/bin/env python3
"""
Mastodon bot for Schep Digital — promotes products and builds audience.

Usage:
    python3 bot/mastodon_bot.py promote   # Post one useful campaign item per 24h
    python3 bot/mastodon_bot.py post "text"  # Post arbitrary text
"""
import os, sys, sqlite3, random, time
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    from campaign import DISCOUNT_CODE, campaign_product, next_variant, tracked_url
except ImportError:  # package import in tests/tools
    from .campaign import DISCOUNT_CODE, campaign_product, next_variant, tracked_url

try:
    from mastodon import Mastodon
except ImportError:
    sys.exit("mastodon.py not installed. Run: pip3 install Mastodon.py")

ENV_PATH  = Path(__file__).parent.parent / ".env"
DB_PATH   = Path(__file__).parent.parent / "db" / "store.db"

MAX_POSTS_PER_DAY = 1
MASTODON_LIMIT    = 500

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
    "Built 10 AI systems over 6 months.\n\nPackaged all of them into one practical bundle at {price}.\n\nThe Complete AI Creator Toolkit: {url}\n(Code {code}: 30% off)\n\n{hashtags}",

    "Instead of buying 10 separate tools:\n\nThe Complete AI Creator Toolkit bundles everything for {price}.\nUse code {code} for 30% off.\n\n{url}\n\n{hashtags}",
]

# A focused seven-day campaign: five useful lessons for every direct offer.
# Specific teaching earns more attention than rotating generic product pitches.
FOCUS_TEMPLATES = [
    "Before installing local AI, check three things: available memory, free storage, and the one real task you need it to do. Bigger is not automatically better.\n\nI made a free 5-minute readiness kit with the exact audit: {url}\n\n{hashtags}",
    "“Local” is not automatically private. Check the whole path: model runner, browser UI, tools, cloud-synced folders, and network binding.\n\nFree private-AI boundary checklist: {url}\n\n{hashtags}",
    "For a first local-AI fit test: close heavy apps, use one small model, repeat the same prompt three times, and inspect where it runs. Keep the smallest setup that passes your task.\n\nFree checklist: {url}\n\n{hashtags}",
    "Choose a local model by the job, not hype:\n\n• drafting or code?\n• short chat or long documents?\n• speed or best output?\n\nDecide before downloading. Free readiness kit: {url}\n\n{hashtags}",
    "A useful local-AI test has four steps: inspect hardware, choose one task, measure the run, then repeat offline. That reveals more than a model leaderboard.\n\nGet the free test sheet: {url}\n\n{hashtags}",
    "Not sure whether your computer is ready for private AI? This free kit gives you a hardware audit, privacy boundary, model-fit test, and a clear next-step decision.\n\n{url}\n\n{hashtags}",
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


def engagement_due():
    """Allow at most one automated engagement batch per rolling 24 hours."""
    if not DB_PATH.exists():
        print("DB not found — fail-closed on engagement")
        return False
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    with sqlite3.connect(str(DB_PATH)) as con:
        count = con.execute(
            "SELECT COUNT(*) FROM promotions WHERE platform='mastodon_engage' AND posted_at >= ?",
            (cutoff,),
        ).fetchone()[0]
    if count:
        print("Engagement skipped: Mastodon batch already ran in the last 24h")
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


def promote_focus_product():
    if not DB_PATH.exists():
        sys.exit("DB not found. Run: python3 db/sync.py")

    with sqlite3.connect(str(DB_PATH)) as con:
        p = campaign_product(con)
        if not p:
            sys.exit("Free Private AI readiness product not found. Run: python3 db/sync.py")
        variant = next_variant(con, "mastodon", p["id"], len(FOCUS_TEMPLATES))

    url = tracked_url(
        p["short_url"] or "https://schephenk.gumroad.com/l/rohes",
        "mastodon",
        f"l{variant + 1}",
    )
    tags = "#LocalAI #Privacy #Ollama #OpenSourceAI"
    text = FOCUS_TEMPLATES[variant].format(
        name=p["name"],
        price=p["formatted_price"],
        url=url,
        code=DISCOUNT_CODE,
        hashtags=tags,
    )
    post_message(text, product_id=p["id"], url=url)


# Keep the historical function name for cron jobs and external callers.
promote_random_product = promote_focus_product


def engage_community():
    if not engagement_due():
        return False
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
    seen_accounts = set()
    for status in results:
        if status.account.id == me.id:
            continue
        # One account = one interaction set per run. Hashtag timelines are often
        # dominated by a single prolific poster; without this we'd like/boost/follow
        # the same account 10+ times in a burst, which reads as bot spam and gets
        # the account rate-limited. Spreading across distinct accounts grows reach.
        if status.account.id in seen_accounts:
            continue
        seen_accounts.add(status.account.id)
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

    summary = f"{interactions} interactions on #{tag}"
    log_promotion("mastodon_engage", None, None, summary)
    print(f"Done. {summary}")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bot/mastodon_bot.py [promote | engage | post <text>]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "promote":
        promote_focus_product()
    elif cmd == "engage":
        print("Automated unsolicited engagement is disabled; publish useful owned-account posts instead.")
    elif cmd == "post":
        text = " ".join(sys.argv[2:])
        if not text:
            sys.exit("Provide text to post.")
        post_message(text)
    else:
        print(f"Unknown: {cmd}")
        sys.exit(1)
