#!/usr/bin/env python3
"""
Bluesky Social Media Bot for Gumroad_AI
Allows agents to promote products autonomously.

Usage:
    python3 bot/bluesky_bot.py post "Your message here!"
    python3 bot/bluesky_bot.py promote  # Auto-selects a product and promotes it
"""

import os
import sys
import sqlite3
import random
try:
    from atproto import Client
except ImportError:
    print("❌ atproto package not installed. Run: pip3 install atproto")
    sys.exit(1)

ENV_PATH = os.path.join(os.path.dirname(__file__), "../.env")
DB_PATH = os.path.join(os.path.dirname(__file__), "../db/store.db")

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
    client.login(user, pw)
    return client

def post_message(text):
    client = get_client()
    print(f"📝 Posting: {text}")
    post = client.send_post(text)
    print(f"✅ Successfully posted to Bluesky! Post URI: {post.uri}")

def promote_random_product():
    if not os.path.exists(DB_PATH):
        print("❌ Database not found. Run: python3 db/sync.py")
        sys.exit(1)
        
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    # Get a published product that is properly priced (> €0.99)
    products = con.execute("SELECT name, formatted_price, short_url FROM products WHERE published=1 AND price_cents > 99").fetchall()
    con.close()
    
    if not products:
        print("❌ No properly priced published products found to promote. Need something > €0.99.")
        sys.exit(1)
        
    p = random.choice(products)
    url = p['short_url'] or "https://schephenk.gumroad.com"
    
    prompts = [
        f"Level up your workflow with '{p['name']}'! Available now for {p['formatted_price']}. Check it out here: {url}",
        f"Don't miss out on '{p['name']}'. Get it today for just {p['formatted_price']}! 🚀 {url}",
        f"Just published: '{p['name']}'. Only {p['formatted_price']}. Enhance your AI skills now! {url}",
        f"Unlock the full potential of AI with '{p['name']}'. Grab yours for {p['formatted_price']} 👉 {url}"
    ]
    
    text = random.choice(prompts)
    post_message(text)

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
