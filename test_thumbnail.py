import os
import sys
import requests

ENV_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.env"

def load_token():
    token = os.environ.get("GUMROAD_ACCESS_TOKEN", "")
    if not token and os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GUMROAD_ACCESS_TOKEN=") and not line.startswith("#"):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
    return token

def main():
    token = load_token()
    # Let's test on SEO Checklist: ROGBErC6NlBMaZBrUR3HyQ==
    product_id = "ROGBErC6NlBMaZBrUR3HyQ=="
    # Provide the exact path given by generate_image
    image_path = sys.argv[1]
    
    url = f"https://api.gumroad.com/v2/products/{product_id}/thumbnail"
    
    with open(image_path, "rb") as f:
        # Field name might be "thumbnail" or just "file"
        files = {"file": ("test_thumbnail.png", f, "image/png")}
        data = {"access_token": token}
        
        response = requests.post(url, data=data, files=files)
        print(response.status_code)
        import json
        try:
            print(json.dumps(response.json(), indent=2))
        except:
            print(response.text)

if __name__ == "__main__":
    main()
