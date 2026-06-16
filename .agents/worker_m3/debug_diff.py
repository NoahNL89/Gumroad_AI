#!/usr/bin/env python3
import os
import json
import sqlite3

DRY_RUN_JSON_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/copy_dry_run.json"
DB_PATH = "/home/administrator/NewGitHub/GumRoad_AI/db/store.db"

with open(DRY_RUN_JSON_PATH, "r") as f:
    expected_products = json.load(f)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Check one mismatched product
prod = expected_products[6] # Consistent Character Genesis: Midjourney Mastery (2026 Edition)
prod_id = prod["id"]
cursor.execute("SELECT description FROM products WHERE id = ?", (prod_id,))
db_desc = cursor.fetchone()[0]

expected_desc = prod["optimized_description"]

def normalize_html(html_str):
    # Remove all whitespace characters to see if text and tags are identical, ignoring formatting
    return "".join(html_str.split())

norm_expected = normalize_html(expected_desc)
norm_db = normalize_html(db_desc)

print(f"Norm expected length (no whitespace): {len(norm_expected)}")
print(f"Norm db length (no whitespace): {len(norm_db)}")

if norm_expected != norm_db:
    print("Mismatched even without whitespace!")
    for idx, (c1, c2) in enumerate(zip(norm_expected, norm_db)):
        if c1 != c2:
            print(f"First diff at char index {idx}: expected {repr(c1)}, actual {repr(c2)}")
            print(f"Context expected: {repr(norm_expected[max(0, idx-20):idx+20])}")
            print(f"Context actual:   {repr(norm_db[max(0, idx-20):idx+20])}")
            break
else:
    print("✅ Matched when ignoring all whitespace!")


conn.close()
