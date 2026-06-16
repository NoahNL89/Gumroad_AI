import json

with open("/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/extracted_products.json", "r") as f:
    products = json.load(f)

for idx, p in enumerate(products):
    if "[NAME]" in p['description'] or "Status:" in p['description']:
        print(f"Index {idx+1}: {p['name']} has placeholder content.")
