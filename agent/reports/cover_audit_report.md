# Gumroad Cover Image Audit Report

## Executive Summary

This report details the findings of an autonomous audit of all product cover assets stored in Schep Digital's store workspace. It maps the active products defined in the local database (`db/store.db`) against assets located under the `downloads/` directory, evaluating them for image file presence, format/naming integrity, standard display dimensions, and uniqueness.

### Key Audit Statistics
- **Total Products Evaluated**: 28
- **Products with Compliant Covers**: 0
- **Products Missing Covers completely**: 17 (Missing folder: 2, Missing file: 15)
- **Products with Technical Extension Mismatches**: 6
- **Products with Non-Standard Aspect Ratios**: 9
- **Products Reusing Duplicate Cover Images**: 7

### Severity Classification and Priority Definitions
- **High Priority**: Covers that are completely missing, have severe aspect ratio deviations (such as Square 1:1 or Ultra-wide 2.35:1) which cause display cropping, or have extension mismatches (internally JPEG but saved as `.png`) that might cause browser rendering or platform upload failures.
- **Medium Priority**: Covers that reuse the same image asset as other products (duplicate checksums), or have slight aspect ratio deviations (e.g. 1.83 aspect ratio).
- **Low Priority**: Compliant covers with standard landscape aspect ratio matching or close to the recommended 1280x720 resolution.

## Cover Replacement Recommendations

| Product Name | Current Cover File | Issue/Verdict | Priority |
| --- | --- | --- | --- |
| 0.5s VIRAL HOOKS: The 2026 Psychology Framework (ADHD-Optimized) | cover---cda98f42-7ac5-4638-8deb-697b73452d18.jpg | Non-standard aspect ratio: Ultra-wide 1584x672 (2.36 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). | High |
| 75 Power Prompts for Content Creators - 2026 Edition | None | Missing cover asset | High |
| AI Content Machine Bundle - 2026 Engagement Blueprint | None | Missing cover asset | High |
| AI PROMPT VAULT 2026: The 200+ Blueprint 'Operating System' (LLM-Patch) | cover.png | Extension mismatch: cover.png is internally JPEG but named with '.png' extension. <br> Non-standard aspect ratio: Ultra-wide 1584x672 (2.36 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). <br> Duplicate cover: Shares exact MD5 hash (04914a4a...) with product(s): The AI Prompt Vault: 200+ Engineering Blueprints (2026 Edition). | High |
| AI Side Hustle Inner Circle: All-Access Vault + Weekly Alpha | cover.png | Extension mismatch: cover.png is internally JPEG but named with '.png' extension. <br> Non-standard aspect ratio: 1408x768 (1.83 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). | High |
| Business Name Generator Workbook - 2026 Edition | None | Missing cover asset | High |
| CV & Resume Templates That Beat ATS - 2026 Edition | None | Missing cover asset | High |
| Consistent Character Genesis | None | Missing cover folder & asset | High |
| Consistent Character Genesis: Midjourney Mastery (2026 Edition) | cover.png | Extension mismatch: cover.png is internally JPEG but named with '.png' extension. <br> Non-standard aspect ratio: 1408x768 (1.83 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). <br> Duplicate cover: Shares exact MD5 hash (6c8b0957...) with product(s): Consistent Character Genesis: Midjourney Mastery (Editorial Edition), GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition). | High |
| Consistent Character Genesis: Midjourney Mastery (Editorial Edition) | cover.png | Extension mismatch: cover.png is internally JPEG but named with '.png' extension. <br> Non-standard aspect ratio: 1408x768 (1.83 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). <br> Duplicate cover: Shares exact MD5 hash (6c8b0957...) with product(s): Consistent Character Genesis: Midjourney Mastery (2026 Edition), GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition). | High |
| Consistent Character Genesis: Midjourney Mastery - 2026 Edition | None | Missing cover asset | High |
| Email Subject Line Mastery - 2026 Edition | None | Missing cover asset | High |
| Freelancer Prompt Pack - Client & Proposal Edition | None | Missing cover asset | High |
| GEMINI 1.5 PRO: Advanced 'No-Chunk' High-Context Architecture | None | Missing cover asset | High |
| GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition) | cover.jpg, placeholder_cover.png | Duplicate cover: Shares exact MD5 hash (ca1167e5...) with product(s): 75 Power Prompts for Content Creators: 2026 Master Edition, 75 Power Prompts for AI Masters (2026). <br> Extension mismatch: placeholder_cover.png is internally JPEG but named with '.png' extension. <br> Non-standard aspect ratio: 1408x768 (1.83 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). <br> Duplicate cover: Shares exact MD5 hash (6c8b0957...) with product(s): Consistent Character Genesis: Midjourney Mastery (2026 Edition), Consistent Character Genesis: Midjourney Mastery (Editorial Edition). | High |
| Instagram Growth Templates - 2026 Edition | None | Missing cover asset | High |
| Journaling Prompts for Clarity & Calm - 2026 Edition | None | Missing cover asset | High |
| Notion Habit Architecture - 2026 Edition | None | Missing cover asset | High |
| Omnichannel Social Media Calendar - 2026 Edition | None | Missing cover asset | High |
| SEO Checklist for Bloggers - 2026 Edition | None | Missing cover asset | High |
| Side Hustle Quick-Start Checklist - 2026 Edition | None | Missing cover asset | High |
| The AI Prompt Vault | None | Missing cover asset | High |
| The AI Prompt Vault: 200+ Engineering Blueprints (2026 Edition) | cover.png | Extension mismatch: cover.png is internally JPEG but named with '.png' extension. <br> Non-standard aspect ratio: Ultra-wide 1584x672 (2.36 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). <br> Duplicate cover: Shares exact MD5 hash (04914a4a...) with product(s): AI PROMPT VAULT 2026: The 200+ Blueprint 'Operating System' (LLM-Patch). | High |
| The AI-to-Blender Mastery Kit - 2026 Edition | cover.png | Non-standard aspect ratio: Square 1024x1024 (1.0 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). | High |
| The Complete AI Creator Toolkit 2026 — All 10 Products Bundle | None | Missing cover folder & asset | High |
| The Sovereign Professional's Local LLM Guide - 2026 Edition | cover.png | Non-standard aspect ratio: Square 1024x1024 (1.0 aspect ratio). Gumroad recommends 1280x720 (1.78 aspect ratio). | High |
| 75 Power Prompts for AI Masters (2026) | cover.jpg | Duplicate cover: Shares exact MD5 hash (ca1167e5...) with product(s): 75 Power Prompts for Content Creators: 2026 Master Edition, GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition). | Medium |
| 75 Power Prompts for Content Creators: 2026 Master Edition | cover.jpg | Duplicate cover: Shares exact MD5 hash (ca1167e5...) with product(s): 75 Power Prompts for AI Masters (2026), GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition). | Medium |

## Duplicate Cover Asset Groupings

The following groupings show image files that have identical MD5 hash values, representing redundant duplicate images reused across different products:

### Group 1: Hash `6c8b095733534d3a0933875ea1f3f94b`

| Product Name | Image File Path | Dimensions | Format |
| --- | --- | --- | --- |
| Consistent Character Genesis: Midjourney Mastery (2026 Edition) | `downloads/Consistent Character Genesis Midjourney Mastery (2026 Edition)/cover.png` | 1408x768 | JPEG |
| Consistent Character Genesis: Midjourney Mastery (Editorial Edition) | `downloads/Consistent Character Genesis Midjourney Mastery (Editorial Edition)/cover.png` | 1408x768 | JPEG |
| GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition) | `downloads/GEMINI MEGA PROMPT PACK The 10M Token 'No-Chunk' Protocol (2026 Edition)/placeholder_cover.png` | 1408x768 | JPEG |

### Group 2: Hash `ca1167e5d284983735a49f022c5846c0`

| Product Name | Image File Path | Dimensions | Format |
| --- | --- | --- | --- |
| 75 Power Prompts for Content Creators: 2026 Master Edition | `downloads/75 Power Prompts for Content Creators 2026 Master Edition/cover.jpg` | 1376x768 | JPEG |
| 75 Power Prompts for AI Masters (2026) | `downloads/75 Power Prompts for AI Masters (2026)/cover.jpg` | 1376x768 | JPEG |
| GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition) | `downloads/GEMINI MEGA PROMPT PACK The 10M Token 'No-Chunk' Protocol (2026 Edition)/cover.jpg` | 1376x768 | JPEG |

### Group 3: Hash `04914a4a40c894033030dbdb5939119b`

| Product Name | Image File Path | Dimensions | Format |
| --- | --- | --- | --- |
| AI PROMPT VAULT 2026: The 200+ Blueprint 'Operating System' (LLM-Patch) | `downloads/AI PROMPT VAULT 2026 The 200+ Blueprint 'Operating System' (LLM-Patch)/cover.png` | 1584x672 | JPEG |
| The AI Prompt Vault: 200+ Engineering Blueprints (2026 Edition) | `downloads/The AI Prompt Vault 200+ Engineering Blueprints (2026 Edition)/cover.png` | 1584x672 | JPEG |

## Technical Format Mismatches (Extension Mismatches)

Files identified with mismatching file extensions relative to their internal binary format. These issues must be fixed to prevent upload/rendering errors:

- **Product**: AI Side Hustle Inner Circle: All-Access Vault + Weekly Alpha
  - File: `downloads/AI Side Hustle Inner Circle All-Access Vault + Weekly Alpha/cover.png`
  - Extension: `.png`
  - Actual Internal Format: `JPEG`

- **Product**: Consistent Character Genesis: Midjourney Mastery (2026 Edition)
  - File: `downloads/Consistent Character Genesis Midjourney Mastery (2026 Edition)/cover.png`
  - Extension: `.png`
  - Actual Internal Format: `JPEG`

- **Product**: Consistent Character Genesis: Midjourney Mastery (Editorial Edition)
  - File: `downloads/Consistent Character Genesis Midjourney Mastery (Editorial Edition)/cover.png`
  - Extension: `.png`
  - Actual Internal Format: `JPEG`

- **Product**: AI PROMPT VAULT 2026: The 200+ Blueprint 'Operating System' (LLM-Patch)
  - File: `downloads/AI PROMPT VAULT 2026 The 200+ Blueprint 'Operating System' (LLM-Patch)/cover.png`
  - Extension: `.png`
  - Actual Internal Format: `JPEG`

- **Product**: The AI Prompt Vault: 200+ Engineering Blueprints (2026 Edition)
  - File: `downloads/The AI Prompt Vault 200+ Engineering Blueprints (2026 Edition)/cover.png`
  - Extension: `.png`
  - Actual Internal Format: `JPEG`

- **Product**: GEMINI MEGA PROMPT PACK: The 10M Token 'No-Chunk' Protocol (2026 Edition)
  - File: `downloads/GEMINI MEGA PROMPT PACK The 10M Token 'No-Chunk' Protocol (2026 Edition)/placeholder_cover.png`
  - Extension: `.png`
  - Actual Internal Format: `JPEG`

## Products Missing Cover Assets

The following products either have no downloads directory or lack a cover image file inside their folder:

### Completely Missing Downloads Folder
- Consistent Character Genesis
- The Complete AI Creator Toolkit 2026 — All 10 Products Bundle

### Folder Exists but Missing Cover Image File
- 75 Power Prompts for Content Creators - 2026 Edition (Folder: `downloads/75 Power Prompts for Content Creators - 2026 Edition/`)
- AI Content Machine Bundle - 2026 Engagement Blueprint (Folder: `downloads/AI Content Machine Bundle - 2026 Engagement Blueprint/`)
- Business Name Generator Workbook - 2026 Edition (Folder: `downloads/Business Name Generator Workbook - 2026 Edition/`)
- CV & Resume Templates That Beat ATS - 2026 Edition (Folder: `downloads/CV & Resume Templates That Beat ATS - 2026 Edition/`)
- Consistent Character Genesis: Midjourney Mastery - 2026 Edition (Folder: `downloads/Consistent Character Genesis Midjourney Mastery - 2026 Edition/`)
- Email Subject Line Mastery - 2026 Edition (Folder: `downloads/Email Subject Line Mastery - 2026 Edition/`)
- Freelancer Prompt Pack - Client & Proposal Edition (Folder: `downloads/Freelancer Prompt Pack - Client & Proposal Edition/`)
- GEMINI 1.5 PRO: Advanced 'No-Chunk' High-Context Architecture (Folder: `downloads/GEMINI 1.5 PRO Advanced 'No-Chunk' High-Context Architecture/`)
- Instagram Growth Templates - 2026 Edition (Folder: `downloads/Instagram Growth Templates - 2026 Edition/`)
- Journaling Prompts for Clarity & Calm - 2026 Edition (Folder: `downloads/Journaling Prompts for Clarity & Calm - 2026 Edition/`)
- Notion Habit Architecture - 2026 Edition (Folder: `downloads/Notion Habit Architecture - 2026 Edition/`)
- Omnichannel Social Media Calendar - 2026 Edition (Folder: `downloads/Omnichannel Social Media Calendar - 2026 Edition/`)
- SEO Checklist for Bloggers - 2026 Edition (Folder: `downloads/SEO Checklist for Bloggers - 2026 Edition/`)
- Side Hustle Quick-Start Checklist - 2026 Edition (Folder: `downloads/Side Hustle Quick-Start Checklist - 2026 Edition/`)
- The AI Prompt Vault (Folder: `downloads/The AI Prompt Vault/`)
