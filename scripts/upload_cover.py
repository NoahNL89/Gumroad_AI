#!/usr/bin/env python3
"""
Gumroad Cover Uploader
Uploads a local image file as the new cover (preview) for a Gumroad product via API.

Usage:
    python3 scripts/upload_cover.py <product_id> <image_path>
"""

import os
import sys
import requests
import json

ENV_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.env"

def load_token():
    token = os.environ.get("GUMROAD_ACCESS_TOKEN", "")
    if not token and os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GUMROAD_ACCESS_TOKEN=") and not line.startswith("#"):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    return token

def upload_cover(product_id, image_path):
    token = load_token()
    if not token:
        print("❌ GUMROAD_ACCESS_TOKEN not found.")
        sys.exit(1)

    if not os.path.exists(image_path):
        print(f"❌ Image not found at: {image_path}")
        sys.exit(1)
        
    url = f"https://api.gumroad.com/v2/products/{product_id}"
    
    print(f"📤 Uploading {os.path.basename(image_path)} to product {product_id}...")
    
    with open(image_path, "rb") as f:
        # Determine content type based on extension
        ext = os.path.splitext(image_path)[1].lower()
        content_type = "image/png" if ext == ".png" else "image/jpeg"
        
        files = {"preview_url": (os.path.basename(image_path), f, content_type)}
        data = {"access_token": token}
        
        response = requests.put(url, data=data, files=files)
        
        if response.status_code == 200:
            res_data = response.json()
            if res_data.get("success"):
                new_url = res_data.get("product", {}).get("preview_url")
                print(f"✅ Successfully updated cover!")
                print(f"🔗 New Cover URL: {new_url}")
            else:
                print(f"❌ API returned success false: {res_data}")
        else:
            print(f"❌ API Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 scripts/upload_cover.py <product_id> <image_path>")
        sys.exit(1)
        
    upload_cover(sys.argv[1], sys.argv[2])
