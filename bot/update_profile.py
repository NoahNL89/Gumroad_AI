#!/usr/bin/env python3
"""
Mastodon Profile Customization Script
Updates the Display Name, Bio, Avatar, Header, and Featured Tags via API.
"""

import os
import sys
try:
    from mastodon import Mastodon
except ImportError:
    print("❌ Mastodon.py not installed.")
    sys.exit(1)

ENV_PATH = os.path.join(os.path.dirname(__file__), "../.env")

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

def main():
    load_env()
    access_token = os.environ.get("MASTODON_ACCESS_TOKEN")
    instance = os.environ.get("MASTODON_INSTANCE", "https://mastodon.social")
    
    if not access_token:
        print("❌ MASTODON_ACCESS_TOKEN not set in .env")
        sys.exit(1)
        
    client = Mastodon(access_token=access_token, api_base_url=instance)
    
    # Paths to generated assets
    avatar_path = "/home/administrator/.gemini/antigravity-cli/brain/7c2d4a27-ec20-4515-bef3-baf746486a36/schep_digital_avatar_1781608169154.png"
    header_path = "/home/administrator/.gemini/antigravity-cli/brain/7c2d4a27-ec20-4515-bef3-baf746486a36/schep_digital_banner_1781608180562.png"
    
    display_name = "Schep Digital | AI & Tools"
    bio = (
        "Empowering creators with AI tools, templates, and productivity systems. "
        "Your unfair advantage in the digital economy. 🚀\n\n"
        "Store: https://schephenk.gumroad.com"
    )
    
    fields = [
        ("Store", "https://schephenk.gumroad.com"),
        ("Focus", "AI & Productivity"),
        ("Tools", "Templates & Automation")
    ]
    
    print("🔄 Updating profile credentials...")
    try:
        client.account_update_credentials(
            display_name=display_name,
            note=bio,
            avatar=avatar_path if os.path.exists(avatar_path) else None,
            header=header_path if os.path.exists(header_path) else None,
            fields=fields
        )
        print("✅ Profile Bio, Avatar, and Header updated successfully!")
    except Exception as e:
        print(f"❌ Failed to update profile: {e}")
        
    # Set featured tags
    tags = ["AI", "Productivity", "CreatorEconomy"]
    print("🔄 Setting featured tags...")
    for tag in tags:
        try:
            client.featured_tag_create(tag)
            print(f"✅ Added featured tag: #{tag}")
        except Exception as e:
            # Might fail if already exists or not supported
            print(f"⚠️ Could not add featured tag #{tag}: {e}")

if __name__ == "__main__":
    main()
