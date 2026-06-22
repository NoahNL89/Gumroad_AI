"""
creem_create_products.py
Creates all 22 Schep Digital products on Creem in test mode.
Saves results to creem/products.json for reference.
"""
import os, json, time, requests
from pathlib import Path

API_BASE = "https://test-api.creem.io/v1"
API_KEY  = os.environ.get("CREEM_API_KEY", "")

if not API_KEY:
    raise SystemExit("CREEM_API_KEY not set in environment")

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json",
}

# price is in smallest currency unit (cents for EUR)
PRODUCTS = [
    {
        "name": "75 Power Prompts for Content Creators: 2026 Edition",
        "description": (
            "75 copy-paste AI prompts across 8 chapters — from batch content "
            "production to audience psychology. Built for creators who need output "
            "today, not theory. Works with Claude, ChatGPT, and Gemini."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "01_75_power_prompts_content_creators",
    },
    {
        "name": "AI Prompt Vault 2026: 200+ Blueprint Prompts",
        "description": (
            "200+ structured prompts across 12 business categories — content, "
            "marketing, strategy, sales, productivity, research, and more. "
            "Each prompt is a blueprint: plug in your context and ship."
        ),
        "price": 999,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "02_ai_prompt_vault_2026",
    },
    {
        "name": "Gemini Mega Prompt Pack: The 10M Token No-Chunk Protocol",
        "description": (
            "50+ prompts engineered specifically for Gemini's 1M-token context window. "
            "Load entire codebases, document libraries, and research archives — "
            "extract structured intelligence in one pass. Zero chunking required."
        ),
        "price": 999,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "03_gemini_mega_prompt_pack",
    },
    {
        "name": "Gemini 1.5 Pro: High-Context Architecture Guide",
        "description": (
            "Master the 1M-token context window. Input structuring with the PRIME "
            "framework, multi-step workflow design, multimodal combinations, and "
            "Python API automation. The complete guide to Gemini's long-context advantage."
        ),
        "price": 999,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "04_gemini_15_pro_high_context",
    },
    {
        "name": "Local LLM Setup Guide: Run AI on Your Own Hardware",
        "description": (
            "Zero API costs, total privacy, unlimited rate limits. From hardware "
            "selection and Ollama setup to Open WebUI, batch processing, and "
            "fine-tuning — fully operational in one afternoon."
        ),
        "price": 1499,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "05_local_llm_guide",
    },
    {
        "name": "AI-to-Blender Kit: Scripts, Prompts & Workflows",
        "description": (
            "15+ ready-to-run Blender Python scripts and 20+ AI prompts for 3D "
            "artists. Concept generation, automated scripting, texture creation, "
            "and scene composition — powered by AI, built for artists."
        ),
        "price": 1499,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "06_ai_to_blender_kit",
    },
    {
        "name": "Consistent Character Genesis 2026: Midjourney Mastery",
        "description": (
            "Three proven techniques for maintaining recognizable AI characters "
            "across 50+ scenes. Character bibles, seed locking, reference injection, "
            "and LoRA fine-tuning. 95% identity retention across all scenes."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "07_consistent_character_genesis_2026",
    },
    {
        "name": "Consistent Character Genesis: Editorial Edition",
        "description": (
            "Brand mascot systems, multi-character scenes, and licensing-safe "
            "commercial workflows for AI-generated illustration. Built for marketers, "
            "publishers, and creative directors who need print-ready output."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "08_consistent_character_genesis_editorial",
    },
    {
        "name": "0.5s Viral Hooks: Stop the Scroll in Half a Second",
        "description": (
            "100+ hook templates across 12 proven formats for TikTok, Reels, "
            "YouTube Shorts, and LinkedIn. Every format tested, every template "
            "ready to deploy. Average 2.5–3× completion rate improvement."
        ),
        "price": 599,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "09_viral_hooks",
    },
    {
        "name": "AI Business Name Generator: 8 Archetypes + 5-Filter System",
        "description": (
            "A structured system for generating and validating business names using AI. "
            "8 naming archetypes, 50+ prompts, and a 5-filter shortlisting process. "
            "From blank page to trademark-ready shortlist."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "10_business_name_generator",
    },
    {
        "name": "Freelancer AI Prompt Pack: Proposals, Clients & Contracts",
        "description": (
            "60+ prompts for every stage of the freelance business — proposals, "
            "client emails, scope creep responses, contracts, rate increases, and "
            "late payment follow-ups. Save 8 hours per week on admin."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "11_freelancer_prompt_pack",
    },
    {
        "name": "Instagram Growth Templates: Captions, Carousels & Stories",
        "description": (
            "30+ caption templates, 15 carousel structures, and 10 story sequences "
            "built around Instagram's 2026 engagement mechanics. Strategy-first "
            "design that drives saves, shares, and profile visits."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "12_instagram_growth_templates",
    },
    {
        "name": "CV & Resume AI Templates: Beat ATS, Win Interviews",
        "description": (
            "ATS-optimized prompts, 5 section formulas, and cover letter generators. "
            "Get past the robots and impress the humans. Includes keyword extraction, "
            "tailoring prompts, and a complete cover letter system."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "13_cv_resume_templates",
    },
    {
        "name": "Notion Habit Architecture: AI-Powered Habit System",
        "description": (
            "12 Notion templates, 30+ AI review prompts, and a 3-layer habit system "
            "built on stacking, streak tracking, and weekly AI-assisted audits. "
            "The infrastructure for compound personal growth."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "14_notion_habit_architecture",
    },
    {
        "name": "Omnichannel Social Media Calendar: The Content Atom Model",
        "description": (
            "Create one piece per week, derive 7+ across every channel. LinkedIn, "
            "X, Instagram, TikTok, and newsletters from one source of truth. "
            "The repurposing engine that makes 4 hours of work fill an entire week."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "15_omnichannel_social_calendar",
    },
    {
        "name": "Email Subject Line Mastery: 80+ Formulas + A/B Framework",
        "description": (
            "80+ subject line formulas across 8 goal categories, an A/B testing "
            "framework, and AI prompts to generate 10 variations for any email "
            "in 60 seconds. Target: 40%+ open rates."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "16_email_subject_line_mastery",
    },
    {
        "name": "Side Hustle Quick-Start Checklist: 90 Days to First Payment",
        "description": (
            "7-phase, 90-day checklist from idea to first paying customer. "
            "Validation, offer creation, first sale, and scaling — one decision "
            "at a time, zero capital required to start."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "17_side_hustle_checklist",
    },
    {
        "name": "Journaling Prompts for Clarity & Calm: 100+ Structured Prompts",
        "description": (
            "100+ prompts across 8 life categories — clarity, decisions, identity, "
            "relationships, goals, and creativity. Each prompt engineered to surface "
            "something useful in 10 minutes. Works on paper, Notion, or Day One."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "18_journaling_prompts",
    },
    {
        "name": "SEO Checklist 2026: Technical, Content & AI Search",
        "description": (
            "80+ checklist items across 6 audit categories — technical foundation, "
            "content-intent matching, on-page optimization, link building, and "
            "AI search readiness. Updated for the Helpful Content era and AI Overviews."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "19_seo_checklist",
    },
    {
        "name": "AI Content Machine Bundle: Hook Architecture + Carousel System",
        "description": (
            "Three integrated tools: Hook Architecture, Carousel Production System, "
            "and Omnichannel Repurposing Engine. One week of setup. 7× your content "
            "output with 4 hours of work per week."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "20_ai_content_machine",
    },
    {
        "name": "75 Power Prompts for AI Masters: Advanced Techniques",
        "description": (
            "Meta-prompting, chain-of-thought engineering, multi-model orchestration, "
            "and adversarial testing — 75 prompts that assume you already know the "
            "basics. For experienced AI users who want the next level."
        ),
        "price": 799,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "21_75_power_prompts_ai_masters",
    },
    {
        "name": "AI Side Hustle Inner Circle: Monthly Playbooks + Community",
        "description": (
            "Monthly playbooks, live strategy sessions, and a private community "
            "for AI-native income builders. Digital products, client services, "
            "and automation strategies — your first €500/month with AI leverage."
        ),
        "price": 1299,
        "currency": "EUR",
        "billing_type": "onetime",
        "slug": "22_ai_side_hustle_inner_circle",
    },
]


def create_product(product: dict) -> dict:
    payload = {k: v for k, v in product.items() if k != "slug"}
    resp = requests.post(f"{API_BASE}/products", headers=HEADERS, json=payload)
    return resp.json()


def main():
    out_dir = Path("creem")
    out_dir.mkdir(exist_ok=True)
    results_file = out_dir / "products.json"

    # Load existing results to avoid duplication
    if results_file.exists():
        existing = json.loads(results_file.read_text())
    else:
        existing = {}

    created = dict(existing)
    errors  = []

    print(f"Creating {len(PRODUCTS)} products on Creem (test mode)...\n")

    for p in PRODUCTS:
        slug = p["slug"]
        if slug in created:
            print(f"  SKIP (exists): {p['name'][:55]}")
            continue

        print(f"  Creating: {p['name'][:55]} ... ", end="", flush=True)
        result = create_product(p)

        if result.get("object") == "product":
            created[slug] = {
                "creem_id":    result["id"],
                "product_url": result["product_url"],
                "name":        result["name"],
                "price_eur":   result["price"] / 100,
                "mode":        result["mode"],
                "status":      result["status"],
            }
            print(f"OK → {result['id']}")
            results_file.write_text(json.dumps(created, indent=2))
        else:
            msg = result.get("message", result)
            print(f"ERROR: {msg}")
            errors.append({"slug": slug, "error": msg})

        time.sleep(0.3)  # gentle rate limit

    print(f"\n{'='*60}")
    print(f"Created: {len(created) - len(existing)} new  |  Total: {len(created)}  |  Errors: {len(errors)}")
    print(f"Results saved to: {results_file}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  {e['slug']}: {e['error']}")

    # Print the product URL summary
    print("\n=== Creem Product URLs (test mode) ===")
    for slug, info in created.items():
        print(f"  {info['name'][:45]:<45} {info['price_eur']:>6.2f}€  {info['product_url']}")


if __name__ == "__main__":
    main()
