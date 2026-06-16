import urllib.request
import urllib.parse
import os
import time

products = [
    {
        "name": "Consistent Character Genesis",
        "file": "assets/consistent_character_genesis.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of character design, 3D modeling, artificial intelligence generation. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "The Complete AI Creator Toolkit 2026 — All 10 Products Bundle",
        "file": "assets/ai_creator_toolkit_bundle.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of a massive toolkit, glowing data cubes, digital assets bundle. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "75 Power Prompts for Content Creators - 2026 Edition",
        "file": "assets/75_power_prompts_content_creators.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of writing, prompt engineering, digital content creation. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "AI Content Machine Bundle - 2026 Engagement Blueprint",
        "file": "assets/ai_content_machine_bundle.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of content generation machine, blueprint, digital factory. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Consistent Character Genesis: Midjourney Mastery - 2026 Edition",
        "file": "assets/midjourney_mastery_character.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of midjourney, artistic prompt mastery, evolving digital characters. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Email Subject Line Mastery - 2026 Edition",
        "file": "assets/email_subject_line_mastery.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of email marketing, open rates, digital communication. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Freelancer Prompt Pack - Client & Proposal Edition",
        "file": "assets/freelancer_prompt_pack.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of freelancing, proposals, glowing business handshake, digital networking. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "GEMINI 1.5 PRO: Advanced 'No-Chunk' High-Context Architecture",
        "file": "assets/gemini_1_5_pro_architecture.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of neural networks, high-context AI models, large language architecture. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Instagram Growth Templates - 2026 Edition",
        "file": "assets/instagram_growth_templates.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of social media growth, engagement graphs, digital community. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Journaling Prompts for Clarity & Calm - 2026 Edition",
        "file": "assets/journaling_prompts_clarity.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of digital journaling, mental clarity, glowing serene digital waves. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Notion Habit Architecture - 2026 Edition",
        "file": "assets/notion_habit_architecture.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of structural organization, habit tracking, digital workspaces, notion architecture. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Omnichannel Social Media Calendar - 2026 Edition",
        "file": "assets/omnichannel_social_calendar.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of calendar planning, omnichannel marketing, digital scheduling. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Side Hustle Quick-Start Checklist - 2026 Edition",
        "file": "assets/side_hustle_checklist.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of startup, checklist, side hustle, glowing checkmarks, success pathway. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "The AI Prompt Vault",
        "file": "assets/ai_prompt_vault.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Concept of a glowing digital vault, storing AI prompts, high-tech security. Dark mode, very wide aspect ratio, high resolution."
    }
]

# Ensure we aren't caching to disk if it hangs
import socket
socket.setdefaulttimeout(15)

for p in products:
    if os.path.exists(p["file"]) and os.path.getsize(p["file"]) > 0:
        print(f"Skipping {p['name']}, file already exists.")
        continue

    # add a random seed to bust pollinations cache if it's acting weird
    seed = int(time.time() * 1000) % 100000
    url_encoded_prompt = urllib.parse.quote(p["prompt"])
    url = f"https://image.pollinations.ai/prompt/{url_encoded_prompt}?width=1280&height=720&nologo=true&seed={seed}"
    print(f"Generating image for {p['name']}...")
    
    success = False
    for attempt in range(5):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                content = response.read()
                if len(content) > 0:
                    with open(p["file"], 'wb') as out_file:
                        out_file.write(content)
                    print(f"Saved to {p['file']}")
                    success = True
                    time.sleep(2)
                    break
        except urllib.error.HTTPError as e:
            if e.code == 402:
                print(f"Rate limited (402). Attempt {attempt + 1}/5. Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print(f"Failed to generate for {p['name']}: {e}")
                time.sleep(2)
        except Exception as e:
            print(f"Exception for {p['name']}: {e}")
            time.sleep(2)
    
    if not success:
        print(f"Could not generate {p['name']} after multiple attempts.")

print("All done!")
