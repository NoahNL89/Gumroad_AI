#!/usr/bin/env python3
"""
Gumroad File Downloader
Downloads all files attached to all published products into a local directory.
"""

import os
import sys
import sqlite3
import urllib.request
import urllib.parse
import json
import re

ENV_PATH = os.path.join(os.path.dirname(__file__), "../.env")
DB_PATH = os.path.join(os.path.dirname(__file__), "../db/store.db")
DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), "../downloads")

def load_token():
    token = os.environ.get("GUMROAD_ACCESS_TOKEN", "")
    if not token and os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GUMROAD_ACCESS_TOKEN=") and not line.startswith("#"):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not token:
        print("❌  GUMROAD_ACCESS_TOKEN not set in .env")
        sys.exit(1)
    return token

TOKEN = load_token()

def sanitize_filename(name):
    """Remove invalid characters from filenames and folder names"""
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def download_product_files():
    if not os.path.exists(DB_PATH):
        print("❌ Database not found. Run db/sync.py first.")
        sys.exit(1)
        
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    products = con.execute("SELECT id, name FROM products WHERE published=1").fetchall()
    con.close()
    
    print(f"📥 Starting download process for {len(products)} products...\n")
    
    total_files = 0
    
    for prod in products:
        prod_id = prod["id"]
        prod_name = sanitize_filename(prod["name"])
        prod_dir = os.path.join(DOWNLOAD_DIR, prod_name)
        
        # Call API to get files
        url = f"https://api.gumroad.com/v2/products/{prod_id}?access_token={TOKEN}"
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read())
        except Exception as e:
            print(f"⚠️ Failed to fetch product {prod_name}: {e}")
            continue
            
        files = data.get("product", {}).get("files", [])
        if not files:
            continue
            
        os.makedirs(prod_dir, exist_ok=True)
        print(f"📂 {prod_name} ({len(files)} files)")
        
        for f in files:
            file_url = f.get("url")
            if not file_url:
                continue
                
            # If name is null, we try to extract it from the URL or fallback to ID
            file_name = f.get("name")
            if not file_name:
                # Try to extract from URL path before query params
                path = urllib.parse.urlparse(file_url).path
                basename = os.path.basename(path)
                if basename:
                    file_name = basename
                else:
                    file_name = f"{f.get('id', 'file')}.{f.get('filetype', 'bin')}"
            
            file_name = sanitize_filename(file_name)
            save_path = os.path.join(prod_dir, file_name)
            
            # Download file if it doesn't exist
            if not os.path.exists(save_path):
                print(f"   Downloading: {file_name} ...", end=" ", flush=True)
                try:
                    urllib.request.urlretrieve(file_url, save_path)
                    print("✅")
                    total_files += 1
                except Exception as e:
                    print(f"❌ Error: {e}")
            else:
                print(f"   Skipping (already exists): {file_name}")
                
    print(f"\n🎉 Finished! Downloaded {total_files} new files to {DOWNLOAD_DIR}/")

if __name__ == "__main__":
    download_product_files()
