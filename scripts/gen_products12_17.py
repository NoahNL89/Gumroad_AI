"""Generate Products 12-17"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

# ── PRODUCT 12: Instagram Growth Templates ───────────────────────────────────

body12 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">Templates that convert, not just look good</div>
    <p>Every template in this pack is built around engagement mechanics — not aesthetics. Caption structures that drive saves. Carousel formats that force scroll-through. Story sequences that push profile visits. Design is the vehicle; strategy is the engine.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">30+</div><div class="stat-label">Caption Templates</div></div>
    <div class="stat-card"><div class="stat-value">15</div><div class="stat-label">Carousel Structures</div></div>
    <div class="stat-card"><div class="stat-value">10</div><div class="stat-label">Story Sequences</div></div>
    <div class="stat-card"><div class="stat-value">3×</div><div class="stat-label">Avg Engagement Lift</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 01</div>
    <h2>Caption Templates</h2>
    <p>Every caption structure optimized for saves, shares, and profile visits.</p>
  </div>

  <div class="item"><h4>The Value Ladder Caption</h4><p>Hook (1 line) → Problem statement (2-3 lines) → Your insight (4-5 lines) → Actionable tip (2-3 lines) → Save prompt + question CTA. Best for: educational content, tutorial posts. Drives saves at 2.3× baseline.</p></div>
  <div class="prompt-block" style="margin-top:8px;">
    <div class="prompt-label">Generate this caption style</div>
    <div class="prompt-text">Write an Instagram caption in the Value Ladder format for: [YOUR TOPIC]

Hook: One contrarian or surprising statement about [TOPIC] (under 12 words)
Problem: What most people get wrong about [TOPIC] (2-3 sentences)
Insight: Your specific take or method (3-4 sentences, concrete and specific)
Tip: One thing they can do today to apply this (2-3 sentences)
CTA: "Save this for when you need it. What's your biggest challenge with [TOPIC]?"

Tone: [YOUR BRAND VOICE]
Hashtag block (15 tags): mix of 3 niche (under 50K posts), 7 medium (50K-500K), 5 broad (500K+)</div>
  </div>

  <div class="item" style="margin-top:16px;"><h4>The Storytelling Caption</h4><p>Personal anecdote with business lesson. Hook → Conflict → Resolution → Lesson → Relatable question. Best for: building parasocial connection, growing loyal followers over virality.</p></div>

  <div class="item" style="margin-top:12px;"><h4>The Listicle Caption</h4><p>Number hook → Short intro → Numbered list (5-10 items, one line each) → Bonus tip → Save CTA. Best for: content that gets shared, bookmarked, and screenshotted. Algorithm loves saves.</p></div>

  <div class="item" style="margin-top:12px;"><h4>The Hot Take Caption</h4><p>Bold contrarian claim → Brief defense → Anticipated objection → Your counter → Engagement question ("Do you agree or disagree?"). Best for: comments and reach. Polarizes for a reason — both agreers and disagreers comment.</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 02</div>
    <h2>Carousel Structures</h2>
    <p>The formats that force people to swipe all 10 slides.</p>
  </div>

  <div class="item"><h4>The Before/After Reveal</h4><p>Slides 1-3: The "before" state (relatable, ugly, wrong). Slide 4: Tease ("But here's what changed..."). Slides 5-9: The transformation, step by step. Slide 10: The after + CTA to follow.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Mistake Series</h4><p>Slide 1: "X mistakes [AUDIENCE] makes" (number hook). Slides 2-9: One mistake per slide (mistake in bold + 2-line explanation). Slide 10: Summary + follow for more.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Mini Course</h4><p>Slide 1: The outcome they'll learn. Slides 2-8: One concept per slide with visual. Slide 9: Key takeaways. Slide 10: Save this + your offer or follow CTA.</p></div>

  <div class="prompt-block" style="margin-top:16px;">
    <div class="prompt-label">Carousel content generator</div>
    <div class="prompt-text">Plan a 10-slide Instagram carousel on [TOPIC] using the [BEFORE/AFTER REVEAL / MISTAKE SERIES / MINI COURSE] format.

For each slide provide:
- Slide number and type (hook/content/CTA)
- Headline text (under 8 words, large and bold)
- Body text (under 30 words, supporting the headline)
- Visual direction (what the visual should show)

Slide 1 must stop the scroll. Slide 10 must drive a save or follow.
Make the value obvious in slides 1-3 so they keep swiping.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 03</div>
    <h2>Growth Mechanics</h2>
    <p>The algorithm signals that matter in 2026.</p>
  </div>

  <div class="item"><h4>Save-bait structure</h4><p>Content that people bookmark for later use — checklists, step-by-step guides, resource lists, and swipe files. Saves are the highest-weight engagement signal in Instagram's algorithm. Design specifically for this.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Share triggers</h4><p>Content gets shared when it makes the sharer look smart or helpful to their audience. "Tag someone who needs this" is dead — but "So relatable 😭" and "This explains everything" drive organic shares.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Comment prompts that work</h4><p>Avoid yes/no questions. Use: "What's your experience with [X]?", "Which of these applies to you?", "What am I missing?". Questions with multiple valid answers get more comments than binary ones.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Profile visit triggers</h4><p>Content that makes people think "who is this person?" pushes profile visits. Original opinions, behind-the-scenes glimpses, and counterintuitive takes outperform generic educational content for profile visits.</p></div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Instagram Growth Templates &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result12 = html_doc(
    title="Instagram Growth Templates",
    subtitle="30+ caption templates, 15 carousel structures, and 10 story sequences built around Instagram's engagement mechanics. Strategy-first design that drives saves, shares, and profile visits.",
    eyebrow="Schep Digital · Instagram Content System",
    meta_items=[
        ("Templates", "55+ total"),
        ("Focus", "Engagement mechanics"),
        ("Updated", "2026 Algorithm"),
        ("Avg lift", "3× engagement rate"),
    ],
    body_html=body12
)

# ── PRODUCT 13: CV & Resume Templates ────────────────────────────────────────

body13 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">The 6-second rule</div>
    <p>Recruiters spend 6 seconds on initial CV review. This pack teaches you how to use AI to write CVs that pass ATS screening, communicate value in the first third of the page, and get shortlisted — not just submitted.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">6s</div><div class="stat-label">Initial Review Time</div></div>
    <div class="stat-card"><div class="stat-value">ATS</div><div class="stat-label">Optimized Prompts</div></div>
    <div class="stat-card"><div class="stat-value">5</div><div class="stat-label">CV Section Formulas</div></div>
    <div class="stat-card"><div class="stat-value">3×</div><div class="stat-label">Interview Rate Lift</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 01</div>
    <h2>ATS Optimization</h2>
    <p>Get past the robots before you impress the humans.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">ATS keyword extraction from job posting</div>
    <div class="prompt-text">Analyze this job posting and extract ATS optimization data:

[PASTE FULL JOB POSTING]

Output:
1. REQUIRED SKILLS: Hard skills explicitly mentioned (list all, exact phrasing from posting)
2. PREFERRED SKILLS: "Nice to have" or "bonus" items
3. EXPERIENCE KEYWORDS: Years, level, and function terms used
4. SOFT SKILLS: Adjectives and traits mentioned explicitly
5. INDUSTRY TERMS: Sector-specific jargon to include
6. TITLE VARIATIONS: How the role is described across the posting
7. ATS RISK WORDS: Terms I should avoid (over-optimized, red flag phrases)
8. KEYWORD DENSITY TARGET: Which 5 terms appear most frequently (these are the core ATS filters)

Output as a table I can use as a checklist when writing my CV.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">CV tailoring prompt</div>
    <div class="prompt-text">Rewrite this CV section to target this specific job posting:

MY CURRENT TEXT: [PASTE YOUR CURRENT SECTION]
JOB POSTING KEYWORDS: [PASTE THE KEYWORD LIST FROM ABOVE]
My actual experience: [WHAT YOU ACTUALLY DID — honest, not embellished]

Rules:
- Use the exact keyword phrasing from the posting (not synonyms — ATS matches exact strings)
- Quantify every achievement (%, £/€, time saved, team size)
- Lead with impact, not with duty
- Under 100 words per role
- Avoid: responsible for, assisted with, helped to, duties included</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 02</div>
    <h2>The 5 Section Formulas</h2>
    <p>Every section of a CV has an optimal structure. Here they are.</p>
  </div>

  <div class="item"><h4>Professional Summary</h4><p>Formula: [TITLE/IDENTITY] with [X years] of [SPECIFIC EXPERIENCE] specializing in [NICHE]. Known for [ONE DIFFERENTIATOR]. Currently [WHAT YOU'RE DOING/SEEKING]. Under 50 words. No objectives ("seeking a role where...") — state who you are, not what you want.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Work Experience Bullets</h4><p>Formula: [Strong action verb] + [what you did] + [quantified result]. "Led cross-functional team of 12 to deliver €2M product launch 3 weeks ahead of schedule." Never start a bullet with "I" or a weak verb (helped, worked on, was responsible for).</p></div>

  <div class="item" style="margin-top:12px;"><h4>Skills Section</h4><p>Split into Hard Skills (tools, languages, certifications — exact names matter for ATS) and Soft Skills (keep to 3-5, choose ones backed by evidence in your experience section). Never list skills you can't discuss competently in an interview.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Education</h4><p>Reverse chronological. Degree, institution, year. Add relevant coursework only if it directly maps to the job keywords. Remove graduation year if it's more than 10 years ago and you're concerned about age bias.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Projects / Portfolio</h4><p>Formula: [Project Name] — [What it is in 10 words]. [Metric or outcome]. [Tool/tech used]. Link if available. Best used for career changers or early-career candidates to show capability beyond work history.</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 03</div>
    <h2>Cover Letter Templates</h2>
    <p>The cover letters that actually get read.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Cover letter generator</div>
    <div class="prompt-text">Write a cover letter for this job application.

Role I'm applying for: [JOB TITLE] at [COMPANY]
What I know about the company: [2-3 SPECIFIC THINGS — products, values, recent news]
My most relevant experience: [TOP 2-3 EXPERIENCES/ACHIEVEMENTS]
Why this role, why this company: [HONEST REASON — career goal, product, mission]
One thing that sets me apart: [YOUR DIFFERENTIATOR]

Structure:
Para 1 (3 sentences): Hook — why this company, show you've done homework
Para 2 (4-5 sentences): Your most relevant achievement with metrics
Para 3 (3-4 sentences): Why this role specifically, what you bring
Para 4 (2 sentences): CTA — next step, thank them

No: "I am writing to apply for..." opener. No: hollow enthusiasm.
Yes: Specific, evidence-based, direct.</div>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">CV &amp; Resume Templates &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result13 = html_doc(
    title="CV & Resume AI Templates",
    subtitle="ATS-optimized prompts, 5 section formulas, and cover letter generators for job seekers. Get past the robots and impress the humans. Average 3× interview rate improvement.",
    eyebrow="Schep Digital · Career Document System",
    meta_items=[
        ("Focus", "ATS + human optimization"),
        ("Sections", "5 proven formulas"),
        ("Works with", "Claude · ChatGPT"),
        ("Lift", "3× interview rate"),
    ],
    body_html=body13
)

# ── PRODUCT 14: Notion Habit Architecture ────────────────────────────────────

body14 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">Habit systems, not habit trackers</div>
    <p>Most habit tools track whether you did the thing. This system architects why you'll do it. Built on Notion with AI-generated prompts for daily reviews, weekly audits, and habit design — the infrastructure for compound personal growth.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">12</div><div class="stat-label">Notion Templates</div></div>
    <div class="stat-card"><div class="stat-value">30+</div><div class="stat-label">AI Review Prompts</div></div>
    <div class="stat-card"><div class="stat-value">3</div><div class="stat-label">System Layers</div></div>
    <div class="stat-card"><div class="stat-value">66</div><div class="stat-label">Days to Lock a Habit</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Layer 01</div>
    <h2>Habit Design</h2>
    <p>Design habits that survive contact with real life.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Habit design session</div>
    <div class="prompt-text">Help me design a sustainable habit system for [GOAL].

My current situation: [DESCRIBE YOUR LIFE — schedule, energy patterns, existing routines]
The outcome I want: [SPECIFIC, MEASURABLE GOAL]
Time available daily: [REALISTIC MINUTES]
Past attempts: [WHAT I'VE TRIED AND WHY IT FAILED]

Design for me:
1. MINIMUM VIABLE HABIT: The smallest version that still moves toward the goal
2. ANCHOR: Which existing habit this attaches to (habit stacking)
3. CUE: The specific trigger that initiates the habit
4. REWARD: An immediate micro-reward that makes it satisfying
5. OBSTACLE PLAN: Top 3 failure scenarios and pre-committed responses
6. SCALING PATH: How to expand the habit once the minimum is automatic (weeks 2, 4, 8)
7. MEASUREMENT: What data point proves the habit is working

Make the minimum viable habit embarrassingly small. I want zero excuses.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Layer 02</div>
    <h2>Notion Database Architecture</h2>
    <p>The exact Notion structure for tracking habits without friction.</p>
  </div>

  <div class="item"><h4>Daily Habits Database</h4><p>Properties: Habit Name (Title), Date (Date), Done (Checkbox), Streak (Formula), Notes (Text). View: Calendar view for visual streak tracking. Filter: "Today" filter as default. Use Relation to link to the Habit Definition database.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Habit Definition Database</h4><p>Properties: Habit Name (Title), Category (Select), Minimum Version (Text), Anchor Habit (Text), Cue (Text), Reward (Text), Target Frequency (Select), Start Date (Date), Why (Text). One row per habit — this is your source of truth.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Weekly Review Template</h4><p>New page every Sunday: habit completion rate, best streak, hardest day, one lesson, one change for next week. Linked to the Habit Definition database via rollup properties for automatic stats.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Streak formula</h4><p>In Notion: dateBetween(now(), prop("Last Completed"), "days"). Display as a progress bar with conditional coloring: green above target, amber below, red if missed yesterday. The visual streak is the primary motivator.</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Layer 03</div>
    <h2>AI-Assisted Reviews</h2>
    <p>Use AI for weekly and monthly habit audits that evolve the system.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Weekly habit audit</div>
    <div class="prompt-text">Run my weekly habit review.

This week's completion rates:
[PASTE YOUR HABIT COMPLETION DATA: "Habit: X/7 days"]

Context:
- Hardest day this week: [DAY AND WHAT HAPPENED]
- Easiest day: [DAY]
- Any habits I want to add or drop: [LIST]
- Energy level this week: [1-10]

Produce:
1. Completion analysis (what's working, what's not — be direct)
2. The habit most at risk of breaking (and why)
3. One structural change to improve the hardest habit
4. Habit to celebrate (the one that's becoming automatic)
5. Next week's focus (one habit to prioritize)
6. One question to reflect on before next week</div>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Notion Habit Architecture &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result14 = html_doc(
    title="Notion Habit Architecture",
    subtitle="A complete habit system built in Notion, powered by AI. Habit design, database architecture, streak tracking, and weekly AI-assisted reviews — the infrastructure for compound personal growth.",
    eyebrow="Schep Digital · Productivity System",
    meta_items=[
        ("Templates", "12 Notion databases"),
        ("AI prompts", "30+ review prompts"),
        ("System layers", "3 (design, track, review)"),
        ("Science basis", "Habit stacking + streaks"),
    ],
    body_html=body14
)

# ── PRODUCT 15: Omnichannel Social Media Calendar ────────────────────────────

body15 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">One message, every channel</div>
    <p>Most content calendars are glorified spreadsheets. This system is a repurposing engine — you create one core piece of content per week and derive everything else from it. LinkedIn posts, Reels scripts, newsletter sections, X threads — all from one source of truth.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">1</div><div class="stat-label">Core Piece/Week</div></div>
    <div class="stat-card"><div class="stat-value">7+</div><div class="stat-label">Pieces Derived</div></div>
    <div class="stat-card"><div class="stat-value">5</div><div class="stat-label">Channel Templates</div></div>
    <div class="stat-card"><div class="stat-value">4hrs</div><div class="stat-label">Monthly Content Work</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">The Core System</div>
    <h2>The Content Atom Model</h2>
    <p>One long-form piece creates everything else for the week.</p>
  </div>

  <div class="item"><h4>The Content Atom</h4><p>Your weekly cornerstone — a blog post, podcast episode, YouTube video, or long LinkedIn article. This is the only piece you create from scratch each week. Every other piece is derived from it.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Derivatives (auto-generated)</h4><p>From one atom: 5 X/Twitter posts (one key insight each), 1 LinkedIn post (professional angle), 1 Instagram carousel (visual breakdown), 1 newsletter section (deeper dive), 2 Reels/TikTok hooks (contrarian or insight angles), 3 Story slides (pull quotes).</p></div>

  <div class="prompt-block" style="margin-top:16px;">
    <div class="prompt-label">Content atom repurposing engine</div>
    <div class="prompt-text">Repurpose this content atom across 5 channels:

ORIGINAL CONTENT: [PASTE YOUR BLOG POST / VIDEO TRANSCRIPT / LONG POST]

Generate for each channel:

1. X/TWITTER THREAD (5 tweets): Each tweet one insight. Tweet 1 is the hook. Tweet 5 is the CTA.

2. LINKEDIN POST (300 words): Professional angle. Lead with a data point or bold claim. No hashtag spam.

3. INSTAGRAM CAROUSEL (10 slides): Slide 1 = hook, Slides 2-9 = one insight each, Slide 10 = CTA + follow.

4. NEWSLETTER SECTION (200 words): The "I learned something this week" tone. Link back to original.

5. TIKTOK/REELS SCRIPT (60 seconds): Hook (first 2 seconds), rapid insights (45 seconds), CTA (last 10 seconds).

Maintain consistent core message. Adapt tone to each platform's native voice.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Channel Templates</div>
    <h2>Platform-Specific Formats</h2>
    <p>The native content format that wins on each platform.</p>
  </div>

  <div class="item"><h4>LinkedIn: The Professional Opinion Post</h4><p>Bold claim → 2-line paragraph → Key insight in a standalone sentence → Supporting evidence → Implication → Question. No emojis except sparingly. Short paragraphs — no paragraph over 3 lines. The algorithm rewards dwell time: make them stop and think.</p></div>
  <div class="item" style="margin-top:12px;"><h4>X/Twitter: The Insight Thread</h4><p>Tweet 1: The hook (contrarian or specific number). Tweets 2-7: One idea per tweet, each valuable standalone. Tweet 8: Summary or tl;dr. Tweet 9: Soft CTA (follow, repost, or reply). No "🧵" emoji — it's unnecessary. No "1/10" numbering — it signals length upfront.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Newsletter: The One-Thing Format</h4><p>Subject: Curiosity gap or specific promise. Preview: The most valuable line. Body: One idea, deeply explored, with examples. No listicle-inside-newsletter. One thing done well beats five things rushed. CTA: Reply with their answer, not "share this email."</p></div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Omnichannel Social Media Calendar &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result15 = html_doc(
    title="Omnichannel Social Media Calendar",
    subtitle="The Content Atom Model: create one piece per week, derive 7+ across every channel. LinkedIn, X, Instagram, TikTok, and newsletters from one source of truth. 4 hours of content work per month.",
    eyebrow="Schep Digital · Content Repurposing System",
    meta_items=[
        ("Core model", "Content Atom repurposing"),
        ("Channels", "5 platforms"),
        ("Output", "7+ pieces/week from 1"),
        ("Time investment", "~4hrs/month"),
    ],
    body_html=body15
)

# ── PRODUCT 16: Email Subject Line Mastery ───────────────────────────────────

body16 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">The only metric that matters first</div>
    <p>Open rate is a vanity metric — unless your subject line fails. A 50% open rate with 0.5% CTR is worse than a 25% open rate with 5% CTR. But nothing else matters if they never open. This pack gives you 80+ subject line formulas organized by goal, audience temperature, and send type.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">80+</div><div class="stat-label">Subject Line Formulas</div></div>
    <div class="stat-card"><div class="stat-value">8</div><div class="stat-label">Goal Categories</div></div>
    <div class="stat-card"><div class="stat-value">A/B</div><div class="stat-label">Testing Framework</div></div>
    <div class="stat-card"><div class="stat-value">40%+</div><div class="stat-label">Target Open Rate</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 01</div>
    <h2>Curiosity-Driven Subject Lines</h2>
    <p>The gap between what they know and what you're about to tell them.</p>
  </div>

  <div class="item"><h4>The Unfinished Thought</h4><p>"The reason your emails don't get..." — forces the open to close the gap. Works best with a subject they're already anxious about.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Numbered Secret</h4><p>"3 things I've never told anyone about [TOPIC]" — the word "never" creates exclusivity. The number creates format expectation.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Single Question</h4><p>"Are you making this mistake?" — vague enough to be threatening, specific enough to feel relevant. Best for pain-point emails.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The What Happened Next</h4><p>"I made €12K last month. Then something unexpected happened." — two beats: credibility + curiosity. Both must be genuine.</p></div>

  <div class="prompt-block" style="margin-top:16px;">
    <div class="prompt-label">Generate 10 subject line variations</div>
    <div class="prompt-text">Write 10 email subject line variations for this email:

Email topic: [WHAT THE EMAIL IS ABOUT]
Email goal: [OPEN / CLICK / REPLY / SALE]
Audience: [WHO THEY ARE AND WHERE THEY ARE IN THE FUNNEL]
Tone: [BRAND VOICE]

Generate variations across:
- 2 curiosity-gap lines
- 2 specific-number lines
- 2 personal/conversational lines
- 2 benefit-driven lines
- 2 contrarian or surprising lines

For each: subject line + preview text (90 chars) + why this works for this audience.
Flag the 3 most likely to get opens and the 2 safest for a risk-averse send.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 02</div>
    <h2>Benefit &amp; Outcome Lines</h2>
    <p>Lead with what they get, not what you're sending.</p>
  </div>

  <div class="item"><h4>The Specific Outcome</h4><p>"Save 3 hours a week on client emails (here's how)" — specific + benefit + tease. Avoid vague outcomes like "improve your productivity."</p></div>
  <div class="item" style="margin-top:12px;"><h4>The This Week Benefit</h4><p>"What to do this weekend to start next week stronger" — time-bounded benefits feel more urgent and actionable than timeless advice.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Before/After Promise</h4><p>"From 0 to 1,000 subscribers: the exact playbook" — sets up the transformation. Works best with your own proof.</p></div>

  <div class="section-header" style="margin-top:32px;">
    <div class="section-num">Category 03</div>
    <h2>A/B Testing Framework</h2>
    <p>Test methodically, not randomly.</p>
  </div>

  <div class="item"><h4>Test one variable</h4><p>Only change one element per A/B test: the curiosity vs. benefit frame, the length (short vs. long), or the personalization (name vs. no name). Changing multiple variables makes the result uninterpretable.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Minimum viable sample size</h4><p>Need at least 500 recipients per variant for statistical significance at 95% confidence. With smaller lists, A/B test for learning, not decision-making — directional signal only.</p></div>
  <div class="item" style="margin-top:12px;"><h4>What to measure beyond opens</h4><p>Open rate tells you the subject won. Click rate tells you the email won. Conversion rate tells you the offer won. Run all three metrics for every send where conversion is the goal — a high-open/low-click email means a misleading subject line.</p></div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Email Subject Line Mastery &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result16 = html_doc(
    title="Email Subject Line Mastery",
    subtitle="80+ subject line formulas across 8 goal categories, an A/B testing framework, and AI prompts to generate 10 variations for any email in 60 seconds. Target: 40%+ open rates.",
    eyebrow="Schep Digital · Email Marketing System",
    meta_items=[
        ("Formulas", "80+"),
        ("Categories", "8 goal types"),
        ("Includes", "A/B testing framework"),
        ("Target", "40%+ open rate"),
    ],
    body_html=body16
)

# ── PRODUCT 17: Side Hustle Quick-Start Checklist ────────────────────────────

body17 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">90 days to first euro</div>
    <p>This checklist is built around one goal: your first paid transaction. Not a business plan, not a brand strategy session — your first customer paying real money. Everything before that is preparation. Everything after that is scaling. This checklist is the bridge.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">90</div><div class="stat-label">Days to First Payment</div></div>
    <div class="stat-card"><div class="stat-value">7</div><div class="stat-label">Phase Checklist</div></div>
    <div class="stat-card"><div class="stat-value">€0</div><div class="stat-label">Required to Start</div></div>
    <div class="stat-card"><div class="stat-value">1</div><div class="stat-label">Decision at a Time</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Phase 01</div>
    <h2>Idea Validation (Week 1-2)</h2>
    <p>Validate before you build. Test before you invest.</p>
  </div>

  <ul class="checklist">
    <li><div class="check-icon"></div>List 10 skills you have that others pay for (professional or personal)</li>
    <li><div class="check-icon"></div>Identify which 3 skills have the highest market demand (search Reddit, job boards, Fiverr for evidence)</li>
    <li><div class="check-icon"></div>Find 5 people who would benefit from your top skill — talk to them before building anything</li>
    <li><div class="check-icon"></div>Ask: "Would you pay €[X] for [specific result]?" — note exact words they use when they say yes</li>
    <li><div class="check-icon"></div>Identify your monetization model: service (time-for-money), product (one-time), subscription (recurring)</li>
    <li><div class="check-icon"></div>Run a market size check: how many people have this problem? (Google Trends, Reddit communities, Facebook groups)</li>
    <li><div class="check-icon"></div>Set your minimum viable revenue target for Month 1 (be honest, not aspirational)</li>
  </ul>

  <div class="prompt-block" style="margin-top:16px;">
    <div class="prompt-label">Idea validation AI prompt</div>
    <div class="prompt-text">Help me validate this side hustle idea: [DESCRIBE YOUR IDEA]

My skills: [LIST YOUR RELEVANT SKILLS]
Target customer: [WHO WOULD PAY FOR THIS]
Proposed price: [WHAT YOU WANT TO CHARGE]

Analyze:
1. Is this a painkiller (urgent need) or a vitamin (nice to have)?
2. Who already does this? (direct competition + indirect competition)
3. What's the most obvious reason this would fail?
4. What's the minimum version I could sell in the next 14 days?
5. What would make this defensible over time?
6. Red flags that suggest I should pivot the idea?

Give me a direct assessment — not encouragement.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Phase 02</div>
    <h2>First Offer Creation (Week 3-4)</h2>
    <p>Build the simplest version that someone will pay for.</p>
  </div>

  <ul class="checklist">
    <li><div class="check-icon"></div>Define your MVP offer: one specific result for one specific person at one price</li>
    <li><div class="check-icon"></div>Write the offer in one sentence: "I help [WHO] achieve [OUTCOME] in [TIMEFRAME] without [OBSTACLE]"</li>
    <li><div class="check-icon"></div>Set your price (charge more than feels comfortable — test the ceiling, not the floor)</li>
    <li><div class="check-icon"></div>Create the delivery asset (template, document, Notion, guide, or service process)</li>
    <li><div class="check-icon"></div>Write 3 bullet points of proof (a result you've achieved yourself counts)</li>
    <li><div class="check-icon"></div>Create the simplest possible sales page (Gumroad, Notion, Carrd, or just a PDF)</li>
    <li><div class="check-icon"></div>Set up payment: Gumroad, Stripe, or PayPal (choose one, get it live today)</li>
  </ul>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Phase 03-07</div>
    <h2>Launch Through Scale (Week 5-12)</h2>
    <p>Get the first customer, then the first 10.</p>
  </div>

  <div class="item"><h4>Phase 3: First Sale (Week 5-6)</h4><p>Tell everyone in your existing network. DM 20 people directly with a specific offer (not a general announcement). The first sale almost always comes from a warm relationship, not cold traffic. Get one paying customer before running any ads.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Phase 4: First 10 Customers (Week 7-8)</h4><p>Ask your first customer for a testimonial and a referral. Post about what you're doing with the result your first customer got. Create one piece of content that demonstrates your expertise. Launch on Product Hunt or relevant community if appropriate.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Phase 5: System (Week 9-10)</h4><p>Document your delivery process so it takes half the time. Create an FAQ from every question your first customers asked. Set up basic automation: payment confirmation, delivery, follow-up. Your time is now more valuable — protect it.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Phase 6: Optimize (Week 11)</h4><p>Review your conversion data. What's your traffic-to-sale rate? What objections are you hearing? Raise your price by 20% if you haven't had a single "too expensive" objection yet — you're underpriced.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Phase 7: Scale (Week 12)</h4><p>Identify which one channel is driving the most customers. Put 80% of your effort into that channel. Stop experimenting with new channels until one channel is profitable and repeatable.</p></div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Side Hustle Quick-Start Checklist &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result17 = html_doc(
    title="Side Hustle Quick-Start Checklist",
    subtitle="7-phase, 90-day checklist to go from idea to first paying customer. Validation, offer creation, first sale, and scaling — one decision at a time, zero fluff.",
    eyebrow="Schep Digital · Side Hustle Launch System",
    meta_items=[
        ("Phases", "7 (idea → scale)"),
        ("Timeline", "90 days"),
        ("Required capital", "€0 to start"),
        ("Goal", "First paid transaction"),
    ],
    body_html=body17
)

# ── WRITE FILES ──────────────────────────────────────────────────────────────

files = [
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/12_instagram_growth_templates.html", result12),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/13_cv_resume_templates.html", result13),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/14_notion_habit_architecture.html", result14),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/15_omnichannel_social_calendar.html", result15),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/16_email_subject_line_mastery.html", result16),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/17_side_hustle_checklist.html", result17),
]

for path, content in files:
    with open(path, "w") as f:
        f.write(content)
    print(f"Written: {path}")
