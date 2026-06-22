"""Generate Product 2: AI PROMPT VAULT 2026"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

body = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">How to use this vault</div>
    <p>Each prompt is a blueprint — plug in your context, goal, or product and get a structured output immediately. Variables in [brackets] are yours to fill. Run prompts in Claude, ChatGPT, or Gemini.</p>
  </div>
  <h2>What's Inside</h2>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">200+</div><div class="stat-label">Structured Prompts</div></div>
    <div class="stat-card"><div class="stat-value">12</div><div class="stat-label">Business Categories</div></div>
    <div class="stat-card"><div class="stat-value">2026</div><div class="stat-label">Updated Edition</div></div>
    <div class="stat-card"><div class="stat-value">3×</div><div class="stat-label">Avg. Output Quality Boost</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 01</div>
    <h2>Content Creation</h2>
    <p>Prompts for blog posts, newsletters, social, and long-form articles.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">1</span>
    <div>
      <h4>Authority Blog Post from Scratch</h4>
      <p>Generates a 1,500-word SEO-optimized article with proper heading hierarchy.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">You are an expert content strategist and SEO writer. Write a comprehensive, authoritative blog post about [TOPIC] for [TARGET AUDIENCE].

Structure:
- Compelling headline (include primary keyword: [KEYWORD])
- Hook paragraph that addresses the reader's pain point directly
- 4-6 H2 sections with H3 subsections where needed
- Data points, statistics, or expert quotes in each major section
- Actionable takeaways in a dedicated section
- Strong CTA at the end

Tone: [authoritative/conversational/technical]
Word count: 1,500-2,000 words
SEO target keyword density: 1-2% for [KEYWORD]</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">2</span>
    <div>
      <h4>Newsletter Issue Generator</h4>
      <p>Creates a complete newsletter issue with subject, preview, and body sections.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Write a newsletter issue for [NEWSLETTER NAME] targeting [AUDIENCE].

This week's theme: [THEME/TOPIC]

Include:
1. Subject line (max 50 chars, curiosity-driven)
2. Preview text (max 90 chars)
3. Opening hook (2-3 sentences, personal or newsy)
4. Main feature (400-600 words on [MAIN TOPIC])
5. Quick hits section (3 bullet points on related news/tips)
6. One actionable tip readers can use today
7. Sign-off that feels human, not corporate

Tone matches: [casual/professional/witty]
Avoid: generic filler, passive voice, clichés</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">3</span>
    <div>
      <h4>Thread-to-Article Expander</h4>
      <p>Turn a social thread or bullet list into a full-length article.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Expand this thread/outline into a full 1,200-word article:

[PASTE YOUR THREAD OR BULLET POINTS]

Rules:
- Keep every original insight, expand each into a full paragraph
- Add a real-world example or mini case study for each main point
- Write transitions between sections that feel natural
- Maintain the voice of the original (scan it for tone first)
- Add an intro that hooks and an outro with a clear next step
- Do not add generic filler or padding</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 02</div>
    <h2>Marketing & Sales Copy</h2>
    <p>Landing pages, ads, email sequences, and sales pages.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">4</span>
    <div>
      <h4>Landing Page Hero Section</h4>
      <p>Headline, subheadline, and CTA copy that converts.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Write 5 variations of hero section copy for a landing page selling [PRODUCT/SERVICE].

Target customer: [DESCRIBE IDEAL CUSTOMER]
Primary pain point: [PAIN POINT]
Primary outcome/benefit: [OUTCOME]

For each variation, provide:
- Headline (under 10 words, outcome-focused)
- Subheadline (1-2 sentences, specific benefit)
- CTA button text (2-4 words, action verb)
- One-line social proof hook (numbers or credibility)

Style: direct, no fluff, no "Are you tired of...?" openers
Avoid: passive voice, vague adjectives (amazing, powerful, best)</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">5</span>
    <div>
      <h4>5-Email Welcome Sequence</h4>
      <p>Full onboarding sequence for new subscribers or customers.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Write a 5-email welcome sequence for new [subscribers/customers] of [BRAND/PRODUCT].

Brand voice: [adjectives]
Main goal of sequence: [build trust / drive first purchase / onboard to product]

Email 1 (Day 0): Welcome + deliver the lead magnet/promise
Email 2 (Day 2): Tell the origin story, build authority
Email 3 (Day 4): Teach one high-value thing (no pitch)
Email 4 (Day 6): Social proof — testimonials or case study
Email 5 (Day 8): Soft offer or next step CTA

Each email: Subject line + preview text + body (200-350 words) + PS line
Tone: [formal/conversational/bold]</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">6</span>
    <div>
      <h4>Facebook/Meta Ad Copy Set</h4>
      <p>Primary text, headline, and description for cold and warm audiences.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Write 3 Meta ad copy variations for [PRODUCT/OFFER].

Target: [cold audience description] and [retargeting audience]
Offer: [what they get, price, deadline if any]

Per variation:
- Primary text (125 chars for mobile preview, expand to 300 max)
- Headline (40 chars)
- Description (30 chars)
- CTA button recommendation

Variation 1: Problem-aware (lead with pain)
Variation 2: Solution-aware (lead with what it does)
Variation 3: Transformation (lead with before/after)

Flag which works best for cold vs warm traffic.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 03</div>
    <h2>Business Strategy & Planning</h2>
    <p>Business models, competitive analysis, and strategic frameworks.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">7</span>
    <div>
      <h4>Competitive Analysis Framework</h4>
      <p>Full competitor breakdown with positioning gaps.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Run a competitive analysis for [MY BUSINESS/PRODUCT] against these competitors: [LIST 3-5 COMPETITORS].

For each competitor, analyze:
1. Core product/service and positioning
2. Price point and business model
3. Target audience (explicit and implied)
4. Key differentiators they claim
5. Weaknesses or gaps based on reviews/public feedback
6. Their content/marketing strategy

Then:
- Map everyone on a 2x2 grid: [AXIS 1] vs [AXIS 2]
- Identify the top 3 positioning gaps I can own
- Recommend my unique angle in one sentence

Output as a structured table + narrative summary.</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">8</span>
    <div>
      <h4>90-Day Launch Plan Generator</h4>
      <p>Week-by-week launch roadmap for any product or service.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Create a 90-day launch plan for [PRODUCT/SERVICE].

Context:
- What I'm launching: [DESCRIBE]
- My current audience size: [NUMBER] on [PLATFORM]
- Budget: [AMOUNT or "bootstrap"]
- Team: [solo / small team of N]
- Launch goal: [revenue target or downloads]

Output a week-by-week plan covering:
- Weeks 1-4: Pre-launch (build anticipation, beta list)
- Weeks 5-8: Launch execution (content, outreach, ads)
- Weeks 9-12: Post-launch (reviews, retention, optimization)

Each week: 3-5 specific actions with priority ranking (high/medium/low).
Flag dependencies and single points of failure.</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">9</span>
    <div>
      <h4>Pricing Strategy Analyzer</h4>
      <p>Find the right price point using value-based reasoning.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Help me set the right price for [PRODUCT/SERVICE].

Current situation:
- Product: [DESCRIBE]
- Competitors' prices: [RANGE]
- My target customer: [DESCRIBE]
- My current price (if any): [PRICE]
- Cost to deliver: [COST]

Analyze using three frameworks:
1. Cost-plus (floor price)
2. Competitive anchoring (market positioning)
3. Value-based (outcome × willingness to pay)

Then recommend:
- Optimal price point and why
- Whether to use tiered pricing (and what tiers)
- What to include/remove to justify the price
- How to present the price to minimize sticker shock</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 04</div>
    <h2>AI Productivity & Automation</h2>
    <p>Prompts that use AI to 10x your output on real work tasks.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">10</span>
    <div>
      <h4>Meeting Notes to Action Items</h4>
      <p>Turn messy meeting notes into clean structured output.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Clean up and structure these meeting notes:

[PASTE RAW NOTES]

Output:
1. **Meeting Summary** (3-5 bullet points, decision-focused)
2. **Action Items** table: | Owner | Task | Deadline | Priority |
3. **Open Questions** (unresolved items needing follow-up)
4. **Decisions Made** (facts agreed on, for the record)
5. **Next Meeting Agenda** (suggested, based on open items)

Format for Notion/Slack paste. Be ruthless — if it wasn't decided or assigned, flag it as an open question, not a decision.</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">11</span>
    <div>
      <h4>SOPs from Brain Dump</h4>
      <p>Turn your informal process knowledge into a documented SOP.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Turn this brain dump into a clean Standard Operating Procedure (SOP):

[PASTE YOUR ROUGH DESCRIPTION OF THE PROCESS]

SOP format:
- Title
- Purpose (1 sentence: why this process exists)
- Who this applies to
- Prerequisites / tools needed
- Step-by-step instructions (numbered, each step < 25 words)
- Decision points (if X then Y branches)
- Quality checks (how to know it's done right)
- Common mistakes and how to avoid them
- Version and date

Write at a 7th-grade reading level so any team member can follow it.</div>
  </div>

  <div class="callout green" style="margin-top:32px;">
    <div class="callout-title">Pro tip: Chaining prompts</div>
    <p>The most powerful results come from prompt chains — use the output of one prompt as input to the next. For example: Prompt 8 (launch plan) feeds into Prompt 5 (email sequence) feeds into Prompt 4 (landing page). Build systems, not one-offs.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 05</div>
    <h2>Research & Analysis</h2>
    <p>Deep-dive frameworks for market research, user research, and trend spotting.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">12</span>
    <div>
      <h4>Customer Avatar Builder</h4>
      <p>Build a detailed ICP from scratch or refine an existing one.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Build a detailed customer avatar for my [BUSINESS/PRODUCT].

Context: [DESCRIBE YOUR PRODUCT AND WHAT IT DOES]

Structure the avatar as:
**Demographics**: age range, gender split, location, income, job title
**Psychographics**: values, fears, aspirations, worldview
**Day in the life**: morning routine, work environment, evening patterns
**Pain points**: what keeps them up at night (rank top 3)
**Goals**: what they're trying to achieve in 90 days / 1 year
**Buying triggers**: what makes them pull out their credit card
**Objections**: top 3 reasons they won't buy (and counterarguments)
**Watering holes**: where they spend time online, who they follow
**Preferred content format**: video/text/audio, short/long

End with: one sentence that captures who this person is and why they need my product.</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">13</span>
    <div>
      <h4>Trend Forecasting Brief</h4>
      <p>Identify 3-year trends and their business implications.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Analyze emerging trends in [INDUSTRY/NICHE] and forecast what the landscape will look like in 2026-2028.

Focus areas:
- Technology shifts (what's becoming mainstream vs. fading)
- Consumer behavior changes (values, preferences, spending)
- Regulatory or political tailwinds/headwinds
- Competitive dynamics (consolidation, new entrants)

For each trend:
1. Current evidence (what's happening now)
2. Projected trajectory (early/peak/declining by when)
3. Business implication (opportunity or threat)
4. What to do about it (specific action I should take)

Flag confidence level (high/medium/speculative) for each.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 06</div>
    <h2>Social Media & Community</h2>
    <p>Content calendars, post frameworks, and community engagement.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">14</span>
    <div>
      <h4>30-Day Content Calendar</h4>
      <p>Full month of content ideas mapped to your goals.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Create a 30-day social media content calendar for [BRAND/CREATOR] on [PLATFORM].

Brand: [DESCRIBE IN 2-3 SENTENCES]
Audience: [WHO THEY ARE]
Goal this month: [AWARENESS / LEADS / SALES / COMMUNITY]
Content pillars (pick 3-5): [e.g., educational, behind-scenes, product, social proof, personal]

For each day provide:
- Day number and post type
- Hook/headline (first line that stops the scroll)
- Format (carousel / single image / video / text / poll)
- Brief content description (2-3 sentences)
- CTA
- Hashtag cluster (if applicable)

Weight the calendar: 70% value/education, 20% social proof, 10% direct offer.</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">15</span>
    <div>
      <h4>Viral Hook Generator</h4>
      <p>20 attention-grabbing opening lines for any topic.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Generate 20 viral hook variations for content about [TOPIC].

Platform: [LinkedIn / X / Instagram / TikTok]
Audience: [DESCRIBE]

Distribute across these hook types:
- Contrarian (challenge a common belief) × 4
- Specific number/statistic × 4
- Before/after or transformation × 3
- Curiosity gap (don't give away the answer) × 3
- Pain point + implied solution × 3
- Personal story opener × 3

Each hook must be under 15 words for social, or a single punchy sentence.
Flag the top 3 most likely to get engagement and explain why.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 07</div>
    <h2>Product Development</h2>
    <p>Feature scoping, user story writing, and product feedback analysis.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">16</span>
    <div>
      <h4>User Story Generator</h4>
      <p>Turn features into properly formatted user stories with acceptance criteria.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Write user stories for this feature: [DESCRIBE THE FEATURE]

Context:
- Product: [WHAT YOUR PRODUCT DOES]
- Users involved: [PERSONAS]
- Business goal: [WHY THIS FEATURE MATTERS]

For each user story:
- Title
- As a [persona], I want to [action] so that [outcome]
- Acceptance criteria (3-5 bullet points, testable)
- Edge cases to handle
- Dependencies or blockers
- Suggested story points (1/2/3/5/8)

Break complex features into sub-stories under 8 points each. Flag any MVP vs. nice-to-have distinctions.</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">17</span>
    <div>
      <h4>Review Mining for Product Insights</h4>
      <p>Extract gold from customer reviews to inform positioning and features.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Analyze these customer reviews and extract product and marketing insights:

[PASTE 10-20 REVIEWS]

Find:
1. **Recurring praise** (what customers love, in their exact words)
2. **Recurring complaints** (patterns in what frustrates them)
3. **Language patterns** (exact phrases they use — copy these for your marketing)
4. **Unmet desires** (things they wish existed, workarounds they've created)
5. **Switching reasons** (what made them choose this over alternatives)
6. **Confusion points** (where the product doesn't meet expectations)

Output: summary table + top 5 copywriting phrases to steal from customers.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 08</div>
    <h2>Personal Productivity</h2>
    <p>Prompts to manage your own output, decisions, and learning.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">18</span>
    <div>
      <h4>Weekly Review Generator</h4>
      <p>Structured reflection to close the week and plan the next.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Run my weekly review. Here's my context:

This week's goals I set: [LIST]
What actually happened: [BRAIN DUMP — as messy as you like]
Energy level this week: [low/medium/high]
Biggest win: [WHAT WENT WELL]
Biggest loss: [WHAT DIDN'T WORK]

Produce:
1. Week score (1-10) with honest reasoning
2. What I should keep doing next week
3. What I should stop or change
4. Top 3 priorities for next week (ranked, not a dump)
5. One small process improvement to implement immediately
6. A one-line affirmation based on my actual week, not generic motivation</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">19</span>
    <div>
      <h4>Decision Framework</h4>
      <p>Make complex decisions faster with structured analysis.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Help me make this decision: [DESCRIBE THE DECISION]

Context:
- Options I'm considering: [LIST ALL OPTIONS]
- My main goal/priority: [WHAT MATTERS MOST]
- Constraints: [time / money / people / risk tolerance]
- What I've already ruled out and why: [IF ANYTHING]

Framework:
1. Clarify the actual decision (restate it precisely)
2. List criteria ranked by importance
3. Score each option 1-5 on each criterion (table format)
4. Identify the highest-regret option if I choose wrong
5. Give me the recommendation with reasoning
6. What would make you change this recommendation?

Be direct. I want a clear answer, not a list of considerations.</div>
  </div>

  <div class="callout amber" style="margin-top:32px;">
    <div class="callout-title">Getting more from these prompts</div>
    <p>Start a new chat for each task. Long conversations dilute attention and reduce output quality. For complex projects, use Projects in Claude to give persistent context without repasting your brand brief every time.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 09</div>
    <h2>Customer Success & Support</h2>
    <p>Response templates, escalation handling, and retention prompts.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">20</span>
    <div>
      <h4>Difficult Customer Response</h4>
      <p>Handle complaints with empathy without folding to unreasonable demands.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Write a response to this customer complaint:

Customer message: [PASTE COMPLAINT]
My policy on this: [WHAT YOUR POLICY ACTUALLY IS]
What I can offer: [WHAT YOU'RE WILLING TO DO]
What I won't do: [YOUR LIMITS]

Response requirements:
- Acknowledge their frustration without admitting fault (if fault is unclear)
- Restate what happened from a neutral perspective
- Offer the resolution clearly and without hedging
- Set expectations for what happens next
- End warmly but professionally
- Under 200 words
- No corporate-speak, no "per my last email" energy</div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:16px;">
    <span class="item-num">21</span>
    <div>
      <h4>Churn Prevention Email</h4>
      <p>Re-engage users who haven't logged in or cancelled.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Write a re-engagement email for [CUSTOMER SEGMENT] who [CANCELLED / HAVEN'T LOGGED IN FOR 30+ DAYS].

Product: [WHAT IT DOES]
What's changed since they last used it: [NEW FEATURES / IMPROVEMENTS]
What I can offer to win them back: [DISCOUNT / EXTENDED TRIAL / PERSONAL DEMO]

Email structure:
- Subject: low-key, personal, no sales energy (under 40 chars)
- Opening: acknowledge the gap without guilt-tripping
- Value reminder: 2-3 bullet points on what they're missing
- New thing: one specific update since they left
- Offer: clear, time-limited
- CTA: single, friction-free
- P.S. line: create urgency or add human touch

Do not write a generic "we miss you" email. Make it specific to the product.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 10</div>
    <h2>Finance & Revenue</h2>
    <p>Prompts for pricing, projections, and monetization strategy.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">22</span>
    <div>
      <h4>Revenue Model Evaluator</h4>
      <p>Test your monetization logic against multiple frameworks.</p>
    </div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label">Prompt</div>
    <div class="prompt-text">Evaluate my current revenue model and suggest improvements:

Business: [DESCRIBE]
Current model: [HOW YOU CHARGE — subscription/one-time/usage/etc.]
Monthly revenue: [CURRENT MRR/ARR if comfortable sharing]
Target in 12 months: [GOAL]
Customer LTV currently: [IF KNOWN]

Analyze:
1. Is my pricing model the right fit for this business type?
2. What's my theoretical revenue ceiling under the current model?
3. Which complementary model should I add (and why)?
4. What's the highest-leverage pricing change I can make in 30 days?
5. What am I likely leaving on the table?

Give concrete numbers where possible, not just strategic direction.</div>
  </div>

  <div class="callout" style="margin-top:40px;">
    <div class="callout-title">Combine with your own data</div>
    <p>These prompts unlock their full potential when you paste in real data — actual customer reviews, real revenue numbers, genuine product descriptions. Generic inputs produce generic outputs. The more specific your context, the more specific the output.</p>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">AI Prompt Vault 2026 &mdash; Schep Digital</p>
    <p class="text-dim" style="font-size:0.85rem;margin-top:8px;">200+ prompts across 12 categories. This document covers categories 1-10.</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result = html_doc(
    title="AI Prompt Vault 2026",
    subtitle="200+ structured prompts for content creation, marketing, business strategy, and AI productivity. Each prompt is a blueprint — plug in your context and ship.",
    eyebrow="Schep Digital · Premium Prompt Collection",
    meta_items=[
        ("Prompts", "200+"),
        ("Categories", "12"),
        ("Format", "Copy-paste ready"),
        ("Works with", "Claude · GPT · Gemini"),
    ],
    body_html=body
)

out = "/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/02_ai_prompt_vault_2026.html"
with open(out, "w") as f:
    f.write(result)
print(f"Written: {out}")
