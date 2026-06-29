#!/usr/bin/env python3
"""Upload product thumbnails when the installed Gumroad CLI supports it."""

import subprocess


def main():
    help_result = subprocess.run(
        ["gumroad", "products", "update", "--help"],
        capture_output=True, text=True, check=False,
    )
    if help_result.returncode != 0:
        print(help_result.stderr.strip() or "Unable to inspect Gumroad CLI capabilities.")
        return help_result.returncode or 1
    if "--thumbnail" not in help_result.stdout:
        print("Thumbnail upload is unavailable in the installed Gumroad CLI.")
        print("Direct API fallback is disabled; no products were changed.")
        return 2

    print("Thumbnail support was detected, but this CLI version exposes an unknown flag contract.")
    print("Update this script against `gumroad products update --help` before bulk changes.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
