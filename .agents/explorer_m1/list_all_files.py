import os
import mimetypes

downloads_dir = "/home/administrator/NewGitHub/GumRoad_AI/downloads"

def main():
    if not os.path.exists(downloads_dir):
        print("Downloads dir not found")
        return

    subdirs = sorted([d for d in os.listdir(downloads_dir) if os.path.isdir(os.path.join(downloads_dir, d))])
    
    for sd in subdirs:
        sd_path = os.path.join(downloads_dir, sd)
        files = sorted(os.listdir(sd_path))
        print(f"\n📂 {sd}")
        for f in files:
            f_path = os.path.join(sd_path, f)
            size_kb = os.path.getsize(f_path) / 1024
            mime, _ = mimetypes.guess_type(f_path)
            # Read first 4 bytes to check signature if no extension
            signature = ""
            try:
                with open(f_path, "rb") as fh:
                    sig = fh.read(4)
                    signature = sig.hex()
            except Exception:
                pass
            
            file_type_str = mime if mime else "Unknown"
            if signature.startswith("89504e47"):
                file_type_str = "image/png"
            elif signature.startswith("ffd8ffe0") or signature.startswith("ffd8ffe1") or signature.startswith("ffd8ffee"):
                file_type_str = "image/jpeg"
            elif signature.startswith("25504446"):
                file_type_str = "application/pdf"
            elif signature.startswith("504b0304"):
                file_type_str = "application/zip"
                
            print(f"   - {f:<50} | {size_kb:>8.2f} KB | {file_type_str} | (sig: {signature[:8]})")

if __name__ == "__main__":
    main()
