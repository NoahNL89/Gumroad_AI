#!/usr/bin/env python3
import os
import sys
import json
import time
import urllib.request
import urllib.parse

# Configuration
DRY_RUN_JSON_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/copy_dry_run.json"
ENV_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.env"
API_BASE = "https://api.gumroad.com/v2"

def load_token():
    token = os.environ.get("GUMROAD_ACCESS_TOKEN", "")
    if not token and os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GUMROAD_ACCESS_TOKEN=") and not line.startswith("#"):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not token:
        print("❌ GUMROAD_ACCESS_TOKEN not found in env or .env file.")
        sys.exit(1)
    return token

def api_put(product_id, data, token):
    data["access_token"] = token
    encoded = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(f"{API_BASE}/products/{product_id}", data=encoded, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            res_data = json.loads(r.read())
            # Gumroad API returns {"success": true, "product": {...}} on success
            return res_data
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    token = load_token()
    
    if not os.path.exists(DRY_RUN_JSON_PATH):
        print(f"❌ copy_dry_run.json not found at {DRY_RUN_JSON_PATH}")
        sys.exit(1)
        
    with open(DRY_RUN_JSON_PATH, "r") as f:
        products = json.load(f)
        
    print(f"Loaded {len(products)} products from copy_dry_run.json.")
    
    results = []
    success_count = 0
    failure_count = 0
    
    for i, prod in enumerate(products, 1):
        prod_id = prod.get("id")
        name = prod.get("name")
        optimized_desc = prod.get("optimized_description")
        price = prod.get("price")
        
        print(f"[{i}/{len(products)}] Updating: {name} (ID: {prod_id}) ...")
        
        payload = {"description": optimized_desc}
        res = api_put(prod_id, payload, token)
        
        if res.get("success"):
            print(f"  ✅ Updated successfully")
            success_count += 1
            results.append({
                "id": prod_id,
                "name": name,
                "price": price,
                "status": "Success",
                "error": None
            })
        else:
            err_msg = res.get("error") or res.get("message") or str(res)
            print(f"  ❌ Failed: {err_msg}")
            failure_count += 1
            results.append({
                "id": prod_id,
                "name": name,
                "price": price,
                "status": "Failed",
                "error": err_msg
            })
            
        # Rate limit handling: small sleep delay between calls (e.g. 0.3s)
        time.sleep(0.3)
        
    print(f"\nUpdate completed: {success_count} success, {failure_count} failures.")
    
    # Save the results to publish_results.json
    results_path = "/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m3/publish_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results log written to {results_path}")

if __name__ == "__main__":
    main()
