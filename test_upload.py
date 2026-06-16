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
    if not token:
        print("No token")
        return

    # SEO Checklist for Bloggers product ID
    product_id = "ROGBErC6NlBMaZBrUR3HyQ=="
    image_path = "/home/administrator/NewGitHub/GumRoad_AI/assets/seo_checklist_cover.jpg"
    
    url = f"https://api.gumroad.com/v2/products/{product_id}"
    
    # Try sending as preview_url or thumbnail or just file?
    # Let's try sending as `preview_url` (Gumroad uses preview_url for cover image)
    # Actually wait, maybe it's just 'thumbnail'?
    
    # Let's use requests files parameter to send multipart form data
    with open(image_path, "rb") as f:
        # Field name might be "preview_url" or "thumbnail"
        files = {"preview_url": ("seo_checklist_cover.jpg", f, "image/jpeg")}
        data = {"access_token": token}
        
        response = requests.put(url, data=data, files=files)
        print(response.status_code)
        print(response.text)

if __name__ == "__main__":
    main()
