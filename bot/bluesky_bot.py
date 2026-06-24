#!/usr/bin/env python3
"""
Bluesky bot for Schep Digital — promotes products with proper hashtag facets.

Usage:
    python3 bot/bluesky_bot.py promote   # Post a product promotion (max 3/day)
    python3 bot/bluesky_bot.py engage    # Like/follow relevant hashtag posts
    python3 bot/bluesky_bot.py post "text"  # Post arbitrary text
"""
import os, sys, sqlite3, random, re
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    from atproto import Client, models
    from atproto_client.utils import TextBuilder
except ImportError:
    sys.exit("atproto not installed. Run: pip3 install atproto")

ENV_PATH  = Path(__file__).parent.parent / ".env"
DB_PATH   = Path(__file__).parent.parent / "db" / "store.db"

MAX_POSTS_PER_DAY = 3
BLUESKY_LIMIT     = 300
DISCOUNT_CODE     = "LAUNCH30"

# Hashtags by category (5-6 per post for Bluesky discovery)
HASHTAGS = {
    "ai_prompts":   ["AI", "ChatGPT", "AIPrompts", "PromptEngineering", "Productivity"],
    "creative":     ["AIArt", "MidjourneyAI", "DigitalArt", "CreativeAI", "AIDesign"],
    "blender":      ["Blender3D", "AIArt", "3DArt", "BlenderPython", "GenerativeAI"],
    "business":     ["Solopreneur", "SideHustle", "DigitalProducts", "OnlineBusiness", "AITools"],
    "writing":      ["Copywriting", "ContentMarketing", "EmailMarketing", "AIWriting", "Marketing"],
    "freelance":    ["Freelancing", "RemoteWork", "Solopreneur", "FreelanceLife", "AITools"],
    "growth":       ["SocialMedia", "ContentCreator", "CreatorEconomy", "GrowthHacking", "Marketing"],
    "productivity": ["Productivity", "GTD", "NotionTemplates", "PKM", "WorkSmart"],
    "default":      ["AI", "Productivity", "DigitalProducts", "Solopreneur", "AITools"],
}


def get_tag_list(name: str) -> list[str]:
    n = name.lower()
    if "blender" in n:                              return HASHTAGS["blender"]
    if "character" in n or "midjourney" in n:       return HASHTAGS["creative"]
    if "instagram" in n or "hook" in n or "viral" in n: return HASHTAGS["growth"]
    if "email" in n or "subject" in n:              return HASHTAGS["writing"]
    if "freelanc" in n or "proposal" in n:          return HASHTAGS["freelance"]
    if "notion" in n or "habit" in n:               return HASHTAGS["productivity"]
    if "side hustle" in n or "business" in n or "cv" in n or "resume" in n:
        return HASHTAGS["business"]
    if "prompt" in n or "gemini" in n or "llm" in n or "vault" in n:
        return HASHTAGS["ai_prompts"]
    return HASHTAGS["default"]


def is_prompt_product(name: str) -> bool:
    """True only for actual prompt packs, so prompt-specific copy stays accurate."""
    n = name.lower()
    return any(k in n for k in ("prompt", "gemini", "llm", "vault"))


# Short copy blocks that fit Bluesky's 300 char limit
# Variables: {name} {price} {url} {code}
# Generic value templates — safe for ANY product. No prompt-pack-specific claims.
GENERIC_VALUE_TEMPLATES = [
    "Spent 14h on content last month. After building AI systems: 3h. Same output.\n\n'{name}' is the system.\n{price} → {url}\nCode {code}: 30% off",

    "One-time purchase. No subscription, no monthly fee.\n\n'{name}' — {price}, instant download.\n{url}\nCode {code} = 30% off",

    "Built this so you don't have to start from a blank page.\n\n'{name}': everything ready to use. {price} once.\n{url} (code {code} = 30% off)",
]

# Prompt-pack-only templates — claim the product IS a set of prompts. Gated by is_prompt_product.
PROMPT_VALUE_TEMPLATES = [
    "Most AI users write prompts like Google searches.\n\nResult: mediocre output.\n\nFix: treat prompts as job specs — role, context, format, constraints.\n\n'{name}' is built this way.\n{url} | code {code} = 30% off",

    "The best AI tool you have is the one with a proven prompt behind it.\n\n'{name}' — {price}, instant download.\n{url}\nCode {code} saves 30%",

    "Stop writing prompts from scratch every time.\n\n'{name}' = copy-paste templates that actually work.\n{price} once, yours forever.\n{url}",

    "Quick workflow upgrade:\n✅ Structured prompts\n✅ Tested templates\n✅ Consistent output\n\n'{name}': {url}\n({price} — code {code} for 30% off)",
]

# Backwards-compatible alias for any external caller that imports VALUE_TEMPLATES.
VALUE_TEMPLATES = GENERIC_VALUE_TEMPLATES + PROMPT_VALUE_TEMPLATES

SELL_TEMPLATES = [
    "'{name}' — {price}\n\nInstant download. Code {code} = 30% off at checkout.\n{url}",
    "New: '{name}'\nEverything you need, ready to use. {price}.\n{url}\nCode {code} = 30% off",
]

BUNDLE_TEMPLATES = [
    "10 AI systems. One bundle. €29.99.\n\nLess than one month of ChatGPT Plus.\n\nThe Complete AI Creator Toolkit:\n{url}\nCode {code} = 30% off → €21 total",

    "Instead of 10 separate tools:\n\nComplete AI Creator Toolkit bundles all of them.\n€29.99 (code {code} → €21)\n{url}",
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
    user = os.environ.get("BLUESKY_USERNAME")
    pw   = os.environ.get("BLUESKY_PASSWORD")
    if not user or not pw:
        sys.exit("BLUESKY_USERNAME or BLUESKY_PASSWORD not set in .env")
    client = Client()
    client.login(user, pw)
    return client


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
        return False
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    with sqlite3.connect(str(DB_PATH)) as con:
        count = con.execute(
            "SELECT COUNT(*) FROM promotions WHERE platform='bluesky' AND posted_at >= ?", (cutoff,)
        ).fetchone()[0]
    if count >= MAX_POSTS_PER_DAY:
        print(f"Rate limit: already posted {count}x today (max {MAX_POSTS_PER_DAY})")
        return False
    return True


def build_post_with_facets(body: str, tags: list[str]) -> tuple[str, list]:
    """
    Build text + facets list for Bluesky.
    Appends hashtags as clickable facets using TextBuilder.
    Returns (full_text, facets_list).
    """
    tb = TextBuilder()
    # Add the main body
    tb.text(body.rstrip())
    tb.text("\n\n")
    for i, tag in enumerate(tags):
        tb.tag(f"#{tag}", tag)
        if i < len(tags) - 1:
            tb.text(" ")
    return tb


def post_message(text: str, tags: list = None, product_id=None, url=None):
    if not check_rate_limit():
        return False

    client = get_client()
    tags = tags or []

    if tags:
        tb = build_post_with_facets(text, tags)
        full_text = tb.build_text()
        if len(full_text) > BLUESKY_LIMIT:
            overflow = len(full_text) - BLUESKY_LIMIT
            text = text[:len(text) - overflow - 3] + "..."
            tb = build_post_with_facets(text, tags)
            full_text = tb.build_text()
        print(f"Posting to Bluesky:\n{full_text}\n")
        post = client.send_post(tb)
    else:
        if len(text) > BLUESKY_LIMIT:
            text = text[:BLUESKY_LIMIT - 3] + "..."
        full_text = text
        print(f"Posting to Bluesky:\n{full_text}\n")
        post = client.send_post(text)

    log_promotion("bluesky", product_id, url, full_text)
    print(f"Posted: {post.uri}")
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
            "SELECT product_id FROM promotions WHERE platform='bluesky' ORDER BY posted_at DESC LIMIT 3"
        ).fetchall()

    if not products:
        sys.exit("No products found.")

    recent_ids = {r["product_id"] for r in last}
    bundle = next((p for p in products if "toolkit" in p["name"].lower() or "bundle" in p["name"].lower()), None)

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
    tags = get_tag_list(p["name"])

    body = tmpl.format(
        name=p["name"],
        price=p["formatted_price"],
        url=url,
        code=DISCOUNT_CODE,
    )
    post_message(body, tags=tags, product_id=p["id"], url=url)


def engage_community():
    """Like and optionally follow posts under AI/productivity hashtags."""
    client = get_client()
    search_tags = ["AItools", "Productivity", "Solopreneur", "PromptEngineering", "SideHustle"]
    tag = random.choice(search_tags)
    print(f"Engaging #{tag} on Bluesky...")

    try:
        # Search recent posts with the tag
        results = client.app.bsky.feed.search_posts({"q": f"#{tag}", "limit": 15})
        posts = results.posts if hasattr(results, "posts") else []
    except Exception as e:
        print(f"Search failed: {e}")
        return

    me = client.me
    interactions = 0
    for post in posts:
        try:
            author_did = post.author.did if hasattr(post.author, "did") else None
            if author_did and me and author_did == me.did:
                continue
            # Like
            client.like(post.uri, post.cid)
            print(f"  Liked: @{post.author.handle}")
            interactions += 1
            # Repost (25%)
            if random.random() < 0.25:
                client.repost(post.uri, post.cid)
                print(f"  Reposted: @{post.author.handle}")
                interactions += 1
            # Follow (30%)
            if author_did and random.random() < 0.30:
                client.follow(author_did)
                print(f"  Followed: @{post.author.handle}")
                interactions += 1
        except Exception as e:
            print(f"  Skip: {e}")

    print(f"Done. {interactions} interactions on #{tag}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bot/bluesky_bot.py [promote | engage | post <text>]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "promote":
        promote_random_product()
    elif cmd == "engage":
        engage_community()
    elif cmd == "post":
        text = " ".join(sys.argv[2:])
        if not text:
            sys.exit("Provide text.")
        post_message(text)
    else:
        print(f"Unknown: {cmd}")
        sys.exit(1)
