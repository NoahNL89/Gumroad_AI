import urllib.request
import urllib.parse
import os

products = [
    {
        "name": "SEO Checklist for Bloggers - 2026 Edition",
        "file": "assets/seo_checklist_cover.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. SEO optimization, search engine growth, blogging checklist concepts. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "CV & Resume Templates That Beat ATS - 2026 Edition",
        "file": "assets/cv_resume_cover.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Resume, CV, career growth, ATS algorithms, job hunting. Dark mode, very wide aspect ratio, high resolution."
    },
    {
        "name": "Business Name Generator Workbook - 2026 Edition",
        "file": "assets/business_name_cover.jpg",
        "prompt": "A professional wide banner background for a digital creator's social media. Cyberpunk aesthetics, neon lines, abstract technology and AI themes. Business names, startup branding, creative ideas workbook. Dark mode, very wide aspect ratio, high resolution."
    }
]

for p in products:
    url_encoded_prompt = urllib.parse.quote(p["prompt"])
    url = f"https://image.pollinations.ai/prompt/{url_encoded_prompt}?width=1280&height=720&nologo=true"
    print(f"Generating image for {p['name']}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(p["file"], 'wb') as out_file:
        out_file.write(response.read())
    print(f"Saved to {p['file']}")

