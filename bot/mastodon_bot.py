#!/usr/bin/env python3
"""
Mastodon Social Media Bot for Gumroad_AI
Promotes products autonomously with rate-limiting and 80/20 value-first principles.

Usage:
    python3 bot/mastodon_bot.py post "Your message here!"
    python3 bot/mastodon_bot.py promote  # Auto-selects a product and promotes it
"""

import os
import sys
import sqlite3
import random
from datetime import datetime, timezone, timedelta
try:
    from mastodon import Mastodon
except ImportError:
    print("❌ Mastodon.py package not installed. Run: pip3 install Mastodon.py")
    sys.exit(1)

ENV_PATH = os.path.join(os.path.dirname(__file__), "../.env")
DB_PATH = os.path.join(os.path.dirname(__file__), "../db/store.db")
BOT_DIR = os.path.dirname(__file__)

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
    access_token = os.environ.get("MASTODON_ACCESS_TOKEN")
    instance = os.environ.get("MASTODON_INSTANCE", "https://mastodon.social")
    
    if not access_token:
        print("❌ MASTODON_ACCESS_TOKEN not set in .env")
        print("   Mastodon 4.4.0+ requires Access Tokens instead of username/password.")
        print("   Get one at: Preferences -> Development -> New Application")
        sys.exit(1)
    
    client = Mastodon(access_token=access_token, api_base_url=instance)
    return client

def log_promotion(platform, product_id, url, content):
    """Log the promotion to the SQLite DB."""
    if not os.path.exists(DB_PATH):
        return
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        INSERT INTO promotions (platform, product_id, url, content, posted_at)
        VALUES (?, ?, ?, ?, ?)
    """, (platform, product_id, url, content, datetime.now(timezone.utc).isoformat()))
    con.commit()
    con.close()

def check_rate_limits():
    """Check if we have exceeded our daily posting limit (Max 3/day)."""
    if not os.path.exists(DB_PATH):
        return True # Can't check
    
    con = sqlite3.connect(DB_PATH)
    twenty_four_hours_ago = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    count = con.execute(
        "SELECT COUNT(*) FROM promotions WHERE platform='mastodon' AND posted_at >= ?", 
        (twenty_four_hours_ago,)
    ).fetchone()[0]
    con.close()
    
    if count >= MAX_POSTS_PER_DAY:
        print(f"⚠️ RATE LIMIT REACHED: Already posted {count} times on Mastodon in the last 24 hours.")
        print("💡 Best practice: Mastodon favors authenticity over spam. We will pause posting.")
        return False
    return True

def post_message(text, product_id=None, url=None):
    if not check_rate_limits():
        sys.exit(0)
        
    client = get_client()
    print(f"📝 Posting to Mastodon:\n{text}\n")
    # Mastodon post creation
    post = client.toot(text)
    
    log_promotion("mastodon", product_id, url, text)
    print(f"✅ Successfully posted to Mastodon! Post URL: {post['url']}")

def promote_random_product():
    if not os.path.exists(DB_PATH):
        print("❌ Database not found. Run: python3 db/sync.py")
        sys.exit(1)
        
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    # Get a published product that is properly priced (> €0.99)
    products = con.execute("SELECT id, name, formatted_price, short_url FROM products WHERE published=1 AND price_cents > 99").fetchall()
    
    # Let's avoid promoting the EXACT same product we promoted last time on Mastodon
    last_promo = con.execute("SELECT product_id FROM promotions WHERE platform='mastodon' ORDER BY posted_at DESC LIMIT 1").fetchone()
    con.close()
    
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
        print("Usage: python3 bot/mastodon_bot.py [post <text> | promote]")
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
        print("Usage: python3 bot/mastodon_bot.py [post <text> | promote]")
        sys.exit(1)
