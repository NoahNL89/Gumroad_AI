#!/usr/bin/env python3
"""
Bluesky Social Media Bot for Gumroad_AI
Promotes products autonomously with rate-limiting and 80/20 value-first principles.

Research-backed best practices applied:
1. MAX 3 POSTS PER DAY: Bluesky rewards authentic engagement over volume.
2. 80/20 VALUE RULE: We mix hard product sales with value-driven advice.
3. DATABASE TRACKING: All posts are logged to `store.db` to prevent spamming.

Usage:
    python3 bot/bluesky_bot.py post "Your message here!"
    python3 bot/bluesky_bot.py promote  # Auto-selects a product and promotes it
"""

import os
import sys
import sqlite3
import random
from datetime import datetime, timezone, timedelta
try:
    from atproto import Client
except ImportError:
    print("❌ atproto package not installed. Run: pip3 install atproto")
    sys.exit(1)

ENV_PATH = os.path.join(os.path.dirname(__file__), "../.env")
DB_PATH = os.path.join(os.path.dirname(__file__), "../db/store.db")

MAX_POSTS_PER_DAY = 3

def load_env():
    """Load credentials from .env file"""
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "=" in line:
                        k, v = line.split("=", 1)
                        os.environ[k.strip()] = v.strip().strip('"').strip("'")

def get_client():
    load_env()
    user = os.environ.get("BLUESKY_USERNAME")
    pw = os.environ.get("BLUESKY_PASSWORD")
    if not user or not pw:
        print("❌ BLUESKY_USERNAME or BLUESKY_PASSWORD not set in .env")
        sys.exit(1)
    
    print(f"🔄 Logging in to Bluesky as {user}...")
    client = Client()
    try:
        client.login(user, pw)
    except Exception as e:
        print(f"❌ Failed to log in to Bluesky: {e}")
        sys.exit(1)
    return client

def log_promotion(platform, product_id, url, content):
    """Log the promotion to the SQLite DB."""
    if not os.path.exists(DB_PATH):
        print(f"⚠️ Warning: Database not found at {DB_PATH}. Promotion not logged.")
        return
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
            INSERT INTO promotions (platform, product_id, url, content, posted_at)
            VALUES (?, ?, ?, ?, ?)
        """, (platform, product_id, url, content, datetime.now(timezone.utc).isoformat()))
        con.commit()

def check_rate_limits():
    """Check if we have exceeded our daily posting limit (Max 3/day)."""
    if not os.path.exists(DB_PATH):
        print(f"⚠️ Warning: Database not found at {DB_PATH}. Refusing to post (fail-closed).")
        return False
    
    with sqlite3.connect(DB_PATH) as con:
        twenty_four_hours_ago = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        count = con.execute(
            "SELECT COUNT(*) FROM promotions WHERE platform='bluesky' AND posted_at >= ?", 
            (twenty_four_hours_ago,)
        ).fetchone()[0]
    
    if count >= MAX_POSTS_PER_DAY:
        print(f"⚠️ RATE LIMIT REACHED: Already posted {count} times in the last 24 hours.")
        print("💡 Best practice: Bluesky favors authenticity over spam. We will pause posting.")
        return False
    return True

BLUESKY_CHAR_LIMIT = 300

def post_message(text, product_id=None, url=None):
    if not check_rate_limits():
        sys.exit(0)
    
    # Enforce Bluesky character limit (300 chars)
    if len(text) > BLUESKY_CHAR_LIMIT:
        suffix = f"... {url}" if url else "..."
        text = text[:BLUESKY_CHAR_LIMIT - len(suffix)] + suffix
        print(f"⚠️ Text truncated to {BLUESKY_CHAR_LIMIT} characters.")
        
    client = get_client()
    print(f"📝 Posting:\n{text}\n")
    try:
        post = client.send_post(text)
    except Exception as e:
        print(f"❌ Failed to post to Bluesky: {e}")
        sys.exit(1)
    
    log_promotion("bluesky", product_id, url, text)
    print(f"✅ Successfully posted to Bluesky! Post URI: {post.uri}")

def promote_random_product():
    if not os.path.exists(DB_PATH):
        print("❌ Database not found. Run: python3 db/sync.py")
        sys.exit(1)
        
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        # Get a published product that is properly priced (> €0.99)
        products = con.execute("SELECT id, name, formatted_price, short_url FROM products WHERE published=1 AND price_cents > 99").fetchall()
    
        # Let's avoid promoting the EXACT same product we promoted last time if possible
        last_promo = con.execute("SELECT product_id FROM promotions WHERE platform='bluesky' ORDER BY posted_at DESC LIMIT 1").fetchone()
    
    if not products:
        print("❌ No properly priced published products found to promote.")
        sys.exit(1)
        
    # Exclude last promoted product if we have multiple choices
    if last_promo and len(products) > 1:
        products = [p for p in products if p['id'] != last_promo['product_id']]
        
    p = random.choice(products)
    url = p['short_url'] or "https://schephenk.gumroad.com"
    
    # 80/20 Rule: Sometimes share value/tips instead of a hard sell
    is_value_post = random.random() < 0.70 # 70% chance of being a "value" / educational hook
    
    if is_value_post:
        prompts = [
            f"💡 Quick tip for creators in 2026: Authenticity + AI is the winning combo. Let the AI handle the boilerplate, you handle the vision. \n\nIf you want to master this workflow, check out my guide on '{p['name']}': {url}",
            f"Building an audience takes time, but the right systems save you hundreds of hours. I distilled my workflow into '{p['name']}'. \n\nLearn the exact blueprint here: {url}",
            f"Stop doing repetitive digital tasks manually. 🛑 \n\n'{p['name']}' is designed to help you scale your output without burning out. \n\nGrab it for {p['formatted_price']}: {url}",
            f"The best digital products solve one specific problem perfectly. That's what I aimed for with '{p['name']}'. \n\nSee how it can help your workflow today 👉 {url}"
        ]
    else:
        # Direct hard sell
        prompts = [
            f"🔥 Level up your workflow with '{p['name']}'! Available now for {p['formatted_price']}. Instant access here: {url}",
            f"Don't miss out on '{p['name']}'. Get it today for just {p['formatted_price']}! 🚀 {url}",
            f"Just published: '{p['name']}'. Only {p['formatted_price']}. Enhance your AI skills now! {url}"
        ]
    
    text = random.choice(prompts)
    post_message(text, product_id=p['id'], url=url)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bot/bluesky_bot.py [post <text> | promote]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "post":
        text = " ".join(sys.argv[2:])
        if not text:
            print("❌ Please provide text to post.")
            sys.exit(1)
        post_message(text)
    elif cmd == "promote":
        promote_random_product()
    else:
        print(f"Unknown command: {cmd}")
        print("Usage: python3 bot/bluesky_bot.py [post <text> | promote]")
        sys.exit(1)
