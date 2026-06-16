import json

with open("/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/extracted_products.json", "r") as f:
    products = json.load(f)

print(f"Total products: {len(products)}")
for idx, p in enumerate(products):
    print(f"{idx+1}. ID: {p['id']} | Name: {p['name']} | Price: {p['price']} EUR | Desc length: {len(p['description'])}")
