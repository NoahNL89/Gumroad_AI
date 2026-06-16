import json

with open("/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/extracted_products.json", "r") as f:
    products = json.load(f)

with open("/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/original_descriptions.txt", "w", encoding="utf-8") as f:
    for idx, p in enumerate(products):
        f.write(f"=== {idx+1}. ID: {p['id']} ===\n")
        f.write(f"Name: {p['name']}\n")
        f.write(f"Price: {p['price']} EUR\n")
        f.write(f"Description:\n{p['description']}\n")
        f.write("=" * 80 + "\n\n")

print("Dumped descriptions to /home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/original_descriptions.txt")
