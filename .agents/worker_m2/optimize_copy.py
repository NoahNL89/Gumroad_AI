import json
import os
import re
import difflib

INPUT_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/extracted_products.json"
OUTPUT_PATH = "/home/administrator/NewGitHub/GumRoad_AI/.agents/worker_m2/copy_dry_run.json"

# Detailed copywriting metadata for each of the 28 products
PRODUCT_METADATA = {
    "ws-l3GFbvznUmNYUgBwUGA==": {
        "hook": "🚀 Stop Buying Tools Separately. Own the Entire AI Creator Arsenal Today.",
        "problem": "Buying individual AI guides and prompt packs is expensive, hard to coordinate, and leaves gaps in your creative workflow.",
        "solution": "Get all 10 premium Schep Digital products in a single, high-value bundle. This complete toolkit gives you the ultimate competitive edge at a fraction of the cost, saving you over 60%.",
        "audience": "Digital creators, marketers, freelancers, and AI power-users looking for a complete, integrated toolkit.",
        "cta": "Click the 'I want this!' button to secure your lifetime license and dominate the AI attention economy!"
    },
    "Ooxbre7qZzU85P1n-wOgMA==": {
        "hook": "🔥 Grab Attention in 0.5 Seconds Before the Algorithm Buries Your Content.",
        "problem": "Traditional hooks are too slow. The modern attention span is under a second, and generic AI hooks are immediately scrolled past, leaving your content invisible.",
        "solution": "A psychological warfare manual optimized for lizard-brain triggers to bypass AI-pattern filters and drive raw human curiosity.",
        "audience": "Short-form video creators, copywriters, and social media marketers seeking high-retention frameworks.",
        "cta": "Click the 'I want this!' button to grab the attention psychology framework and scale your organic reach!"
    },
    "I9qlMBYv_lfoN4eDQskBcg==": {
        "hook": "💎 Unlock the Exact AI Revenue Systems Dominating the 2026 Economy.",
        "problem": "Public AI side hustles are saturated by the time you hear about them on YouTube or TikTok, leaving you with zero profit.",
        "solution": "An exclusive, active intelligence feed offering weekly niche breakdowns, prompt blueprints, and pre-release digital assets before anyone else.",
        "audience": "Aspiring solopreneurs, side-hustlers, and digital creators looking for profitable, uncrowded AI niches.",
        "cta": "Subscribe now to lock in your lifetime alpha rate and get instant access to the Master Vault!"
    },
    "pkAOT6Z7J6HXSLS0_a0NcQ==": {
        "hook": "🧠 Stop Cutting Your Data. Master the 10-Million Token Context Window.",
        "problem": "RAG and data chunking lose context, introduce errors, and waste valuable engineering time by cutting up your data.",
        "solution": "Learn the 'No-Chunk' protocol to feed entire codebases, 1000-page PDFs, and hours of video directly into Gemini 1.5 Pro.",
        "audience": "Developers, technical writers, and database analysts who need deep-context reasoning.",
        "cta": "Click the 'I want this!' button to master high-context prompt engineering and own the context loop!"
    },
    "gIXM0JN3NDuI1-2BadEVNg==": {
        "hook": "🔒 Break Free from AI Subscriptions. Run the World's Best Models Locally.",
        "problem": "Cloud AI tools are expensive, censor your inputs, track your data, and lock you into recurring monthly subscription fees.",
        "solution": "A comprehensive setup guide to run Llama 3, DeepSeek, and Mistral on your own hardware at zero cost, completely offline.",
        "audience": "Privacy-focused professionals, developers, writers, and solopreneurs demanding data sovereignty.",
        "cta": "Click the 'I want this!' button to quit the subscription trap and air-gap your AI intelligence today!"
    },
    "KA9cbFaDhhCoh94TTuZ4pA==": {
        "hook": "🎨 Stop Rendering Slow. Bridge the Gap Between AI Speed and Blender Precision.",
        "problem": "Manually modeling every primary shape and texture map is too slow in a fast-paced professional production pipeline.",
        "solution": "Connect generative AI speed with Blender's 3D environment for rapid prototyping, seamless texture mapping, and fast rendering.",
        "audience": "3D artists, game designers, and digital illustrators looking to 10x their workflow velocity.",
        "cta": "Click the 'I want this!' button to master the AI-to-Blender pipeline and dominate the 3D space!"
    },
    "dQhOuA5T5rE6RC1hQ2Y5pw==": {
        "hook": "🎯 End the Midjourney Character Lottery. Lock in Consistent Faces Every Time.",
        "problem": "Character faces drift across different generations, ruining continuity for comics, storyboards, and brand assets.",
        "solution": "A surgical reference-locking workflow using `--cref` and weight calibration to secure stable character DNA across infinite scenes.",
        "audience": "Graphic novelists, storyboard artists, and AI influencer creators seeking professional consistency.",
        "cta": "Click the 'I want this!' button to master consistent character creation and build your brand asset library!"
    },
    "LunWD_5niwqmTtPvImj2aw==": {
        "hook": "📸 Preserve the Digital Soul of Your Character Across Infinite Scenarios.",
        "problem": "Casual character prompting looks amateurish and fails to maintain clothing or style consistency in professional editorial layouts.",
        "solution": "Editorial-grade character workflows specializing in Reference (cref) control, weight tuning, and master reference sheets.",
        "audience": "Publishers, art directors, and serious character designers looking for professional-grade consistency.",
        "cta": "Click the 'I want this!' button to move from a casual prompter to a digital character architect!"
    },
    "Tv95wemLl_bfeX_hBvp-2A==": {
        "hook": "⚡ Transform Your AI from a Generic Writer to a High-Conversion Machine.",
        "problem": "Standard AI outputs sound robotic, trigger AI detection filters, and fail to engage human readers or generate sales.",
        "solution": "75 battle-tested, structured command architectures engineered to bypass filters and produce high-intent content.",
        "audience": "Content creators, copywriters, and online brand builders looking to optimize their conversion rates.",
        "cta": "Click the 'I want this!' button to secure your master copy of the 75 Power Prompts and convert readers!"
    },
    "cgrMuZIqz_IvAUjX0q404w==": {
        "hook": "🛠️ Patch Your AI Workflows. Install the 2026 LLM Prompting Operating System.",
        "problem": "Wasting hours trying to write the perfect prompt only to receive inconsistent, weak, or superficial outputs.",
        "solution": "A massive, structured library of 200+ blueprint prompts engineered with Chain-of-Thought reasoning for expert-level execution.",
        "audience": "Knowledge workers, freelancers, and entrepreneurs who need an operating system for productivity.",
        "cta": "Click the 'I want this!' button to download the prompt vault and patch your AI workflow inefficiencies!"
    },
    "eTBvYNwCDOJU21B-2dRYjQ==": {
        "hook": "📢 Stop Wishing, Start Commanding. Own the 75 Creator Blueprint Prompts.",
        "problem": "Vague prompts yield shallow content that algorithm filters immediately flag, ruining your blog and newsletter growth.",
        "solution": "Structured, multi-step prompting architectures designed to extract expert-level, platform-native outputs from LLMs.",
        "audience": "Bloggers, scriptwriters, and newsletter creators who want structured command templates.",
        "cta": "Click the 'I want this!' button to command the models and produce high-impact creator content!"
    },
    "FDNeAJrsuP-GGvnC1hM3Ag==": {
        "hook": "🏷️ Turn a Blank Page Into a Brandable Name That Sticks in 2026.",
        "problem": "Brainstorming business names is hard, and most names lack personality, domain availability, or emotional resonance.",
        "solution": "A structured naming workbook using psychological frameworks, trademark checks, and AI validation techniques.",
        "audience": "Aspiring founders, product managers, and brand creators looking for a memorable brand identity.",
        "cta": "Click the 'I want this!' button to secure your workbook and build a brand name that lasts!"
    },
    "Z-tzjE8BgdTI91cBCilkbA==": {
        "hook": "💼 10x Your Freelance Output and Reclaim Your Freedom Using AI.",
        "problem": "Freelancers spend too much unpaid time on administrative tasks, proposals, and low-margin production work.",
        "solution": "Over 250 prompts designed to automate proposals, onboarding, cold outreach, and client communication.",
        "audience": "Freelancers, solopreneurs, and independent contractors wanting to scale their income.",
        "cta": "Click the 'I want this!' button to optimize your output and run your business on your own terms!"
    },
    "mXjh_3p4Yv-cTAzpI8sDbA==": {
        "hook": "📈 Decode the 2026 Instagram Algorithm and Turn Views Into Sales.",
        "problem": "Post views don't equal sales, and the Instagram algorithm constantly shifts its metrics away from simple likes.",
        "solution": "A template playbook focused on retention, carousel architecture, and story funnels that drive DMs and link clicks.",
        "audience": "Instagram creators, e-commerce brand owners, and social media managers looking for conversion.",
        "cta": "Click the 'I want this!' button to master the hook and dominate the Instagram feed!"
    },
    "iDizl7YGaHnQervCVINnSQ==": {
        "hook": "📄 Bypass the AI Gatekeepers. Land Your Dream Interview in 2026.",
        "problem": "Over 90% of resumes are filtered out by Applicant Tracking Systems (ATS) before a human recruiter ever reads them.",
        "solution": "Resume templates and formatting strategies engineered to rank high in ATS while impressing hiring managers.",
        "audience": "Job seekers, career changers, and recent graduates wanting callbacks.",
        "cta": "Click the 'I want this!' button to quantify your value, beat the filter, and land the role!"
    },
    "k0kIprwalUhdgVbZbqijLw==": {
        "hook": "📅 Stop Tracking Habits. Build a Permanent Behavioral Identity.",
        "problem": "Simple habit checklists fail within days because they don't address behavior psychology or gamification metrics.",
        "solution": "A complete Notion blueprint using Formulas 2.0 to gamify habits, track analytics, and build lasting routines.",
        "audience": "Productivity enthusiasts, Notion users, and anyone building new routines.",
        "cta": "Click the 'I want this!' button to build the identity and run the ultimate habit architecture!"
    },
    "gF9E6NWBQjFGjPjTNVdXEw==": {
        "hook": "🗓️ Streamline Your Social Media Calendar Across All Major Channels.",
        "problem": "Content calendars are messy, disconnected, and take hours of manual planning every single week.",
        "solution": "A unified, omnichannel calendar system designed to coordinate content across X, LinkedIn, Instagram, and TikTok with zero friction.",
        "audience": "Social media managers, content strategists, and solo creators seeking sanity in planning.",
        "cta": "Click the 'I want this!' button to organize your content strategy and save hours of work!"
    },
    "c6HlPLBt4ylslV1Nht3IVQ==": {
        "hook": "✉️ Rescue Your Emails from the Spam Folder. Triple Your Open Rates.",
        "problem": "AI email filters are blocking promotional text, and inbox noise is higher than ever, causing low open rates.",
        "solution": "A psychological and technical guide to crafting subject lines that beat the filters and trigger curiosity.",
        "audience": "Email marketers, newsletter authors, and business owners striving for higher inbox reach.",
        "cta": "Click the 'I want this!' button to open the inbox and build an audience that wants to hear from you!"
    },
    "aKUv7bw36hPXijZ47qpHAg==": {
        "hook": "💰 Build a Modern, High-Margin Side Hustle Powered by AI.",
        "problem": "Traditional side hustles like driving or manual gig work require too much time for too little financial return.",
        "solution": "A step-by-step checklist to identify, validate, and scale AI-driven digital arbitrage side hustles.",
        "audience": "Solopreneurs, full-time workers seeking secondary income, and beginners.",
        "cta": "Click the 'I want this!' button to own the system and build a profitable secondary income!"
    },
    "836otFGMZwShsk8B6I7iuQ==": {
        "hook": "🧘 Upgrade Your Mind. Navigate Modern Stress with Science-Backed Journaling.",
        "problem": "Staring at a blank page creates mental resistance, and basic journaling does not solve cognitive stress or anxiety.",
        "solution": "Journaling prompts built on Cognitive Behavioral Therapy (CBT) and RAIN mindfulness to restructure thoughts.",
        "audience": "High-stress professionals, wellness seekers, and creators wanting mental clarity.",
        "cta": "Click the 'I want this!' button to refine your mind and find calm in the digital storm!"
    },
    "ROGBErC6NlBMaZBrUR3HyQ==": {
        "hook": "🔍 Dominate the Search Moat in the Age of AI-Generated Content.",
        "problem": "Search engines are penalizing generic AI fluff, making traditional keyword stuffing completely obsolete.",
        "solution": "A human-first E-E-A-T search strategy checklist to establish authentic authority and rank permanently.",
        "audience": "Bloggers, content creators, and SEO strategists who need genuine search traffic.",
        "cta": "Click the 'I want this!' button to upgrade your blog, earn your rankings, and be undeniably human!"
    },
    "bTlLI6ymD4kbSj9VRn0mXg==": {
        "hook": "👾 Lock in Character DNA in Midjourney. Create Enduring Digital Assets.",
        "problem": "Without consistency, you cannot monetize AI characters or build continuous visual narratives in Midjourney.",
        "solution": "Professional-grade workflows for Midjourney cref parameter control and structural persistence across scenes.",
        "audience": "AI artists, comic book writers, and storyboard creators seeking visual consistency.",
        "cta": "Click the 'I want this!' button to lock in your character's identity and build digital IP!"
    },
    "_g5PymMS3u3xYEeuvIOiNQ==": {
        "hook": "🤖 Build a High-Velocity Content Machine That Algorithm Filters Can't Stop.",
        "problem": "Generic AI content is muted by platform algorithms that prioritize high-retention, human-like engagement.",
        "solution": "A multi-step command architecture bundle to turn raw ideas into high-retention carousels, hooks, and posts.",
        "audience": "Brand founders, creators, and agency owners wanting to scale content production.",
        "cta": "Click the 'I want this!' button to build a high-performance content machine today!"
    },
    "tG5FweE35UaG-ak4ZE511g==": {
        "hook": "🔑 Deploy 200+ Professional Engineering Blueprints to Run Your Business.",
        "problem": "Copy-pasting simplistic prompts produces low-quality, generic results that waste time and look amateurish.",
        "solution": "A structured database of engineering-grade prompts using Chain-of-Thought reasoning for high-value outputs.",
        "audience": "Solopreneurs, project managers, and digital writers seeking advanced prompt design.",
        "cta": "Click the 'I want this!' button to deploy the engineering blueprints and streamline your operations!"
    },
    "f8ZzLmXADJxkrT_zuzBPng==": {
        "hook": "🌟 Unlock the Full Potential of 2026 LLMs with 75 Structured Command Blueprints.",
        "problem": "Generic prompts fail to leverage the advanced reasoning of next-gen AI models, yielding shallow content.",
        "solution": "Structured, multi-step prompt templates engineered specifically for high-conversion content creators.",
        "audience": "Creators, copywriters, and newsletter growth specialists.",
        "cta": "Click the 'I want this!' button to own the 75 power prompts and level up your output!"
    },
    "ACW3nWRr0KsHqXX9zFHgbA==": {
        "hook": "🎨 Create Consistent Protagonists Across Infinite Worlds in Midjourney.",
        "problem": "Relying on luck or random seed values keeps your character faces drifting, preventing serious visual storytelling.",
        "solution": "Definitive, master-level workflows for structural character persistence in Midjourney's latent space.",
        "audience": "Digital illustrators, game concept designers, and content creators looking for consistent characters.",
        "cta": "Click the 'I want this!' button to master character genesis and build enduring assets!"
    },
    "VkymGRV8NPff5TCLVHjuUw==": {
        "hook": "🚀 Equip Yourself with the 200+ Blueprint Prompting Operating System.",
        "problem": "Low-value AI content lacks expertise, causing your business, brand, or professional outputs to suffer.",
        "solution": "High-performance, Chain-of-Thought command blueprints designed for premium, expert-grade results.",
        "audience": "Knowledge workers, startup founders, and freelancers looking for productivity systems.",
        "cta": "Click the 'I want this!' button to deploy the prompting operating system and command the models!"
    },
    "QQQhvnq-IJb5fxi-eywkWQ==": {
        "hook": "🐳 Unleash the 10M Token Edge. Stop Chunking and Start Auditing.",
        "problem": "Working with limited context windows forces you to split databases, losing crucial cross-referencing capabilities.",
        "solution": "The definitive No-Chunk field manual for feeding entire codebases and books into Gemini's massive context window.",
        "audience": "Software engineers, data analysts, and legal/financial auditors needing large file reasoning.",
        "cta": "Click the 'I want this!' button to unlock infinite context leverage and start auditing!"
    }
}

def extract_features_from_description(name, description):
    # Fallback for the placeholder product 17
    if "[NAME]" in description or "gF9E6NWBQjFGjPjTNVdXEw" in name:
        return [
            "Unified content calendar template to plan posts across X, LinkedIn, Instagram, and TikTok",
            "Omnichannel repurposing workflows to turn 1 core idea into 10 platform-native formats",
            "Algorithm compliance checklists tracking the latest 2026 retention signals",
            "Interactive kanban board stages to coordinate content from draft to published status"
        ]
        
    features = []
    
    # Check for HTML <li> tags
    li_matches = re.findall(r'<li>\s*(.*?)\s*</li>', description, re.DOTALL)
    if li_matches:
        for m in li_matches:
            # Strip HTML tags inside li
            m_clean = re.sub(r'<[^>]+>', '', m).strip()
            # Remove linebreaks/extra spaces
            m_clean = " ".join(m_clean.split())
            if m_clean:
                features.append(m_clean)
                
    # If no <li> tags, check for lines starting with - or *
    if not features:
        lines = description.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('-') or line.startswith('*'):
                item = line.lstrip('-* \t').strip()
                # Clean up bold markers
                item = item.replace("**", "")
                if item:
                    features.append(item)
                    
    # Clean features list from any outdated price mentions
    cleaned_features = []
    for f in features:
        # Skip items that talk about June 2026 pricing or alpha pricing thresholds
        if any(term in f.lower() for term in ["€0.99", "alpha price", "beta-tester", "launch price", "impulse buy"]):
            continue
        cleaned_features.append(f)
        
    return cleaned_features

def main():
    if not os.path.exists(INPUT_PATH):
        print(f"Error: Input file {INPUT_PATH} does not exist.")
        return

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        products = json.load(f)

    optimized_products = []

    print("Optimizing product descriptions...")
    print(f"{'PRODUCT NAME':<60} | {'ORIG':>5} | {'OPT':>5} | {'DIFF%':>6} | {'SIM':>5}")
    print("-" * 92)

    for idx, p in enumerate(products):
        p_id = p["id"]
        p_name = p["name"]
        orig_desc = p["description"]
        price = p["price"]

        metadata = PRODUCT_METADATA.get(p_id)
        if not metadata:
            print(f"Warning: No metadata found for product {p_name} ({p_id}). Using fallback.")
            metadata = {
                "hook": f"🚀 Maximize Your Results with {p_name}.",
                "problem": "Traditional manual methods are too slow, expensive, and lead to poor conversion rates.",
                "solution": "Deploy our battle-tested, structured framework to automate your workflow, save time, and scale profits.",
                "audience": "Professionals, creators, and marketers looking to optimize their digital output.",
                "cta": "Click the 'I want this!' button to get instant lifetime access now!"
            }

        features = extract_features_from_description(p_name, orig_desc)
        features_html = "\n".join([f"  <li><strong>{f.split(':')[0]}:</strong>{f.split(':')[1] if ':' in f else ''}</li>" if ":" in f else f"  <li>{f}</li>" for f in features])

        # Format optimized description according to conversion copywriting strategy
        opt_desc = f"""<h2><strong>{metadata['hook']}</strong></h2>

<p><strong>The Challenge:</strong> {metadata['problem']}</p>

<p><strong>The Breakthrough:</strong> {metadata['solution']}</p>

<h3><strong>What's Inside:</strong></h3>
<ul>
{features_html}
</ul>

<p><strong>Who Is This For?</strong><br>
This product is specifically designed for {metadata['audience']}</p>

<hr>

<p><strong>👉 Get Instant Lifetime Access Now:</strong></p>
<p>{metadata['cta']} Secure your copy today for only €{price:.2f}.</p>
"""

        # Programmatic check for change (length and content comparison)
        len_orig = len(orig_desc)
        len_opt = len(opt_desc)
        len_diff_pct = abs(len_opt - len_orig) / max(len_orig, 1) * 100.0
        
        matcher = difflib.SequenceMatcher(None, orig_desc, opt_desc)
        similarity = matcher.ratio()

        # Check: has changed by at least 30%?
        # Length change >= 30% OR content similarity <= 70%
        has_changed_significantly = (len_diff_pct >= 30.0) or (similarity <= 0.70)

        assert has_changed_significantly, f"Error: Description for '{p_name}' not modified by 30%!"

        print(f"{p_name[:59]:<60} | {len_orig:>5} | {len_opt:>5} | {len_diff_pct:>5.1f}% | {similarity:>5.2f}")

        optimized_products.append({
            "id": p_id,
            "name": p_name,
            "price": price,
            "original_description": orig_desc,
            "optimized_description": opt_desc,
            "length_diff_pct": len_diff_pct,
            "content_similarity": similarity
        })

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(optimized_products, f, indent=2, ensure_ascii=False)

    print("-" * 92)
    print(f"Successfully optimized {len(optimized_products)} products.")
    print(f"Dry run file written to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
