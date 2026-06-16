import os
from PIL import Image

downloads_dir = "/home/administrator/NewGitHub/GumRoad_AI/downloads"

def main():
    if not os.path.exists(downloads_dir):
        print(f"Error: {downloads_dir} does not exist.")
        return

    subdirs = [d for d in os.listdir(downloads_dir) if os.path.isdir(os.path.join(downloads_dir, d))]
    subdirs.sort()

    print(f"{'Folder Name':<50} | {'Cover Filename':<45} | {'Size (KB)':<10} | {'Dimensions':<12} | {'Format'}")
    print("-" * 130)

    total_covers = 0
    for sd in subdirs:
        sd_path = os.path.join(downloads_dir, sd)
        files = os.listdir(sd_path)
        covers = [f for f in files if "cover" in f.lower()]
        
        for c in covers:
            c_path = os.path.join(sd_path, c)
            size_kb = os.path.getsize(c_path) / 1024
            
            try:
                with Image.open(c_path) as img:
                    width, height = img.size
                    img_format = img.format
                dimensions = f"{width}x{height}"
            except Exception as e:
                dimensions = "ERROR"
                img_format = "UNKNOWN"
            
            print(f"{sd[:50]:<50} | {c:<45} | {size_kb:<10.2f} | {dimensions:<12} | {img_format}")
            total_covers += 1

    print(f"\nTotal cover images found: {total_covers}")

if __name__ == "__main__":
    main()
