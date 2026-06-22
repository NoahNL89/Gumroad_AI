"""
inject_images.py
Post-processes every product HTML file in downloads/pdfs/ and injects:
  - key-art.jpg as a hero image on the cover page
  - interior-01, 02, 03 illustrations at the first three section-headers
"""
import os, re, glob

BASE = "/home/administrator/NewGitHub/GumRoad_AI"
IMG_BASE = f"{BASE}/codex_images"
HTML_DIR = f"{BASE}/downloads/pdfs"

# Map from HTML filename stem → codex_images subfolder
PRODUCT_IMAGE_MAP = {
    "01_75_power_prompts_content_creators": "11-power-prompts-2026",
    "02_ai_prompt_vault_2026":              "24-ai-prompt-vault",
    "03_gemini_mega_prompt_pack":           "28-gemini-mega-prompt-pack",
    "04_gemini_15_pro_high_context":        "04-gemini-high-context",
    "05_local_llm_guide":                   "05-local-llm-guide",
    "06_ai_to_blender_kit":                 "06-ai-to-blender",
    "07_consistent_character_genesis_2026": "07-character-genesis-2026",
    "08_consistent_character_genesis_editorial": "08-character-genesis-editorial",
    "09_viral_hooks":                       "02-viral-hooks",
    "10_business_name_generator":           "12-business-name-workbook",
    "11_freelancer_prompt_pack":            "13-freelancer-prompt-pack",
    "12_instagram_growth_templates":        "14-instagram-growth",
    "13_cv_resume_templates":               "15-cv-resume-templates",
    "14_notion_habit_architecture":         "16-notion-habit-architecture",
    "15_omnichannel_social_calendar":       "17-omnichannel-calendar",
    "16_email_subject_line_mastery":        "18-email-subject-lines",
    "17_side_hustle_checklist":             "19-side-hustle-checklist",
    "18_journaling_prompts":                "20-journaling-clarity-calm",
    "19_seo_checklist":                     "21-seo-checklist",
    "20_ai_content_machine":                "23-ai-content-machine",
    "21_75_power_prompts_ai_masters":       "25-power-prompts-ai-masters",
    "22_ai_side_hustle_inner_circle":       "03-ai-side-hustle-inner-circle",
}


def img_tag(path, cls, caption=None):
    tag = f'<img src="file://{path}" class="{cls}" alt="">'
    if caption:
        return (f'<div class="img-interior-wrap">'
                f'{tag}'
                f'<p class="img-interior-caption">{caption}</p>'
                f'</div>')
    return tag


def get_interior_images(img_folder):
    """Return sorted list of interior-0N-*.jpg paths."""
    imgs = sorted(glob.glob(f"{img_folder}/interior-0*.jpg"))
    return imgs  # [interior-01-*.jpg, interior-02-*.jpg, interior-03-*.jpg]


def inject_cover_image(html, key_art_path):
    """Insert hero image between cover-sub paragraph and cover-meta div."""
    marker = '<div class="cover-meta">'
    idx = html.find(marker)
    if idx == -1:
        return html
    hero = f'\n  {img_tag(key_art_path, "img-cover-hero")}\n  '
    return html[:idx] + hero + html[idx:]


def inject_interior_images(html, interior_paths):
    """Insert up to 3 interior images after consecutive section-header closing divs."""
    if not interior_paths:
        return html

    # We look for the pattern that closes a section-header:
    # the section-header div always ends with \n  </div> (2-space indent)
    # We find each occurrence after a section-header opening.
    result = html
    offset = 0
    inserted = 0

    for img_path in interior_paths[:3]:
        # Find the next section-header from current offset
        sh_pos = result.find('class="section-header"', offset)
        if sh_pos == -1:
            break

        # From sh_pos, find the closing </div> (2-space indented)
        close_tag = "\n  </div>"
        close_pos = result.find(close_tag, sh_pos)
        if close_pos == -1:
            break

        insert_at = close_pos + len(close_tag)

        # Build caption from filename: interior-01-context-window.jpg → Context Window
        fname = os.path.basename(img_path)
        name_part = re.sub(r"^interior-0\d-", "", fname).replace(".jpg", "").replace("-", " ").title()

        img_html = f'\n\n  {img_tag(img_path, "img-interior", name_part)}'
        result = result[:insert_at] + img_html + result[insert_at:]
        offset = insert_at + len(img_html)
        inserted += 1

    return result


def process_file(html_path):
    stem = os.path.splitext(os.path.basename(html_path))[0]
    img_folder_name = PRODUCT_IMAGE_MAP.get(stem)
    if not img_folder_name:
        print(f"  SKIP (no mapping): {stem}")
        return

    img_folder = f"{IMG_BASE}/{img_folder_name}"
    if not os.path.isdir(img_folder):
        print(f"  SKIP (folder missing): {img_folder}")
        return

    key_art = f"{img_folder}/key-art.jpg"
    if not os.path.isfile(key_art):
        print(f"  SKIP (no key-art): {img_folder}")
        return

    interior_imgs = get_interior_images(img_folder)

    with open(html_path, "r") as f:
        html = f.read()

    # Skip if already injected (look for actual img tag, not just CSS class)
    if '<img src="file://' in html:
        print(f"  ALREADY injected: {stem}")
        return

    html = inject_cover_image(html, key_art)
    html = inject_interior_images(html, interior_imgs)

    with open(html_path, "w") as f:
        f.write(html)

    print(f"  OK ({len(interior_imgs)} interior images): {stem}")


if __name__ == "__main__":
    html_files = sorted(glob.glob(f"{HTML_DIR}/*.html"))
    print(f"Processing {len(html_files)} HTML files...\n")
    for hf in html_files:
        process_file(hf)
    print("\nDone.")
