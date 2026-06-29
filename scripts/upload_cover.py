#!/usr/bin/env python3
"""Upload a product cover when the installed Gumroad CLI supports it."""

import os
import subprocess
import sys


def upload_cover(product_id, image_path):
    if not os.path.isfile(image_path):
        print(f"Image not found: {image_path}")
        return 1

    help_result = subprocess.run(
        ["gumroad", "products", "update", "--help"],
        capture_output=True, text=True, check=False,
    )
    if help_result.returncode != 0:
        print(help_result.stderr.strip() or "Unable to inspect Gumroad CLI capabilities.")
        return help_result.returncode or 1
    if "--preview-url" not in help_result.stdout:
        print("Cover upload is unavailable: this Gumroad CLI has no --preview-url flag.")
        print("Direct API fallback is disabled; no product was changed.")
        return 2

    result = subprocess.run([
        "gumroad", "products", "update", product_id,
        "--preview-url", os.path.abspath(image_path),
        "--json", "--no-input", "--no-color", "--yes",
    ], check=False)
    return result.returncode


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 scripts/upload_cover.py <product_id> <image_path>")
        raise SystemExit(1)
    raise SystemExit(upload_cover(sys.argv[1], sys.argv[2]))
