# Handoff Report — explorer_m1

## 1. Observation

### Authentication Status Check
Running `./scripts/auth-check.sh` directly returns:
```
=== Gumroad Auth Check ===

❌ Not authenticated.

To authenticate:
  gumroad auth login              # Interactive device flow
  export GUMROAD_ACCESS_TOKEN=xxx # CI/Agent mode
```
However, running `gumroad auth status --json --no-input` with the exported token returns:
```json
{
  "authenticated": true,
  "user": {
    "name": "Schep Digital",
    "currency_type": "eur",
    "email": "schephenk198@gmail.com",
    ...
  },
  "source": "env"
}
```
Line 10 of `scripts/auth-check.sh` reads:
```bash
if ! gumroad auth status --json --no-input 2>/dev/null | jq -e '.seller' > /dev/null 2>&1; then
```
The key `.seller` is not present in the JSON payload returned by `gumroad auth status`.

### Database Sync
Running `python3 db/sync.py` succeeded with output:
```
📦 Syncing products...
   /products API returned: 10
   User links (all permalinks): 28
   Extra products fetched by permalink: 18
   Total products discovered: 28
   ✅ 28 products saved to DB
```
A total of 28 products are stored in `db/store.db`. Only one product is priced at <= €0.99:
* Name: `Consistent Character Genesis`
* Price: `€0.99 a month` (recurring subscription)
* ID: `ACW3nWRr0KsHqXX9zFHgbA==`

### Product Cover Images and Files
Inside the `downloads/` directory:
- 26 folders exist (representing the product names).
- 12 cover images are found across 11 product directories.
- 6 of the cover images have extension `.png` but their internal file format is `JPEG`.
- Several files within these directories lack file extensions (e.g., `75-power-prompts`, `Consistent_Character_Genesis_FINAL`), but reading their first 4 bytes shows signature `25504446` (`%PDF`), meaning they are PDF files.

---

## 2. Logic Chain

1. **Authentication:** The `gumroad` CLI returns `"authenticated": true` and contains a `.user` object at the root of the JSON payload. Because the `scripts/auth-check.sh` checks for a `.seller` key which is absent, it incorrectly reports "Not authenticated". Changing the key path from `.seller` to `.user` resolves the auth-check failure.
2. **Products database sync:** The sync script discovered all 28 products (10 from `/products` endpoint and 18 extra fetched via individual user permalinks), matching expected counts. 27 of 28 products are priced > €0.99 (properly priced).
3. **Downloads folder contents:**
   - Folder name and product name alignment: Folders are named using sanitized versions of the product names.
   - Missing folder: "The Complete AI Creator Toolkit 2026 — All 10 Products Bundle" does not have a folder in `downloads/`.
   - Cover format verification: Utilizing Pillow's `Image.format` confirmed that files named `cover.png` in 6 folders are actually JPEGs (JPEG file signature `ffd8ffe0` or `ffd8ffe1`), whereas the ones in `The AI-to-Blender Mastery Kit - 2026 Edition` and `The Sovereign Professional's Local LLM Guide - 2026 Edition` are true PNGs.
   - Extensionless files: Checking the header bytes of files without extensions like `75-power-prompts` returned `%PDF`, confirming they are PDFs.

---

## 3. Caveats

- We did not write or execute any code to update products. The database sync was purely read-only updates downloaded from Gumroad API.
- We did not download any new files, but analyzed the files already residing in the `downloads/` folder.
- The MIME type detection of extensionless files was done via custom byte-matching scripts and not using system-level utilities like `file`, which may have minor differences depending on OS configuration.

---

## 4. Conclusion

- **Authentication:** The store is successfully authenticated. The `scripts/auth-check.sh` script should be patched with `auth-check.patch` to use `.user` instead of `.seller`.
- **Products database:** `store.db` is successfully synchronized and contains 28 products. Only 1 product (`Consistent Character Genesis`) remains underpriced at `€0.99 a month`.
- **Cover images & attachments:** There are 12 cover images in total. A summary of cover images, formats, and dimensions is included in the tables below. Several cover images have wrong extensions (PNG instead of JPEG), and many attachment files lack `.pdf` extensions.

### Detailed Product Table

| Product ID | Product Name | Current Price | Description Length | Cover Image Location |
|---|---|---|---|---|
| `Ooxbre7qZzU85P1n-wOgMA==` | 0.5s VIRAL HOOKS: The 2026 Psychology Framework (ADHD-Optimized) | €5.99 | 1317 | `downloads/0.5s VIRAL HOOKS The 2026 Psychology Framework (ADHD-Optimized)/cover---cda98f42-7ac5-4638-8deb-697b73452d18.jpg` |
| `f8ZzLmXADJxkrT_zuzBPng==` | 75 Power Prompts for AI Masters (2026) | €7.99 | 1453 | `downloads/75 Power Prompts for AI Masters (2026)/cover.jpg` |
| `eTBvYNwCDOJU21B-2dRYjQ==` | 75 Power Prompts for Content Creators - 2026 Edition | €7.99 | 1453 | *None* (Folder found, but no cover file) |
| `Tv95wemLl_bfeX_hBvp-2A==` | 75 Power Prompts for Content Creators: 2026 Master Edition | €7.99 | 1444 | `downloads/75 Power Prompts for Content Creators 2026 Master Edition/cover.jpg` |
| `_g5PymMS3u3xYEeuvIOiNQ==` | AI Content Machine Bundle - 2026 Engagement Blueprint | €7.99 | 1419 | *None* (Folder found, but no cover file) |
| `cgrMuZIqz_IvAUjX0q404w==` | AI PROMPT VAULT 2026: The 200+ Blueprint 'Operating System' (LLM-Patch) | €9.99 | 1202 | `downloads/AI PROMPT VAULT 2026 The 200+ Blueprint 'Operating System' (LLM-Patch)/cover.png` |
| `I9qlMBYv_lfoN4eDQskBcg==` | AI Side Hustle Inner Circle: All-Access Vault + Weekly Alpha | €12.99 | 976 | `downloads/AI Side Hustle Inner Circle All-Access Vault + Weekly Alpha/cover.png` |
| `FDNeAJrsuP-GGvnC1hM3Ag==` | Business Name Generator Workbook - 2026 Edition | €7.99 | 1527 | *None* (Folder found, but no cover file) |
| `iDizl7YGaHnQervCVINnSQ==` | CV & Resume Templates That Beat ATS - 2026 Edition | €7.99 | 1445 | *None* (Folder found, but no cover file) |
| `ACW3nWRr0KsHqXX9zFHgbA==` | Consistent Character Genesis | €0.99/mo | 1698 | *None* (Folder found, but no cover file) |
| `dQhOuA5T5rE6RC1hQ2Y5pw==` | Consistent Character Genesis: Midjourney Mastery (2026 Edition) | €7.99 | 1481 | `downloads/Consistent Character Genesis Midjourney Mastery (2026 Edition)/cover.png` |
| `LunWD_5niwqmTtPvImj2aw==` | Consistent Character Genesis: Midjourney Mastery (Editorial Edition) | €7.99 | 1163 | `downloads/Consistent Character Genesis Midjourney Mastery (Editorial Edition)/cover.png` |
| `bTlLI6ymD4kbSj9VRn0mXg==` | Consistent Character Genesis: Midjourney Mastery - 2026 Edition | €7.99 | 1698 | *None* (Folder found, but no cover file) |
| `c6HlPLBt4ylslV1Nht3IVQ==` | Email Subject Line Mastery - 2026 Edition | €7.99 | 1539 | *None* (Folder found, but no cover file) |
| `Z-tzjE8BgdTI91cBCilkbA==` | Freelancer Prompt Pack - Client & Proposal Edition | €7.99 | 1532 | *None* (Folder found, but no cover file) |
| `pkAOT6Z7J6HXSLS0_a0NcQ==` | GEMINI 1.5 PRO: Advanced 'No-Chunk' High-Context Architecture | €9.99 | 1093 | *None* (Folder found, but no cover file) |
| `QQQhvnq-IJb5fxi-eywkWQ==` | GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition) | €9.99 | 1228 | `downloads/GEMINI MEGA PROMPT PACK The 10M Token 'No-Chunk' Protocol (2026 Edition)/cover.jpg`, `placeholder_cover.png` |
| `mXjh_3p4Yv-cTAzpI8sDbA==` | Instagram Growth Templates - 2026 Edition | €7.99 | 1372 | *None* (Folder found, but no cover file) |
| `836otFGMZwShsk8B6I7iuQ==` | Journaling Prompts for Clarity & Calm - 2026 Edition | €7.99 | 1475 | *None* (Folder found, but no cover file) |
| `k0kIprwalUhdgVbZbqijLw==` | Notion Habit Architecture - 2026 Edition | €7.99 | 1619 | *None* (Folder found, but no cover file) |
| `gF9E6NWBQjFGjPjTNVdXEw==` | Omnichannel Social Media Calendar - 2026 Edition | €7.99 | 333 | *None* (Folder found, but no cover file) |
| `ROGBErC6NlBMaZBrUR3HyQ==` | SEO Checklist for Bloggers - 2026 Edition | €7.99 | 1585 | *None* (Folder found, but no cover file) |
| `aKUv7bw36hPXijZ47qpHAg==` | Side Hustle Quick-Start Checklist - 2026 Edition | €7.99 | 1561 | *None* (Folder found, but no cover file) |
| `tG5FweE35UaG-ak4ZE511g==` | The AI Prompt Vault | €7.99 | 1551 | *None* (Folder found, but no cover file) |
| `VkymGRV8NPff5TCLVHjuUw==` | The AI Prompt Vault: 200+ Engineering Blueprints (2026 Edition) | €7.99 | 1496 | `downloads/The AI Prompt Vault 200+ Engineering Blueprints (2026 Edition)/cover.png` |
| `KA9cbFaDhhCoh94TTuZ4pA==` | The AI-to-Blender Mastery Kit - 2026 Edition | €14.99 | 1372 | `downloads/The AI-to-Blender Mastery Kit - 2026 Edition/cover.png` |
| `ws-l3GFbvznUmNYUgBwUGA==` | The Complete AI Creator Toolkit 2026 — All 10 Products Bundle | €29.99 | 699 | *None* (No folder exists in `downloads/`) |
| `gIXM0JN3NDuI1-2BadEVNg==` | The Sovereign Professional's Local LLM Guide - 2026 Edition | €14.99 | 1412 | `downloads/The Sovereign Professional's Local LLM Guide - 2026 Edition/cover.png` |

### Detailed Cover Image Inspection Table

| Product Directory | Cover Filename | Size (KB) | Dimensions | Real Format | Extension Mismatch? |
|---|---|---|---|---|---|
| `0.5s VIRAL HOOKS The 2026 Psychology Framework (ADHD-Optimized)` | `cover---cda98f42-7ac5-4638-8deb-697b73452d18.jpg` | 683.71 | 1584x672 | JPEG | No |
| `75 Power Prompts for AI Masters (2026)` | `cover.jpg` | 914.98 | 1376x768 | JPEG | No |
| `75 Power Prompts for Content Creators 2026 Master Edition` | `cover.jpg` | 914.98 | 1376x768 | JPEG | No |
| `AI PROMPT VAULT 2026 The 200+ Blueprint 'Operating System' (LLM-Patch)` | `cover.png` | 846.19 | 1584x672 | JPEG | **Yes (PNG -> JPEG)** |
| `AI Side Hustle Inner Circle All-Access Vault + Weekly Alpha` | `cover.png` | 668.62 | 1408x768 | JPEG | **Yes (PNG -> JPEG)** |
| `Consistent Character Genesis Midjourney Mastery (2026 Edition)` | `cover.png` | 897.41 | 1408x768 | JPEG | **Yes (PNG -> JPEG)** |
| `Consistent Character Genesis Midjourney Mastery (Editorial Edition)` | `cover.png` | 897.41 | 1408x768 | JPEG | **Yes (PNG -> JPEG)** |
| `GEMINI MEGA PROMPT PACK The 10M Token 'No-Chunk' Protocol (2026 Edition)` | `cover.jpg` | 914.98 | 1376x768 | JPEG | No |
| `GEMINI MEGA PROMPT PACK The 10M Token 'No-Chunk' Protocol (2026 Edition)` | `placeholder_cover.png` | 897.41 | 1408x768 | JPEG | **Yes (PNG -> JPEG)** |
| `The AI Prompt Vault 200+ Engineering Blueprints (2026 Edition)` | `cover.png` | 846.19 | 1584x672 | JPEG | **Yes (PNG -> JPEG)** |
| `The AI-to-Blender Mastery Kit - 2026 Edition` | `cover.png` | 1793.41 | 1024x1024 | PNG | No |
| `The Sovereign Professional's Local LLM Guide - 2026 Edition` | `cover.png` | 1465.15 | 1024x1024 | PNG | No |

---

## 5. Verification Method

To independently verify the results, run these commands from the project root:

1. **Verify DB records & Price:**
   ```bash
   sqlite3 db/store.db "SELECT id, name, price_cents, formatted_price FROM products;"
   ```
2. **Verify Cover Image Dimensions & Formats:**
   ```bash
   python3 .agents/explorer_m1/inspect_covers.py
   ```
3. **Verify All Downloaded Files (incl. PDF signatures):**
   ```bash
   python3 .agents/explorer_m1/list_all_files.py
   ```
4. **Verify Auth Status logic:**
   ```bash
   bash -c 'source .env && export GUMROAD_ACCESS_TOKEN && gumroad auth status --json --no-input | jq -e ".user" >/dev/null && echo "Auth status check passed"'
   ```
