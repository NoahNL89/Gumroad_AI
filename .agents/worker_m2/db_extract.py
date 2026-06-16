import sqlite3
import json
import os

DB_PATH = "/home/administrator/NewGitHub/GumRoad_AI/db/store.db"
OUTPUT_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/extracted_products.json"

def main():
    if not os.path.exists(DB_PATH):
        print(f"Error: Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, description, price_cents FROM products")
    rows = cursor.fetchall()

    products = []
    for r in rows:
        price = (r["price_cents"] or 0) / 100.0
        products.append({
            "id": r["id"],
            "name": r["name"],
            "description": r["description"] or "",
            "price": price
        })

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    print(f"Successfully extracted {len(products)} products and saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
