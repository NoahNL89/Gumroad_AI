import json
import os

JSON_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/copy_dry_run.json"

def main():
    if not os.path.exists(JSON_PATH):
        print(f"❌ Error: {JSON_PATH} not found.")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Total entries: {len(data)}")
    for idx, p in enumerate(data):
        print(f"Product {idx+1}: {p['name']}")
        # Verify structure
        for key in ["id", "name", "price", "original_description", "optimized_description", "length_diff_pct", "content_similarity"]:
            if key not in p:
                print(f"  ❌ Missing key: {key}")
                return
        
        # Verify optimized description contents
        opt = p["optimized_description"]
        if "<strong>" not in opt or "Challenge" not in opt or "Breakthrough" not in opt or "What's Inside" not in opt or "Who Is This For" not in opt:
            print("  ❌ Missing required sections in optimized description")
            return

    print("✅ All checks passed! copy_dry_run.json is valid.")

if __name__ == "__main__":
    main()
