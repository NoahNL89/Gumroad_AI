import os
import sqlite3
import requests
import difflib

# Configuration
DB_PATH = "db/store.db"
THUMBNAIL_DIR = "assets/thumbnails"
ENV_PATH = ".env"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/NoahNL89/Gumroad_AI/main/assets/thumbnails"

def load_token():
    token = os.environ.get("GUMROAD_ACCESS_TOKEN", "")
    if not token and os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GUMROAD_ACCESS_TOKEN=") and not line.startswith("#"):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return token

def upload_thumbnail(product_id, product_name, filename, token):
    url = f"https://api.gumroad.com/v2/products/{product_id}/thumbnail"
    raw_url = f"{GITHUB_RAW_BASE}/{filename}"
    
    print(f"Uploading for '{product_name}' -> {filename}")
    response = requests.post(
        url,
        data={
            "access_token": token,
            "url": raw_url
        }
    )
    if response.status_code == 200:
        print("  ✅ Success")
    else:
        print(f"  ❌ Failed: {response.text}")

def main():
    token = load_token()
    if not token:
        print("Error: Missing GUMROAD_ACCESS_TOKEN")
        return
        
    # Get all products
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM products")
    products = {row[1]: row[0] for row in cursor.fetchall()}
    conn.close()
    
    # Get all thumbnails
    if not os.path.exists(THUMBNAIL_DIR):
        print(f"Directory {THUMBNAIL_DIR} not found.")
        return
        
    files = [f for f in os.listdir(THUMBNAIL_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # Simple mapping
    for f in files:
        if "schep_digital" in f or "test_thumbnail" in f:
            continue
            
        # Clean filename for matching
        clean_name = f.replace("_", " ").replace(".png", "").replace(".jpg", "").lower()
        # Remove timestamps
        clean_name = " ".join([w for w in clean_name.split() if not w.isdigit()])
        
        # Match with product names
        product_names = list(products.keys())
        matches = difflib.get_close_matches(clean_name, [p.lower() for p in product_names], n=1, cutoff=0.3)
        
        if matches:
            matched_lower = matches[0]
            # Find original case
            original_name = next(p for p in product_names if p.lower() == matched_lower)
            product_id = products[original_name]
            
            upload_thumbnail(product_id, original_name, f, token)
        else:
            print(f"⚠️  Could not find a match for file: {f}")

if __name__ == "__main__":
    main()
