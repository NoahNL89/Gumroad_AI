#!/usr/bin/env python3
"""
Bluesky bot for Schep Digital — promotes products with proper hashtag facets.

Usage:
    python3 bot/bluesky_bot.py promote   # Post one useful campaign item per 24h
    python3 bot/bluesky_bot.py post "text"  # Post arbitrary text
"""
import os, sys, sqlite3, random, re
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    from campaign import DISCOUNT_CODE, campaign_product, next_variant, tracked_url
except ImportError:  # package import in tests/tools
    from .campaign import DISCOUNT_CODE, campaign_product, next_variant, tracked_url

try:
    from atproto import Client, models
    from atproto_client.utils import TextBuilder
except ImportError:
    sys.exit("atproto not installed. Run: pip3 install atproto")

ENV_PATH  = Path(__file__).parent.parent / ".env"
DB_PATH   = Path(__file__).parent.parent / "db" / "store.db"

MAX_POSTS_PER_DAY = 1
BLUESKY_LIMIT     = 300

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
    "10 practical AI systems. One bundle. {price}.\n\nThe Complete AI Creator Toolkit:\n{url}\nCode {code} = 30% off",

    "Instead of 10 separate tools:\n\nThe Complete AI Creator Toolkit bundles all of them.\n{price} (code {code} = 30% off)\n{url}",
]

FOCUS_TEMPLATES = [
    "Freelancers: before putting client documents into any AI workflow, decide what must stay off third-party servers. Then check whether your computer can handle the task locally.\n\nFree readiness kit: {url}",
    "Consultants using AI with client files: “local” is not automatically private. Check the runner, browser UI, synced folders, tools and network binding.\n\nFree checklist: {url}",
    "First client-work fit test: use non-sensitive sample text, close heavy apps, run one small local model and repeat the task 3 times.\n\nFree readiness kit: {url}",
    "Freelancers do not need the biggest local model. Start with the job—proposals, document summaries, code or notes—then choose the smallest setup that passes.\n\nFree kit: {url}",
    "Before using local AI for client work, test hardware fit, one real task, repeatable output and offline behavior—with non-sensitive material.\n\nFree test sheet: {url}",
    "Handle client documents and wondering whether your laptop can run AI locally? Audit memory, storage, workflow boundaries and one real task first.\n\nFree readiness kit: {url}",
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


def engagement_due():
    """Allow at most one automated engagement batch per rolling 24 hours."""
    if not DB_PATH.exists():
        print("DB not found — fail-closed on engagement")
        return False
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    with sqlite3.connect(str(DB_PATH)) as con:
        count = con.execute(
            "SELECT COUNT(*) FROM promotions WHERE platform='bluesky_engage' AND posted_at >= ?",
            (cutoff,),
        ).fetchone()[0]
    if count:
        print("Engagement skipped: Bluesky batch already ran in the last 24h")
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


def fit_post_text(text: str, tags: list[str], url: str | None = None) -> str:
    """Fit Bluesky's limit without ever slicing a destination URL."""
    tag_suffix = "\n\n" + " ".join(f"#{tag}" for tag in tags) if tags else ""
    body_limit = BLUESKY_LIMIT - len(tag_suffix)
    if len(text) <= body_limit:
        return text
    if url and url in text:
        prefix = text.split(url, 1)[0].rstrip()
        prefix_limit = body_limit - len(url) - 1
        if prefix_limit >= 2:
            prefix = prefix[: prefix_limit - 1].rstrip() + "…"
            return f"{prefix}\n{url}"
        return url
    return text[: body_limit - 1].rstrip() + "…"


def post_message(text: str, tags: list = None, product_id=None, url=None):
    if not check_rate_limit():
        return False

    client = get_client()
    tags = tags or []

    if tags:
        text = fit_post_text(text, tags, url=url)
        tb = build_post_with_facets(text, tags)
        full_text = tb.build_text()
        if len(full_text) > BLUESKY_LIMIT:
            raise RuntimeError("Bluesky post fitter exceeded the platform limit")
        print(f"Posting to Bluesky:\n{full_text}\n")
        post = client.send_post(tb)
    else:
        text = fit_post_text(text, tags, url=url)
        full_text = text
        print(f"Posting to Bluesky:\n{full_text}\n")
        post = client.send_post(text)

    log_promotion("bluesky", product_id, url, full_text)
    print(f"Posted: {post.uri}")
    return True


def promote_focus_product():
    if not DB_PATH.exists():
        sys.exit("DB not found. Run: python3 db/sync.py")

    with sqlite3.connect(str(DB_PATH)) as con:
        p = campaign_product(con)
        if not p:
            sys.exit("Free Private AI readiness product not found. Run: python3 db/sync.py")
        variant = next_variant(con, "bluesky", p["id"], len(FOCUS_TEMPLATES))

    url = tracked_url(
        p["short_url"] or "https://schephenk.gumroad.com/l/rohes",
        "bluesky",
        f"l{variant + 1}",
    )
    tags = ["LocalAI", "Privacy", "Ollama"]

    body = FOCUS_TEMPLATES[variant].format(
        name=p["name"],
        price=p["formatted_price"],
        url=url,
        code=DISCOUNT_CODE,
    )
    post_message(body, tags=tags, product_id=p["id"], url=url)


# Keep the historical function name for cron jobs and external callers.
promote_random_product = promote_focus_product


def engage_community():
    """Like and optionally follow posts under AI/productivity hashtags."""
    if not engagement_due():
        return False
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

    summary = f"{interactions} interactions on #{tag}"
    log_promotion("bluesky_engage", None, None, summary)
    print(f"Done. {summary}")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bot/bluesky_bot.py [promote | engage | post <text>]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "promote":
        promote_focus_product()
    elif cmd == "engage":
        print("Automated unsolicited engagement is disabled; publish useful owned-account posts instead.")
    elif cmd == "post":
        text = " ".join(sys.argv[2:])
        if not text:
            sys.exit("Provide text.")
        post_message(text)
    else:
        print(f"Unknown: {cmd}")
        sys.exit(1)
