#!/usr/bin/env python3
import os
import hashlib
import sqlite3
from collections import defaultdict
from PIL import Image

def compute_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_image_info(file_path):
    try:
        with Image.open(file_path) as img:
            width, height = img.size
            img_format = img.format  # e.g. 'JPEG' or 'PNG'
            return width, height, img_format
    except Exception as e:
        return None, None, str(e)

def normalize_name(name):
    # Normalize colons and spaces to match folder naming convention
    return name.replace(':', '')

def main():
    workspace_root = "/home/administrator/NewGitHub/GumRoad_AI"
    db_path = os.path.join(workspace_root, "db/store.db")
    downloads_dir = os.path.join(workspace_root, "downloads")
    report_path = os.path.join(workspace_root, "cover_audit_report.md")

    # Connect to db
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, published FROM products")
    db_products = cursor.fetchall()
    conn.close()

    # List of all cover files found
    # We will map them by: normalized_folder_name -> list of cover file info
    all_covers = defaultdict(list)
    
    if os.path.exists(downloads_dir):
        folders = os.listdir(downloads_dir)
        for folder in folders:
            folder_path = os.path.join(downloads_dir, folder)
            if not os.path.isdir(folder_path):
                continue
            for filename in os.listdir(folder_path):
                # Search for files containing 'cover' and with image extension
                if "cover" in filename.lower() and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    file_path = os.path.join(folder_path, filename)
                    md5_hash = compute_md5(file_path)
                    w, h, fmt = get_image_info(file_path)
                    
                    # Calculate aspect ratio
                    aspect_ratio = round(w / h, 2) if (w and h) else 0.0
                    
                    all_covers[folder.lower()].append({
                        "filename": filename,
                        "relative_path": os.path.relpath(file_path, workspace_root),
                        "absolute_path": file_path,
                        "md5": md5_hash,
                        "width": w,
                        "height": h,
                        "format": fmt,
                        "aspect_ratio": aspect_ratio
                    })

    # Grouping and Analysis
    product_status = {}
    
    # Track missing covers
    missing_folders = []
    missing_files = []
    
    # Track duplicates
    hash_to_files = defaultdict(list)

    # Walk through products in database
    for pid, name, published in db_products:
        norm_name = normalize_name(name)
        folder_found = False
        product_folder_name = None
        
        # Check folder presence case-insensitively
        if os.path.exists(downloads_dir):
            for f in os.listdir(downloads_dir):
                if f.lower() == norm_name.lower():
                    folder_found = True
                    product_folder_name = f
                    break
        
        if not folder_found:
            missing_folders.append(name)
            product_status[name] = {
                "folder_exists": False,
                "covers": [],
                "issues": ["Missing cover folder in downloads/", "Missing cover asset"],
                "verdict": "Missing cover folder & asset",
                "priority": "High"
            }
        else:
            covers = all_covers[product_folder_name.lower()]
            if not covers:
                missing_files.append(name)
                product_status[name] = {
                    "folder_exists": True,
                    "folder_name": product_folder_name,
                    "covers": [],
                    "issues": ["Missing cover asset in product folder"],
                    "verdict": "Missing cover asset",
                    "priority": "High"
                }
            else:
                product_status[name] = {
                    "folder_exists": True,
                    "folder_name": product_folder_name,
                    "covers": covers,
                    "issues": [],
                    "verdict": "OK",
                    "priority": "Low"
                }
                for cover in covers:
                    hash_to_files[cover["md5"]].append((name, cover))

    # Identify duplicates
    duplicate_groups = {}
    for md5, files in hash_to_files.items():
        # A duplicate is when multiple products share the same MD5 hash
        unique_products = set(pname for pname, _ in files)
        if len(unique_products) > 1:
            duplicate_groups[md5] = files

    # Analyze covers for technical issues & updates
    for name, status in product_status.items():
        if not status["folder_exists"] or not status["covers"]:
            continue
        
        covers = status["covers"]
        issues = []
        high_priority = False
        medium_priority = False

        for cover in covers:
            # 1. Extension mismatch check
            ext = os.path.splitext(cover["filename"])[1].lower()
            fmt = cover["format"]
            ext_mismatch = False
            if fmt == "JPEG" and ext not in [".jpg", ".jpeg"]:
                ext_mismatch = True
            elif fmt == "PNG" and ext != ".png":
                ext_mismatch = True
            
            if ext_mismatch:
                issues.append(f"Extension mismatch: {cover['filename']} is internally {fmt} but named with '{ext}' extension.")
                high_priority = True

            # 2. Aspect ratio check
            # Standard is close to 1.78 (16:9, e.g. 1280x720)
            aspect = cover["aspect_ratio"]
            if cover["width"] == 1280 and cover["height"] == 720:
                pass  # Perfect
            elif 1.75 <= aspect <= 1.80:
                # Slight variance, low priority, let's flag as small issue or ok
                pass
            elif aspect == 1.0:
                issues.append(f"Non-standard aspect ratio: Square {cover['width']}x{cover['height']} ({aspect} aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio).")
                high_priority = True
            elif aspect > 2.0:
                issues.append(f"Non-standard aspect ratio: Ultra-wide {cover['width']}x{cover['height']} ({aspect} aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio).")
                high_priority = True
            else:
                issues.append(f"Non-standard aspect ratio: {cover['width']}x{cover['height']} ({aspect} aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio).")
                # Slightly non-standard dimension but not square/ultra-wide could be medium or high
                if aspect > 1.81 or aspect < 1.74:
                    medium_priority = True

            # 3. Duplicate check
            md5 = cover["md5"]
            if md5 in duplicate_groups:
                shared_with = [pname for pname, _ in duplicate_groups[md5] if pname != name]
                issues.append(f"Duplicate cover: Shares exact MD5 hash ({md5[:8]}...) with product(s): {', '.join(shared_with)}.")
                medium_priority = True

        if issues:
            status["issues"] = issues
            status["verdict"] = " | ".join(issues)
            status["priority"] = "High" if high_priority else "Medium"
        else:
            status["verdict"] = "Valid - Compliant with guidelines"
            status["priority"] = "Low"

    # Build report content
    report_lines = []
    report_lines.append("# Gumroad Cover Image Audit Report")
    report_lines.append("")
    
    # Executive Summary
    report_lines.append("## Executive Summary")
    report_lines.append("")
    total_products = len(db_products)
    missing_folder_count = len(missing_folders)
    missing_file_count = len(missing_files)
    total_missing = missing_folder_count + missing_file_count
    
    # Calculate counts
    mismatch_count = 0
    ratio_count = 0
    duplicate_count = 0
    ok_count = 0
    
    for name, status in product_status.items():
        if not status["folder_exists"] or not status["covers"]:
            continue
        has_mismatch = any(
            (cover["format"] == "JPEG" and os.path.splitext(cover["filename"])[1].lower() not in [".jpg", ".jpeg"]) or
            (cover["format"] == "PNG" and os.path.splitext(cover["filename"])[1].lower() != ".png")
            for cover in status["covers"]
        )
        has_ratio = any(
            not (cover["width"] == 1280 and cover["height"] == 720) and not (1.75 <= cover["aspect_ratio"] <= 1.80)
            for cover in status["covers"]
        )
        has_dup = any(cover["md5"] in duplicate_groups for cover in status["covers"])
        
        if has_mismatch:
            mismatch_count += 1
        if has_ratio:
            ratio_count += 1
        if has_dup:
            duplicate_count += 1
        if not has_mismatch and not has_ratio and not has_dup:
            ok_count += 1

    report_lines.append("This report details the findings of an autonomous audit of all product cover assets stored in Schep Digital's store workspace. It maps the active products defined in the local database (`db/store.db`) against assets located under the `downloads/` directory, evaluating them for image file presence, format/naming integrity, standard display dimensions, and uniqueness.")
    report_lines.append("")
    report_lines.append("### Key Audit Statistics")
    report_lines.append(f"- **Total Products Evaluated**: {total_products}")
    report_lines.append(f"- **Products with Compliant Covers**: {ok_count}")
    report_lines.append(f"- **Products Missing Covers completely**: {total_missing} (Missing folder: {missing_folder_count}, Missing file: {missing_file_count})")
    report_lines.append(f"- **Products with Technical Extension Mismatches**: {mismatch_count}")
    report_lines.append(f"- **Products with Non-Standard Aspect Ratios**: {ratio_count}")
    report_lines.append(f"- **Products Reusing Duplicate Cover Images**: {duplicate_count}")
    report_lines.append("")
    report_lines.append("### Severity Classification and Priority Definitions")
    report_lines.append("- **High Priority**: Covers that are completely missing, have severe aspect ratio deviations (such as Square 1:1 or Ultra-wide 2.35:1) which cause display cropping, or have extension mismatches (internally JPEG but saved as `.png`) that might cause browser rendering or platform upload failures.")
    report_lines.append("- **Medium Priority**: Covers that reuse the same image asset as other products (duplicate checksums), or have slight aspect ratio deviations (e.g. 1.83 aspect ratio).")
    report_lines.append("- **Low Priority**: Compliant covers with standard landscape aspect ratio matching or close to the recommended 1280x720 resolution.")
    report_lines.append("")

    # Cover Replacement Recommendations
    report_lines.append("## Cover Replacement Recommendations")
    report_lines.append("")
    report_lines.append("| Product Name | Current Cover File | Issue/Verdict | Priority |")
    report_lines.append("| --- | --- | --- | --- |")
    
    # Sort recommendations by priority (High, then Medium, then Low) and then by product name
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    sorted_products = sorted(
        product_status.items(),
        key=lambda item: (priority_order[item[1]["priority"]], item[0])
    )
    
    for name, status in sorted_products:
        cover_files_str = ", ".join(c["filename"] for c in status["covers"]) if status["covers"] else "None"
        verdict = status["verdict"]
        priority = status["priority"]
        
        # Clean verdict string for markdown table
        clean_verdict = verdict.replace("|", "<br>")
        report_lines.append(f"| {name} | {cover_files_str} | {clean_verdict} | {priority} |")
        
    report_lines.append("")

    # Duplicate Cover Asset Groupings
    report_lines.append("## Duplicate Cover Asset Groupings")
    report_lines.append("")
    report_lines.append("The following groupings show image files that have identical MD5 hash values, representing redundant duplicate images reused across different products:")
    report_lines.append("")
    
    for i, (md5, files) in enumerate(duplicate_groups.items(), 1):
        report_lines.append(f"### Group {i}: Hash `{md5}`")
        report_lines.append("")
        report_lines.append("| Product Name | Image File Path | Dimensions | Format |")
        report_lines.append("| --- | --- | --- | --- |")
        for pname, cover in files:
            report_lines.append(f"| {pname} | `{cover['relative_path']}` | {cover['width']}x{cover['height']} | {cover['format']} |")
        report_lines.append("")
        
    if not duplicate_groups:
        report_lines.append("*No duplicate cover assets detected.*")
        report_lines.append("")

    # Technical Format Mismatches
    report_lines.append("## Technical Format Mismatches (Extension Mismatches)")
    report_lines.append("")
    report_lines.append("Files identified with mismatching file extensions relative to their internal binary format. These issues must be fixed to prevent upload/rendering errors:")
    report_lines.append("")
    
    mismatch_found = False
    for name, status in product_status.items():
        for cover in status["covers"]:
            ext = os.path.splitext(cover["filename"])[1].lower()
            fmt = cover["format"]
            if (fmt == "JPEG" and ext not in [".jpg", ".jpeg"]) or (fmt == "PNG" and ext != ".png"):
                mismatch_found = True
                report_lines.append(f"- **Product**: {name}")
                report_lines.append(f"  - File: `{cover['relative_path']}`")
                report_lines.append(f"  - Extension: `{ext}`")
                report_lines.append(f"  - Actual Internal Format: `{fmt}`")
                report_lines.append("")
                
    if not mismatch_found:
        report_lines.append("*No technical format mismatches detected.*")
        report_lines.append("")

    # Missing Cover Assets
    report_lines.append("## Products Missing Cover Assets")
    report_lines.append("")
    report_lines.append("The following products either have no downloads directory or lack a cover image file inside their folder:")
    report_lines.append("")
    
    if missing_folders:
        report_lines.append("### Completely Missing Downloads Folder")
        for name in sorted(missing_folders):
            report_lines.append(f"- {name}")
        report_lines.append("")
        
    if missing_files:
        report_lines.append("### Folder Exists but Missing Cover Image File")
        for name in sorted(missing_files):
            status = product_status[name]
            report_lines.append(f"- {name} (Folder: `downloads/{status['folder_name']}/`)")
        report_lines.append("")
        
    if not missing_folders and not missing_files:
        report_lines.append("*All products have cover assets.*")
        report_lines.append("")

    # Write report
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        
    print(f"Audit report programmatically written to {report_path}")

if __name__ == "__main__":
    main()
