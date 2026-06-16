import sqlite3
import os

DB_PATH = "/home/administrator/NewGitHub/GumRoad_AI/db/store.db"

def main():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, description, price_cents, formatted_price FROM products")
    rows = cursor.fetchall()

    print(f"Extracted {len(rows)} products:")
    print("=" * 80)
    for row in rows:
        price = row["price_cents"] / 100.0 if row["price_cents"] is not None else 0.0
        print(f"ID: {row['id']}")
        print(f"Name: {row['name']}")
        print(f"Price: {price} EUR ({row['formatted_price']})")
        desc = row["description"] or ""
        print(f"Description Length: {len(desc)} characters")
        print(f"Description Snippet:\n{desc[:100]}...")
        print("-" * 80)

    conn.close()

if __name__ == "__main__":
    main()
