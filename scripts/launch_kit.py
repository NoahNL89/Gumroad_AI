#!/usr/bin/env python3
"""
launch_kit.py — generate ready-to-post launch content for the channels the
social bots can't reach (Reddit, Product Hunt, SEO, email, X thread).

The Mastodon/Bluesky bots post into tiny audiences. Real buyers are on Reddit,
Product Hunt, in search results, and on your email list. This turns one product
into a multi-channel launch kit you (or a human) can post in minutes.

Usage:
    python3 scripts/launch_kit.py best                 # the strongest seller (or priciest if none sold)
    python3 scripts/launch_kit.py <product-id>
    python3 scripts/launch_kit.py "linkedin"           # first product whose name matches
    python3 scripts/launch_kit.py best --write         # also save to agent/launch_kits/<slug>.md
"""
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "store.db"
OUT_DIR = ROOT / "agent" / "launch_kits"
CODE = "LAUNCH30"

# product keyword -> (subreddits, primary SEO keyword theme)
CHANNELS = [
    (("blender", "3d"),            ["r/blender", "r/3Dmodeling", "r/StableDiffusion"], "AI to Blender workflow"),
    (("character", "midjourney"),  ["r/midjourney", "r/StableDiffusion", "r/AIArt"], "consistent AI characters"),
    (("instagram", "hook", "viral", "content machine"), ["r/InstagramMarketing", "r/socialmedia", "r/Entrepreneur"], "social media hooks"),
    (("linkedin",),                ["r/linkedin", "r/marketing", "r/Entrepreneur"], "LinkedIn content system"),
    (("email", "subject"),         ["r/copywriting", "r/Emailmarketing", "r/marketing"], "email subject lines"),
    (("freelanc", "proposal"),     ["r/freelance", "r/Upwork", "r/Entrepreneur"], "freelance proposals"),
    (("notion", "habit"),          ["r/Notion", "r/productivity", "r/getdisciplined"], "Notion productivity system"),
    (("cv", "resume"),             ["r/resumes", "r/jobs", "r/cscareerquestions"], "ATS resume templates"),
    (("seo",),                     ["r/SEO", "r/blogging", "r/juststart"], "SEO checklist for blogs"),
    (("side hustle", "business"),  ["r/sidehustle", "r/Entrepreneur", "r/juststart"], "side hustle starter"),
    (("prompt", "vault", "gemini", "llm"), ["r/ChatGPT", "r/PromptEngineering", "r/artificial"], "AI prompt engineering"),
]
DEFAULT_SUBS = ["r/Entrepreneur", "r/SideProject", "r/digitalnomad"]
DEFAULT_KW = "AI productivity templates"


def channels_for(name: str):
    n = name.lower()
    for keys, subs, kw in CHANNELS:
        if any(k in n for k in keys):
            return subs, kw
    return DEFAULT_SUBS, DEFAULT_KW


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:50]


def resolve_product(con, selector: str):
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT id, name, formatted_price, short_url, sales_count, price_cents, description "
        "FROM products WHERE published=1 AND price_cents > 99"
    ).fetchall()
    if not rows:
        sys.exit("No published, paid products found. Run: python3 db/sync.py")
    if selector == "best":
        # best seller; if nothing has sold yet, the flagship (priciest) product
        return sorted(rows, key=lambda r: (r["sales_count"] or 0, r["price_cents"] or 0))[-1]
    for r in rows:
        if r["id"] == selector:
            return r
    matches = [r for r in rows if selector.lower() in r["name"].lower()]
    if matches:
        return matches[0]
    sys.exit(f"No product matched {selector!r}. Try 'best', an id, or a name fragment.")


def build_kit(p) -> str:
    name = p["name"]
    price = p["formatted_price"]
    url = p["short_url"] or "https://schephenk.gumroad.com"
    subs, kw = channels_for(name)
    short = name.split(":")[0].split(" - ")[0].strip()

    return f"""# Launch Kit — {name}

**Product:** {name}  ·  **Price:** {price}  ·  **URL:** {url}  ·  **Code:** {CODE} (30% off)
Lifetime sales so far: {p['sales_count'] or 0}

> Goal: get this in front of real buyers. The social bots reach almost no one —
> these channels are where purchases actually come from. Post value first; the
> link is the P.S., not the pitch.

---

## 1. Reddit (highest-intent free traffic)

**Where:** {", ".join(subs)}  ·  *(read each sub's self-promo rules first; lead with value, comment for a week before posting a link)*

**Title options:**
- I spent way too long figuring out {kw}; here's the system that finally worked
- After 50+ attempts at {kw}, these are the only steps that mattered
- A no-fluff {kw} checklist (what I wish I'd had on day one)

**Body (paste, then trim to your voice):**
Most advice on {kw} is either vague or trying to sell you something. So here's the actual workflow I use, free:

1. [give 3–5 genuinely useful, specific steps from the product — teach, don't tease]
2. ...
3. ...

This took months to refine. I packaged the full version (templates + every step done-for-you) as "{short}" if you want the shortcut instead of rebuilding it — link in a comment so I'm not breaking the spirit of the sub. Happy to answer anything in the thread.

*(First comment:)* For anyone who asked — it's here: {url} (code {CODE} = 30% off this week). But the steps above are the core; you can do this without buying anything.

---

## 2. Product Hunt

**Tagline (≤60 chars):** {short} — {kw} without the guesswork
**Description:** {short} is a done-for-you {kw} kit: everything you need, ready to use, {price} once (no subscription). Built for makers who'd rather ship than research.
**Topics:** Artificial Intelligence, Productivity, Marketing
**First maker comment:** I kept rebuilding the same {kw} workflow from scratch, so I packaged it once and for all. Launch code {CODE} takes 30% off today. Feedback very welcome — what would make it a no-brainer for you?

---

## 3. SEO article (compounding free traffic)

**Target keyword:** {kw}
**Title tag (≤60 chars):** {kw.title()}: A Practical 2026 Guide
**Meta description (≤155 chars):** A step-by-step {kw} guide for 2026 — the exact workflow, templates, and a shortcut kit if you want it done for you.
**H2 outline:**
- What most people get wrong about {kw}
- The {kw} workflow, step by step
- Templates & tools that save the most time
- Common mistakes (and how to avoid them)
- FAQ
**Soft CTA (end of article):** If you'd rather not build this from scratch, "{short}" packages the whole system: {url}

---

## 4. Email to your list (the asset that compounds)

**Subject A:** the {kw} shortcut I promised
**Subject B:** done-for-you: {short}
**Body:**
Quick one. I just released "{short}" — the full {kw} system, ready to use.
No subscription, {price} once, yours forever.
This week only: code {CODE} takes 30% off → {url}
Reply if you have questions; I read every one.

---

## 5. X / Twitter thread (5 posts)

1. Most {kw} advice is vague. Here's the exact system I use, in 4 steps. 🧵
2. Step 1: [specific, useful tip from the product]
3. Step 2: [specific, useful tip]
4. Step 3–4: [specific, useful tips]
5. If you want it done-for-you (templates + every step), I packaged it as "{short}": {url} — code {CODE} = 30% off this week.

---

*Generated by scripts/launch_kit.py — fill the [bracketed] spots with 1–2 real, specific tips from the product before posting. Specificity is what converts.*
"""


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    selector = argv[0]
    write = "--write" in argv
    con = sqlite3.connect(str(DB_PATH))
    p = resolve_product(con, selector)
    con.close()
    kit = build_kit(p)
    print(kit)
    if write:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        out = OUT_DIR / f"{slugify(p['name'])}.md"
        out.write_text(kit, encoding="utf-8")
        print(f"\n[saved] {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
