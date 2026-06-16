#!/usr/bin/env python3
"""
Mastodon Social Media Bot for Gumroad_AI
Promotes products autonomously and acts as an engagement engine.

Research-backed best practices applied:
1. COMMUNITY ENGAGEMENT: Mastodon has no algorithm. Growth comes from interacting, boosting, and following.
2. MAX 3 POSTS PER DAY: Prevents spamming and respects instance culture.
3. 80/20 VALUE RULE: We mix hard product sales with value-driven advice.
4. DATABASE TRACKING: All posts are logged to `store.db`.

Usage:
    python3 bot/mastodon_bot.py post "Your message here!"
    python3 bot/mastodon_bot.py promote  # Auto-selects a product and promotes it
    python3 bot/mastodon_bot.py engage   # Follows, likes, and boosts relevant niche tags
"""

import os
import sys
import sqlite3
import random
import time
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
    post = client.toot(text)
    
    log_promotion("mastodon", product_id, url, text)
    print(f"✅ Successfully posted to Mastodon! Post URL: {post['url']}")

def promote_random_product():
    if not os.path.exists(DB_PATH):
        print("❌ Database not found. Run: python3 db/sync.py")
        sys.exit(1)
        
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    products = con.execute("SELECT id, name, formatted_price, short_url FROM products WHERE published=1 AND price_cents > 99").fetchall()
    last_promo = con.execute("SELECT product_id FROM promotions WHERE platform='mastodon' ORDER BY posted_at DESC LIMIT 1").fetchone()
    con.close()
    
    if not products:
        print("❌ No properly priced published products found to promote.")
        sys.exit(1)
        
    if last_promo and len(products) > 1:
        products = [p for p in products if p['id'] != last_promo['product_id']]
        
    p = random.choice(products)
    url = p['short_url'] or "https://schephenk.gumroad.com"
    
    is_value_post = random.random() < 0.70 # 70% chance of being a "value" / educational hook
    
    if is_value_post:
        prompts = [
            f"💡 Quick tip for creators in 2026: Authenticity + AI is the winning combo. Let the AI handle the boilerplate, you handle the vision. \n\nIf you want to master this workflow, check out my guide on '{p['name']}': {url} #AI #CreatorEconomy",
            f"Building an audience takes time, but the right systems save you hundreds of hours. I distilled my workflow into '{p['name']}'. \n\nLearn the exact blueprint here: {url} #Productivity #Solopreneur",
            f"Stop doing repetitive digital tasks manually. 🛑 \n\n'{p['name']}' is designed to help you scale your output without burning out. \n\nGrab it for {p['formatted_price']}: {url} #DigitalMarketing",
            f"The best digital products solve one specific problem perfectly. That's what I aimed for with '{p['name']}'. \n\nSee how it can help your workflow today 👉 {url} #SideHustle"
        ]
    else:
        prompts = [
            f"🔥 Level up your workflow with '{p['name']}'! Available now for {p['formatted_price']}. Instant access here: {url} #Productivity",
            f"Don't miss out on '{p['name']}'. Get it today for just {p['formatted_price']}! 🚀 {url} #DigitalProducts",
            f"Just published: '{p['name']}'. Only {p['formatted_price']}. Enhance your AI skills now! {url} #AI"
        ]
    
    text = random.choice(prompts)
    post_message(text, product_id=p['id'], url=url)

def engage_community():
    """Autonomously interact with relevant hashtags to build organic reach."""
    client = get_client()
    hashtags = ["AI", "Productivity", "CreatorEconomy", "Solopreneur", "DigitalMarketing", "ContentCreator", "SideHustle"]
    
    tag = random.choice(hashtags)
    print(f"🔍 Searching Mastodon for recent posts with #{tag}...")
    
    try:
        results = client.timeline_hashtag(tag, limit=8)
    except Exception as e:
        print(f"❌ Error fetching timeline: {e}")
        sys.exit(1)
        
    interactions = 0
    for status in results:
        # Avoid replying/interacting with our own posts
        if status.account.id == client.me().id:
            continue
            
        try:
            # 1. Favorite the post (High probability)
            if not status.favourited:
                client.status_favourite(status.id)
                print(f"❤️ Favorited post by @{status.account.acct}")
                interactions += 1
                
            # 2. Reblog/Boost the post (Medium probability, adds huge value)
            if not status.reblogged and random.random() < 0.3:
                client.status_reblog(status.id)
                print(f"🔁 Boosted post by @{status.account.acct}")
                interactions += 1
                
            # 3. Follow the user (Low probability)
            # Mastodon API handles already-followed seamlessly
            if random.random() < 0.4:
                client.account_follow(status.account.id)
                print(f"👤 Followed @{status.account.acct}")
                interactions += 1
                
            time.sleep(1) # Be polite to the API
        except Exception as e:
            print(f"⚠️ Could not interact with post {status.id}: {e}")
            
    print(f"\n✅ Engagement complete! Total interactions generated for #{tag}: {interactions}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bot/mastodon_bot.py [post <text> | promote | engage]")
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
    elif cmd == "engage":
        engage_community()
    else:
        print(f"Unknown command: {cmd}")
        print("Usage: python3 bot/mastodon_bot.py [post <text> | promote | engage]")
        sys.exit(1)
