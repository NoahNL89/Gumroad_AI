import json

with open("/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/extracted_products.json", "r") as f:
    products = json.load(f)

for idx in [0, 16]:  # Index 0 is product 1, Index 16 is product 17
    p = products[idx]
    print(f"Product: {p['name']}")
    print("Description:")
    print(p['description'])
    print("=" * 80)
