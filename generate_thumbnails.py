import urllib.request
import urllib.parse
import os
import sqlite3
import re

def get_products():
    conn = sqlite3.connect('db/store.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM products')
    products = []
    for row in cursor.fetchall():
        if row['name'] not in ["Consistent Character Genesis", "SEO Checklist for Bloggers - 2026 Edition"]:
            products.append(row['name'])
    conn.close()
    return products

products = get_products()
print(f"Found {len(products)} products")

os.makedirs('assets/thumbnails', exist_ok=True)

for name in products:
    prompt = f"A professional 1:1 square thumbnail for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Dark mode, very wide aspect ratio, high resolution. Concept: {name}"
    url_encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{url_encoded_prompt}?width=1024&height=1024&nologo=true"
    
    # create safe filename
    safe_name = "".join([c if c.isalnum() else "_" for c in name]).strip("_").lower()
    safe_name = re.sub(r'_+', '_', safe_name)
    file_path = f"assets/thumbnails/{safe_name}.jpg"
    
    print(f"Generating image for {name}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Saved to {file_path}")
    except Exception as e:
        print(f"Error for {name}: {e}")

