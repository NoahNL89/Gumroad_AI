#!/usr/bin/env python3
import os
import sys
import json
import sqlite3

DRY_RUN_JSON_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/copy_dry_run.json"
DB_PATH = "/home/administrator/NewGitHub/GumRoad_AI/db/store.db"

def main():
    if not os.path.exists(DRY_RUN_JSON_PATH):
        print(f"❌ copy_dry_run.json not found at {DRY_RUN_JSON_PATH}")
        sys.exit(1)
        
    if not os.path.exists(DB_PATH):
        print(f"❌ store.db not found at {DB_PATH}")
        sys.exit(1)
        
    with open(DRY_RUN_JSON_PATH, "r") as f:
        expected_products = json.load(f)
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print(f"Verifying {len(expected_products)} products against store.db...")
    
    mismatches = []
    matches_count = 0
    not_found_count = 0
    
    for i, prod in enumerate(expected_products, 1):
        prod_id = prod.get("id")
        name = prod.get("name")
        expected_desc = prod.get("optimized_description")
        
        # Query db
        cursor.execute("SELECT name, description, price_cents FROM products WHERE id = ?", (prod_id,))
        row = cursor.fetchone()
        
        if not row:
            print(f"❌ Product not found in DB: {name} (ID: {prod_id})")
            not_found_count += 1
            mismatches.append({
                "id": prod_id,
                "name": name,
                "reason": "Not found in database"
            })
            continue
            
        db_name, db_desc, db_price_cents = row
        
        # Normalize descriptions to avoid false mismatches from line endings or whitespace formatting introduced by Gumroad's HTML cleaner
        norm_expected = "".join(expected_desc.split())
        norm_db = "".join((db_desc or "").split())
        
        if norm_expected == norm_db:
            matches_count += 1
        else:
            mismatches.append({
                "id": prod_id,
                "name": name,
                "expected": expected_desc,
                "actual": db_desc,
                "reason": "Description content mismatch"
            })
            print(f"❌ Description mismatch for {name} (ID: {prod_id})")
            # print first 100 chars of difference
            print(f"   Expected: {repr(norm_expected[:100])}")
            print(f"   Actual:   {repr(norm_db[:100])}")
            
    conn.close()
    
    print("\nVerification Summary:")
    print(f"  Total checked: {len(expected_products)}")
    print(f"  Matches: {matches_count}")
    print(f"  Mismatches: {len(mismatches)}")
    print(f"  Not Found: {not_found_count}")
    
    if mismatches:
        print("\n❌ Verification FAILED!")
        sys.exit(1)
    else:
        print("\n✅ Verification PASSED! All descriptions in store.db match copy_dry_run.json.")
        sys.exit(0)

if __name__ == "__main__":
    main()
