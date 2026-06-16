import sqlite3
import os
import glob

db_path = "/home/administrator/NewGitHub/GumRoad_AI/db/store.db"
downloads_dir = "/home/administrator/NewGitHub/GumRoad_AI/downloads"

def main():
    if not os.path.exists(db_path):
        print(f"Error: Database {db_path} does not exist yet.")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, name, price_cents, formatted_price, description FROM products ORDER BY name")
        products = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}")
        conn.close()
        return

    print(f"Found {len(products)} products in the database.\n")

    # Get list of subdirectories in downloads/
    if os.path.exists(downloads_dir):
        download_dirs = [d for d in os.listdir(downloads_dir) if os.path.isdir(os.path.join(downloads_dir, d))]
    else:
        download_dirs = []

    print(f"{'ID':<15} | {'Name':<50} | {'Price':<10} | {'Desc Len':<8} | {'Cover Image Path'}")
    print("-" * 110)

    for p in products:
        p_id = p['id']
        name = p['name']
        price = p['formatted_price'] if p['formatted_price'] else f"€{p['price_cents']/100:.2f}"
        desc = p['description'] or ""
        desc_len = len(desc)

        # Match directory name in downloads
        # Clean name slightly to match folder names (sometimes folder names might not match exactly, so we do case-insensitive or exact check)
        matched_dir = None
        for d in download_dirs:
            if d.lower() == name.lower():
                matched_dir = d
                break
        
        # If no exact match, try partial match or cleaning
        if not matched_dir:
            cleaned_name = name.replace(":", "").replace("/", "").replace("?", "").strip()
            for d in download_dirs:
                if d.lower() == cleaned_name.lower():
                    matched_dir = d
                    break
        
        cover_path = "No matching folder"
        if matched_dir:
            dir_path = os.path.join(downloads_dir, matched_dir)
            files = os.listdir(dir_path)
            covers = [f for f in files if "cover" in f.lower()]
            if covers:
                cover_path = ", ".join([os.path.join("downloads", matched_dir, c) for c in covers])
            else:
                cover_path = f"Folder found ({matched_dir}), but no cover file"
        else:
            # Maybe search by partial match
            partial_matches = []
            for d in download_dirs:
                # check if first 15 chars match
                if d[:15].lower() == name[:15].lower():
                    partial_matches.append(d)
            if partial_matches:
                matched_dir = partial_matches[0]
                dir_path = os.path.join(downloads_dir, matched_dir)
                files = os.listdir(dir_path)
                covers = [f for f in files if "cover" in f.lower()]
                if covers:
                    cover_path = ", ".join([os.path.join("downloads", matched_dir, c) for c in covers])
                else:
                    cover_path = f"Folder found ({matched_dir}), but no cover file"

        print(f"{p_id:<15} | {name[:50]:<50} | {price:<10} | {desc_len:<8} | {cover_path}")

    conn.close()

if __name__ == "__main__":
    main()
