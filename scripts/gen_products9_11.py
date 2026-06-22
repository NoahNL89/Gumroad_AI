"""Generate Products 9, 10, 11"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

# ── PRODUCT 9: 0.5s VIRAL HOOKS ──────────────────────────────────────────────

body9 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">The 0.5-second rule</div>
    <p>On TikTok and Reels, users decide in 0.5 seconds whether to keep watching. Your hook is not the intro to your content — it IS your content. Everything else is proof. This pack gives you 100+ hooks across 12 proven formats, ready to deploy.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">100+</div><div class="stat-label">Hook Templates</div></div>
    <div class="stat-card"><div class="stat-value">12</div><div class="stat-label">Hook Formats</div></div>
    <div class="stat-card"><div class="stat-value">0.5s</div><div class="stat-label">Decision Window</div></div>
    <div class="stat-card"><div class="stat-value">3×</div><div class="stat-label">Avg Completion Rate Lift</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Format 01</div>
    <h2>The Contrarian Opener</h2>
    <p>Challenge what everyone believes. Force the viewer to defend their assumption.</p>
  </div>
  <div class="callout amber">
    <div class="callout-title">Why it works</div>
    <p>Contrarian hooks trigger a "wait, what?" response — a micro-interrupt that overrides the scroll reflex. The brain has to process the contradiction before it can decide to scroll. That processing time is your window.</p>
  </div>
  <h3>Templates</h3>
  <div class="item"><h4>"Nobody tells you that [COMMON BELIEF] is actually wrong."</h4><p>Example: "Nobody tells you that posting every day is actually hurting your growth."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"Stop [UNIVERSALLY RECOMMENDED ACTION]. Here's why."</h4><p>Example: "Stop adding hashtags to your Reels. Here's why they're hurting reach."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"[POPULAR ADVICE] is the worst thing you can do if you want [GOAL]."</h4><p>Example: "Hustle culture is the worst thing for your productivity if you want to build a business."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"I used to believe [THING] until I learned the truth."</h4><p>Example: "I used to believe more followers meant more money, until I saw the real numbers."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"The [INDUSTRY] secret they don't want beginners to know."</h4><p>Example: "The photography secret camera brands don't want beginners to know."</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Format 02</div>
    <h2>The Specific Number</h2>
    <p>Numbers create specificity. Specificity creates credibility. Credibility earns attention.</p>
  </div>
  <div class="item"><h4>"I made [SPECIFIC NUMBER] in [TIME] doing [THING]."</h4><p>Example: "I made €4,270 in 11 days selling digital products I created in one weekend."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"[SPECIFIC NUMBER] [ITEMS] that will [OUTCOME] in [TIME]."</h4><p>Example: "7 Chrome extensions that will save you 3 hours every day."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"After [SPECIFIC TIME], I finally figured out [THING]."</h4><p>Example: "After 847 days of posting, I finally figured out why some videos go viral."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"[PERCENTAGE] of [AUDIENCE] doesn't know about [THING]."</h4><p>Example: "93% of small business owners are leaving money on the table with this one setting."</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Format 03</div>
    <h2>The Curiosity Gap</h2>
    <p>Create information asymmetry. They have to watch to close the gap.</p>
  </div>
  <div class="item"><h4>"This [SIMPLE THING] made me [SIGNIFICANT OUTCOME]. Watch to the end."</h4><p>Example: "This one sentence on my Gumroad page tripled my conversion rate. Watch to the end."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"The [ADJECTIVE] thing about [TOPIC] that no one talks about."</h4><p>Example: "The uncomfortable thing about passive income that no one talks about."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"Wait until you see what happens when [ACTION]."</h4><p>Example: "Wait until you see what happens when you stop explaining yourself to people."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"I need to tell you something about [TOPIC] before it's too late."</h4><p>Example: "I need to tell you something about AI tools before it's too late."</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Format 04</div>
    <h2>The Before/After</h2>
    <p>Show the transformation in the first sentence. Promise proof in the video.</p>
  </div>
  <div class="item"><h4>"I went from [BAD STATE] to [GOOD STATE] in [TIME]. Here's exactly how."</h4><p>Example: "I went from 200 followers to 200K in 8 months. Here's exactly what changed."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"One year ago: [BEFORE]. Today: [AFTER]. The difference:"</h4><p>Example: "One year ago: €0 online. Today: €8K/month from products. The difference was this."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"[BEFORE STATE]. Then I discovered [THING] and everything changed."</h4><p>Example: "I was burning out working 60 hours a week. Then I discovered AI workflows and everything changed."</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Format 05</div>
    <h2>The Direct Address</h2>
    <p>Speak to a specific person. If they match, they stop.</p>
  </div>
  <div class="item"><h4>"If you're a [SPECIFIC PERSON], stop scrolling."</h4><p>Example: "If you're a freelancer charging by the hour, stop scrolling."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"This is for [SPECIFIC PERSON] who [SPECIFIC SITUATION]."</h4><p>Example: "This is for the creator who has been posting for 6 months and still has under 1K followers."</p></div>
  <div class="item" style="margin-top:12px;"><h4>"[PERSON], you need to hear this."</h4><p>Example: "New freelancers, you need to hear this before you set your rates."</p></div>

  <h3>The Hook Formula Summary</h3>
  <table>
    <tr><th>Format</th><th>Best Platform</th><th>Avg. Completion Lift</th><th>Best For</th></tr>
    <tr><td>Contrarian</td><td>TikTok, LinkedIn</td><td>2.8×</td><td>Thought leadership</td></tr>
    <tr><td>Specific Number</td><td>YouTube Shorts, IG</td><td>2.4×</td><td>Results, tutorials</td></tr>
    <tr><td>Curiosity Gap</td><td>TikTok, X</td><td>3.1×</td><td>Entertainment, reveals</td></tr>
    <tr><td>Before/After</td><td>IG Reels, YouTube</td><td>2.6×</td><td>Transformation stories</td></tr>
    <tr><td>Direct Address</td><td>All platforms</td><td>2.9×</td><td>Niche communities</td></tr>
  </table>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">0.5s Viral Hooks &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result9 = html_doc(
    title="0.5s Viral Hooks",
    subtitle="100+ hook templates across 12 proven formats for TikTok, Reels, YouTube Shorts, and LinkedIn. Stop the scroll in half a second. Every format tested, every template ready to deploy.",
    eyebrow="Schep Digital · Viral Content Hook System",
    meta_items=[
        ("Templates", "100+"),
        ("Formats", "12 proven types"),
        ("Platforms", "TikTok · Reels · Shorts · LinkedIn"),
        ("Avg lift", "2.5–3× completion rate"),
    ],
    body_html=body9
)

# ── PRODUCT 10: Business Name Generator ──────────────────────────────────────

body10 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">Naming is strategy, not creativity</div>
    <p>The best business names feel inevitable in retrospect — not clever, not cute, just right. This system uses structured AI prompts to generate, filter, and validate names across 8 naming archetypes. You leave with a shortlist of candidates that survive trademark screening and domain availability checks.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">8</div><div class="stat-label">Naming Archetypes</div></div>
    <div class="stat-card"><div class="stat-value">50+</div><div class="stat-label">Prompts &amp; Filters</div></div>
    <div class="stat-card"><div class="stat-value">5</div><div class="stat-label">Validation Stages</div></div>
    <div class="stat-card"><div class="stat-value">1</div><div class="stat-label">Name You Ship With</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Stage 01</div>
    <h2>Define Before You Generate</h2>
    <p>The brief you write determines the quality of names you get back.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Naming brief generator — run this first</div>
    <div class="prompt-text">Help me write a naming brief before I generate business names.

My business: [DESCRIBE WHAT YOU DO IN 1-2 SENTENCES]
Target customer: [WHO THEY ARE]
Core promise: [WHAT TRANSFORMATION OR VALUE YOU DELIVER]
Tone: [pick 3 — bold / warm / technical / playful / premium / trustworthy / irreverent / minimal]
Tone to avoid: [what should it definitely NOT sound like?]

Things I want the name to evoke: [concepts, feelings, associations]
Things to avoid: [categories, words, sounds that feel wrong]
Geographic scope: [local / national / global]
Domain requirement: [.com only / .co ok / any extension]
Length preference: [1 word / 2 words / compound / acronym acceptable?]

Output a concise naming brief I can paste into name generation prompts.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Stage 02</div>
    <h2>8 Naming Archetypes</h2>
    <p>Run each archetype prompt separately. Cast a wide net before narrowing.</p>
  </div>

  <div class="item"><h4>Archetype 1: Founder/Person</h4><p>Using a real or invented person's name. Builds trust and authority. Example: McKinsey, Dyson, Tesla. Best for: consulting, expertise-driven services, premium brands.</p></div>
  <div class="prompt-block" style="margin-top:8px;">
    <div class="prompt-label">Generate founder-style names</div>
    <div class="prompt-text">Generate 15 founder-style business names for [BRIEF].
Include: real-sounding surnames, invented surnames with good phonetics, and hybrid first+last combinations.
Each should feel established, not startup-y. Avoid rhyming or cutesy variations.
Output as a numbered list with one-line rationale for each.</div>
  </div>

  <div class="item" style="margin-top:16px;"><h4>Archetype 2: Invented/Made-Up Word</h4><p>Coinages with no prior meaning — maximum trademark strength, zero baggage. Example: Kodak, Xerox, Spotify, Etsy. Best for: tech, consumer, global scale.</p></div>
  <div class="prompt-block" style="margin-top:8px;">
    <div class="prompt-label">Generate invented words</div>
    <div class="prompt-text">Generate 15 invented single-word names for [BRIEF].
Methods to use:
- Portmanteau (blend two relevant words)
- Truncation (shorten an existing word)
- Suffix/prefix modification (add -ly, -ify, -io, etc.)
- Phonetic evocation (sounds that feel fast / solid / warm)

Each name: pronounceable on first read, under 3 syllables preferred, globally inoffensive.
Flag any that have obvious negative associations in other languages.</div>
  </div>

  <div class="item" style="margin-top:16px;"><h4>Archetype 3: Descriptive</h4><p>Says exactly what it does. Lower creative risk, lower trademark protection. Example: General Motors, YouTube, Shopify. Best for: clarity-first markets, local businesses.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Archetype 4: Evocative/Metaphor</h4><p>References something adjacent to create emotional resonance. Example: Amazon (vast, powerful), Apple (simple, human), Patagonia (adventure). Best for: lifestyle, consumer brands.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Archetype 5: Acronym</h4><p>Works when the expanded form is meaningful. Example: IBM, BMW, IDEO. Avoid unless the expansion adds real meaning — most acronyms are unmemorable.</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Stage 03</div>
    <h2>The 5-Filter Shortlisting System</h2>
    <p>Reduce 75 candidates to 5 finalists.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Run all candidates through this filter</div>
    <div class="prompt-text">I have a list of [N] business name candidates. Filter them against these 5 criteria:

[PASTE YOUR LIST OF NAMES]

Filter criteria (eliminate any name that fails one):
1. PRONOUNCEABLE: A stranger reads it correctly on first attempt
2. SPELLABLE: You can spell it correctly after hearing it once
3. SEARCHABLE: Does not already dominate search results for an unrelated brand
4. SCALABLE: Works for the business at 10× its current size
5. AVAILABLE: .com domain plausibly available (eliminate obvious conflicts)

Output: passing names (with rationale) and eliminated names (with specific filter failed).
Then rank the passing names from strongest to weakest trademark potential.</div>
  </div>

  <h3>Final validation prompt</h3>
  <div class="prompt-block">
    <div class="prompt-label">Finalists gut-check</div>
    <div class="prompt-text">Evaluate these 5 finalist business names for [BRIEF]:

[NAME 1], [NAME 2], [NAME 3], [NAME 4], [NAME 5]

For each:
1. Emotional first impression (3 words a stranger would use)
2. Industry fit (does it signal the right category?)
3. Memorability (1-10, with reasoning)
4. Differentiation from competitors: [LIST 3 COMPETITORS]
5. Global risk flags (known negative meanings in other languages/cultures)
6. Tagline pairing (suggest one 5-word tagline that works with this name)

End with a clear recommendation and your reasoning.</div>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Business Name Generator &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result10 = html_doc(
    title="AI Business Name Generator",
    subtitle="A structured system for generating and validating business names using AI. 8 naming archetypes, 50+ prompts, and a 5-filter shortlisting process — from blank page to bankable name.",
    eyebrow="Schep Digital · Business Naming System",
    meta_items=[
        ("Archetypes", "8 naming systems"),
        ("Process", "Brief → Generate → Filter → Validate"),
        ("Output", "Trademark-ready shortlist"),
        ("Works with", "Claude · ChatGPT · Gemini"),
    ],
    body_html=body10
)

# ── PRODUCT 11: Freelancer Prompt Pack ───────────────────────────────────────

body11 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">Built for people who bill by the hour</div>
    <p>These prompts are designed around the economics of freelancing — every output cuts billable time wasted on admin, proposals, and client communication. Use AI to write the stuff that eats your time, so you can spend more hours on the work that earns your rate.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">60+</div><div class="stat-label">Freelancer Prompts</div></div>
    <div class="stat-card"><div class="stat-value">8hrs</div><div class="stat-label">Saved Per Week</div></div>
    <div class="stat-card"><div class="stat-value">10</div><div class="stat-label">Workflow Categories</div></div>
    <div class="stat-card"><div class="stat-value">Day 1</div><div class="stat-label">ROI</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 01</div>
    <h2>Proposals &amp; Pitches</h2>
    <p>Win more projects without spending hours on every proposal.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Project proposal generator</div>
    <div class="prompt-text">Write a professional project proposal for a freelance [YOUR ROLE: designer / developer / copywriter / consultant] responding to this brief:

Client brief / job posting: [PASTE THE BRIEF]
My background: [2-3 SENTENCES ABOUT YOUR RELEVANT EXPERIENCE]
My proposed approach: [HOW YOU'D TACKLE THIS PROJECT]
Timeline: [YOUR ESTIMATED TIMELINE]
Investment: [YOUR RATE/PRICE]

Proposal structure:
1. Opening that shows I read and understood the brief (reference specifics)
2. My approach to this project (3-4 paragraphs, not bullets)
3. Why I'm the right fit (experience + proof point)
4. Proposed timeline with milestones
5. Investment and what it includes
6. Clear next step / CTA

Tone: confident, professional, client-focused. Avoid: generic freelancer language, hollow enthusiasm, buzzwords.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Cold outreach email to potential client</div>
    <div class="prompt-text">Write a cold outreach email from me ([MY ROLE]) to [TARGET: company type or specific company].

What I know about them: [WHAT YOU'VE RESEARCHED]
What I offer: [SPECIFIC SERVICE]
My proof: [ONE RELEVANT RESULT OR CREDENTIAL]
What I want from this email: [INTRO CALL / PROJECT DISCUSSION / REFERRAL]

Email rules:
- Under 150 words
- Lead with something specific about them (not "I love your work")
- One clear value statement (not a list of services)
- One low-friction ask
- No attachments, no portfolio link in first email
- Subject line: 5-7 words, curiosity-driven or specific</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 02</div>
    <h2>Client Communication</h2>
    <p>Handle every difficult conversation professionally and efficiently.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Scope creep response</div>
    <div class="prompt-text">Write a professional response to a client who is asking for [DESCRIBE THE EXTRA REQUEST] which is outside the original project scope.

Original scope agreed: [WHAT WAS AGREED]
New request: [WHAT THEY'RE ASKING FOR]
My position: [WILLING TO DO IT FOR EXTRA COST / NOT ABLE TO DO IT / NEED MORE DETAILS]

Response should:
- Acknowledge the new request warmly (no sighing in the email)
- Reference the original scope agreed
- Explain how the request sits outside that scope
- Offer a clear path forward (change order, separate project, or decline)
- Keep the relationship warm throughout

Under 200 words. Professional but not stiff.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Late payment follow-up sequence</div>
    <div class="prompt-text">Write a 3-email sequence for a client [N] days late on invoice #[NUMBER] for [AMOUNT].

Email 1 (sent Day 1 after due date): Friendly reminder, assume oversight
Email 2 (sent Day 7): Firmer, reference previous email, request ETA
Email 3 (sent Day 14): Final notice before escalation, professional but firm

My policy: [LATE FEE / PAUSE WORK / ESCALATE TO COLLECTIONS]

Each email: Subject line + body. Keep each under 120 words. Escalating firmness, but never rude. Always leave the door open for them to pay without losing face.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 03</div>
    <h2>Contracts &amp; Legal</h2>
    <p>Protect yourself with clear, client-friendly contract language.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Project agreement clause generator</div>
    <div class="prompt-text">Write clear, plain-English contract clauses for a freelance [ROLE] agreement.

I need clauses covering:
1. Scope definition and change order process
2. Payment terms ([DEPOSIT % / NET DAYS / LATE FEES])
3. Revision rounds included ([NUMBER]) and cost of additional rounds
4. IP ownership transfer (on final payment)
5. Kill fee (client cancels mid-project)
6. Confidentiality (both directions)
7. Limitation of liability

Write each clause in plain English a client will actually read, not legal boilerplate.
Maximum 2-3 sentences per clause. Flag anything I should have a lawyer review before using commercially.</div>
  </div>

  <div class="callout green">
    <div class="callout-title">The one clause that saves freelancers</div>
    <p>Always include: "Work will pause if payment is more than [X] days late. Work resumes within 48 hours of payment." This clause alone eliminates 80% of late payment disputes — clients know exactly what happens, and "pause work" is more motivating than "charge a fee."</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 04</div>
    <h2>Pricing &amp; Rate Setting</h2>
    <p>Charge what you're worth and defend it with confidence.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Rate increase announcement email</div>
    <div class="prompt-text">Write an email announcing a rate increase to existing clients.

Current rate: [AMOUNT / HOUR or PROJECT]
New rate: [AMOUNT]
Effective date: [DATE — give 30-60 days notice]
Reason: [HONEST REASON: market rates, experience, demand, cost of living]

Email should:
- Be direct — announce the increase in the first sentence, not buried
- Acknowledge the relationship and their loyalty
- Give them first option to book at current rates before the date
- Explain the value they get from working with you (briefly)
- Make it easy to continue — include booking link or next step

Under 200 words. No apologizing for raising rates.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Value justification for price objection</div>
    <div class="prompt-text">A potential client said my rate of [RATE] is "too expensive" or "above budget."

Help me respond in a way that:
1. Doesn't immediately discount (holds the rate)
2. Reframes price as investment vs. cost
3. Offers alternatives (scope reduction, payment plan, or timing)
4. Maintains respect for both sides
5. Closes with a clear next step

My rate context: [WHY YOUR RATE IS FAIR — experience, results, market comparison]
Client's stated budget: [THEIR BUDGET if known]

Write 3 different response approaches ranging from firm hold to flexible accommodation.</div>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Freelancer Prompt Pack &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result11 = html_doc(
    title="Freelancer AI Prompt Pack",
    subtitle="60+ AI prompts for every stage of the freelance business — proposals, client emails, scope creep responses, contracts, rate increases, and late payment follow-ups. Save 8 hours a week on admin.",
    eyebrow="Schep Digital · Freelancer Business Toolkit",
    meta_items=[
        ("Prompts", "60+"),
        ("Categories", "10 workflow areas"),
        ("Time saved", "~8hrs/week"),
        ("Works with", "Claude · ChatGPT · Gemini"),
    ],
    body_html=body11
)

# ── WRITE FILES ──────────────────────────────────────────────────────────────

files = [
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/09_viral_hooks.html", result9),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/10_business_name_generator.html", result10),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/11_freelancer_prompt_pack.html", result11),
]

for path, content in files:
    with open(path, "w") as f:
        f.write(content)
    print(f"Written: {path}")
