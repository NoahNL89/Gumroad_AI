#!/bin/bash
# Upload remade PDFs to Gumroad products 3-22
# Product 1 and 2 were already uploaded.

source .env
set -e

upload() {
  local id="$1"
  local pdf="$2"
  local name="$3"
  echo -n "  Uploading $name ... "
  gumroad products update "$id" \
    --file "$pdf" \
    --file-name "$name" \
    --json --no-input --yes > /tmp/gumroad_upload.json 2>&1
  echo "done"
}

echo "=== Uploading remade PDFs to Gumroad ==="

upload "QQQhvnq-IJb5fxi-eywkWQ==" \
  "downloads/pdfs/03_gemini_mega_prompt_pack.pdf" \
  "Gemini Mega Prompt Pack (Schep Digital).pdf"

upload "pkAOT6Z7J6HXSLS0_a0NcQ==" \
  "downloads/pdfs/04_gemini_15_pro_high_context.pdf" \
  "Gemini 1.5 Pro High-Context Guide (Schep Digital).pdf"

upload "gIXM0JN3NDuI1-2BadEVNg==" \
  "downloads/pdfs/05_local_llm_guide.pdf" \
  "Local LLM Setup Guide (Schep Digital).pdf"

upload "KA9cbFaDhhCoh94TTuZ4pA==" \
  "downloads/pdfs/06_ai_to_blender_kit.pdf" \
  "AI-to-Blender Kit (Schep Digital).pdf"

upload "dQhOuA5T5rE6RC1hQ2Y5pw==" \
  "downloads/pdfs/07_consistent_character_genesis_2026.pdf" \
  "Consistent Character Genesis 2026 (Schep Digital).pdf"

upload "LunWD_5niwqmTtPvImj2aw==" \
  "downloads/pdfs/08_consistent_character_genesis_editorial.pdf" \
  "Consistent Character Genesis Editorial (Schep Digital).pdf"

upload "Ooxbre7qZzU85P1n-wOgMA==" \
  "downloads/pdfs/09_viral_hooks.pdf" \
  "0.5s Viral Hooks (Schep Digital).pdf"

upload "FDNeAJrsuP-GGvnC1hM3Ag==" \
  "downloads/pdfs/10_business_name_generator.pdf" \
  "AI Business Name Generator (Schep Digital).pdf"

upload "Z-tzjE8BgdTI91cBCilkbA==" \
  "downloads/pdfs/11_freelancer_prompt_pack.pdf" \
  "Freelancer AI Prompt Pack (Schep Digital).pdf"

upload "mXjh_3p4Yv-cTAzpI8sDbA==" \
  "downloads/pdfs/12_instagram_growth_templates.pdf" \
  "Instagram Growth Templates (Schep Digital).pdf"

upload "iDizl7YGaHnQervCVINnSQ==" \
  "downloads/pdfs/13_cv_resume_templates.pdf" \
  "CV & Resume AI Templates (Schep Digital).pdf"

upload "k0kIprwalUhdgVbZbqijLw==" \
  "downloads/pdfs/14_notion_habit_architecture.pdf" \
  "Notion Habit Architecture (Schep Digital).pdf"

upload "gF9E6NWBQjFGjPjTNVdXEw==" \
  "downloads/pdfs/15_omnichannel_social_calendar.pdf" \
  "Omnichannel Social Media Calendar (Schep Digital).pdf"

upload "c6HlPLBt4ylslV1Nht3IVQ==" \
  "downloads/pdfs/16_email_subject_line_mastery.pdf" \
  "Email Subject Line Mastery (Schep Digital).pdf"

upload "aKUv7bw36hPXijZ47qpHAg==" \
  "downloads/pdfs/17_side_hustle_checklist.pdf" \
  "Side Hustle Quick-Start Checklist (Schep Digital).pdf"

upload "836otFGMZwShsk8B6I7iuQ==" \
  "downloads/pdfs/18_journaling_prompts.pdf" \
  "Journaling Prompts for Clarity & Calm (Schep Digital).pdf"

upload "ROGBErC6NlBMaZBrUR3HyQ==" \
  "downloads/pdfs/19_seo_checklist.pdf" \
  "SEO Checklist 2026 (Schep Digital).pdf"

upload "_g5PymMS3u3xYEeuvIOiNQ==" \
  "downloads/pdfs/20_ai_content_machine.pdf" \
  "AI Content Machine Bundle (Schep Digital).pdf"

upload "f8ZzLmXADJxkrT_zuzBPng==" \
  "downloads/pdfs/21_75_power_prompts_ai_masters.pdf" \
  "75 Power Prompts for AI Masters (Schep Digital).pdf"

upload "I9qlMBYv_lfoN4eDQskBcg==" \
  "downloads/pdfs/22_ai_side_hustle_inner_circle.pdf" \
  "AI Side Hustle Inner Circle (Schep Digital).pdf"

echo ""
echo "=== All uploads complete ==="
