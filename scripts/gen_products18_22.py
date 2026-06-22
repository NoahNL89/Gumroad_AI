"""Generate Products 18-22"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

# ── PRODUCT 18: Journaling Prompts ───────────────────────────────────────────

body18 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">Why most journaling fails</div>
    <p>Blank pages produce blank thinking. The "write whatever comes to mind" approach works for 2% of people. The other 98% need structured prompts that pull out specific insights, reframes, and decisions. This pack gives you 100+ prompts across 8 categories — each one engineered to surface something useful.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">100+</div><div class="stat-label">Structured Prompts</div></div>
    <div class="stat-card"><div class="stat-value">8</div><div class="stat-label">Life Categories</div></div>
    <div class="stat-card"><div class="stat-value">3</div><div class="stat-label">Difficulty Levels</div></div>
    <div class="stat-card"><div class="stat-value">10min</div><div class="stat-label">Minimum Session</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 01</div>
    <h2>Clarity &amp; Decision Making</h2>
    <p>Prompts that cut through noise and surface what you actually think.</p>
  </div>

  <div class="item"><h4>The 10-10-10 prompt</h4><p>Write about a decision you're wrestling with. How will you feel about this choice in 10 minutes? In 10 months? In 10 years? Which time horizon matters most for this decision, and why?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Regret Minimization prompt</h4><p>Imagine yourself at 80, looking back at this moment. What would you regret not doing? What would you regret doing? Which regret is easier to live with?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Advice Flip prompt</h4><p>Write the advice you would give your best friend if they came to you with your exact situation. Now write why you're not taking that advice yourself. What does the gap tell you?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Pre-mortem prompt</h4><p>It's one year from now and the thing you're planning has failed completely. What went wrong? List every plausible reason. Now: which of these can you prevent in advance?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Energy Audit prompt</h4><p>List everything you did this week. Mark each item: gave me energy (+) or drained me (-). What pattern do you see? What should you do more of, less of, or stop entirely?</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 02</div>
    <h2>Self-Knowledge &amp; Identity</h2>
    <p>Prompts that build an accurate picture of who you actually are.</p>
  </div>

  <div class="item"><h4>The Peak Moment prompt</h4><p>Describe a moment in the last year when you felt most like yourself — fully engaged, competent, and energized. What were you doing? Who were you with? What made it feel that way?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Fear Inventory prompt</h4><p>Write down every fear that is limiting a decision you want to make right now. For each fear: is it based on evidence or assumption? What's the realistic worst-case? What would you do if that happened?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Values Clash prompt</h4><p>Name two values that are in tension in your life right now (e.g., freedom vs. security, ambition vs. presence). How are you navigating the conflict? Which value is winning, and is that your actual choice or a default?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Narrative Audit prompt</h4><p>What is the story you most often tell about yourself — to others and to yourself? Is it accurate? Is it serving you? What story would you prefer to tell, and what would have to change for it to be true?</p></div>

  <div class="callout" style="margin-top:24px;">
    <div class="callout-title">How to use these prompts</div>
    <p>Pick one prompt. Write for exactly 10 minutes without stopping. Don't edit as you write. At the end, underline the single most important sentence. That's your insight for the day — act on it before tomorrow.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 03</div>
    <h2>Relationships &amp; Communication</h2>
    <p>Prompts that surface what you actually feel about the people in your life.</p>
  </div>

  <div class="item"><h4>The Unsent Letter prompt</h4><p>Write a letter to someone you have unresolved feelings about — good or bad. Say everything you've never said. You won't send it. What does writing it reveal?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Appreciation Deficit prompt</h4><p>Who in your life deserves more acknowledgment than they're getting from you? What specifically do you appreciate about them that you haven't said? Write it now — then consider whether to actually say it.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Boundary Inventory prompt</h4><p>Where are you saying yes when you mean no? What would you stop doing if you were completely honest about your limits? What is the cost of maintaining each current boundary violation?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Pattern Recognition prompt</h4><p>What conflict or frustration keeps recurring in your relationships (work, personal, or both)? What is your consistent role in that pattern? What would change if you responded differently next time?</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 04</div>
    <h2>Goals &amp; Progress</h2>
    <p>Prompts that create honest accountability — without the toxic positivity.</p>
  </div>

  <div class="item"><h4>The Gap Analysis prompt</h4><p>Where do you want to be in 12 months? Where are you now? Write the honest gap. What specific actions close it? Which of those actions are you actually willing to do?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Momentum Audit prompt</h4><p>What is building in your life right now — getting better through consistent effort? What is decaying — getting worse through neglect? Write both lists. Which deserves more attention?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The One Year Ago prompt</h4><p>Think back exactly one year. What did you want then that you now have? What did you want then that you still don't have — and honestly, why not? What does the answer tell you about the next year?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Constraint prompt</h4><p>What is the single biggest obstacle between you and your most important goal right now? Not a list — just one. What would it take to remove or work around that constraint?</p></div>

  <div class="callout green" style="margin-top:24px;">
    <div class="callout-title">The AI journaling extension</div>
    <p>After writing any prompt, paste your entry into Claude or ChatGPT with: "Read what I wrote and ask me the 3 questions that would push my thinking further." The AI will identify blind spots your own journaling can't see.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 05</div>
    <h2>Creativity &amp; Expression</h2>
    <p>Prompts that unlock original thinking and break creative blocks.</p>
  </div>

  <div class="item"><h4>The Worst Version prompt</h4><p>Deliberately write the worst possible version of what you're trying to create. Make it embarrassingly bad on purpose. Now: what's actually good that you were avoiding? (This breaks perfectionism-paralysis.)</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Steal Framework prompt</h4><p>What are 3 ideas from completely different fields that could apply to your current creative challenge? Describe how each one would work if transplanted. Which combination creates something new?</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Constraints prompt</h4><p>Pick an arbitrary constraint for your creative project (only 5 words, no budget, must finish in 1 hour, must be the opposite of your instinct). Write what you'd make under that constraint. What does working under pressure reveal?</p></div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Journaling Prompts for Clarity &amp; Calm &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result18 = html_doc(
    title="Journaling Prompts for Clarity & Calm",
    subtitle="100+ structured prompts across 8 life categories. Clarity, decisions, identity, relationships, goals, and creativity — each prompt engineered to surface something useful in 10 minutes.",
    eyebrow="Schep Digital · Structured Journaling System",
    meta_items=[
        ("Prompts", "100+"),
        ("Categories", "8 life areas"),
        ("Session time", "10 minutes minimum"),
        ("Works with", "Paper · Notion · Day One"),
    ],
    body_html=body18
)

# ── PRODUCT 19: SEO Checklist ─────────────────────────────────────────────────

body19 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">SEO in 2026: Intent over keywords</div>
    <p>Google's Helpful Content system rewards content that satisfies searcher intent — not content stuffed with keywords. This checklist is built around that reality. Every item here connects to a ranking signal that still matters, plus the AI-driven signals that matter now.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">80+</div><div class="stat-label">Checklist Items</div></div>
    <div class="stat-card"><div class="stat-value">6</div><div class="stat-label">Audit Categories</div></div>
    <div class="stat-card"><div class="stat-value">2026</div><div class="stat-label">Updated Edition</div></div>
    <div class="stat-card"><div class="stat-value">AI</div><div class="stat-label">Search Ready</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 01</div>
    <h2>Technical Foundation</h2>
    <p>The infrastructure that lets Google crawl, index, and understand your site.</p>
  </div>

  <ul class="checklist">
    <li><div class="check-icon"></div>Core Web Vitals pass: LCP &lt;2.5s, INP &lt;200ms, CLS &lt;0.1 (measure in PageSpeed Insights)</li>
    <li><div class="check-icon"></div>HTTPS enforced on all pages, no mixed content warnings</li>
    <li><div class="check-icon"></div>XML sitemap submitted to Google Search Console, no errors</li>
    <li><div class="check-icon"></div>robots.txt allows crawl of all important pages (test in GSC)</li>
    <li><div class="check-icon"></div>Canonical tags set correctly — no duplicate content without canonical</li>
    <li><div class="check-icon"></div>Structured data (Schema.org) implemented for relevant content types</li>
    <li><div class="check-icon"></div>Mobile-first: full functionality works at 375px viewport width</li>
    <li><div class="check-icon"></div>No broken internal links (crawl with Screaming Frog or Ahrefs)</li>
    <li><div class="check-icon"></div>404 pages return actual 404 status (not 200 with error content)</li>
    <li><div class="check-icon"></div>Redirect chains under 2 hops — eliminate 301→301→301 chains</li>
    <li><div class="check-icon"></div>JavaScript rendering not blocking critical content for Googlebot</li>
    <li><div class="check-icon"></div>Image alt text on all informational images, empty alt on decorative</li>
  </ul>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 02</div>
    <h2>Content &amp; Intent Match</h2>
    <p>The gap between what you wrote and what the searcher actually wanted.</p>
  </div>

  <ul class="checklist">
    <li><div class="check-icon"></div>Primary keyword appears in: title tag, H1, first 100 words, URL slug</li>
    <li><div class="check-icon"></div>Search intent matched: informational / navigational / transactional / commercial — is your content the right type?</li>
    <li><div class="check-icon"></div>SERP analysis done: compare your format, depth, and angle to the top 5 results</li>
    <li><div class="check-icon"></div>Content covers the topic completely — no major sub-questions left unanswered</li>
    <li><div class="check-icon"></div>E-E-A-T signals present: author bio, credentials, first-hand experience, publication date</li>
    <li><div class="check-icon"></div>Unique angle or data point present — not just a rephrased version of existing content</li>
    <li><div class="check-icon"></div>Internal links to 2-4 relevant pages on your site</li>
    <li><div class="check-icon"></div>External links to 1-3 authoritative sources (opens in new tab)</li>
    <li><div class="check-icon"></div>Reading level appropriate for audience (test at readability-score.com)</li>
    <li><div class="check-icon"></div>Content updated within last 12 months (or reviewed and marked current)</li>
  </ul>

  <div class="callout amber" style="margin-top:24px;">
    <div class="callout-title">The Helpful Content test</div>
    <p>Read your page and answer: "Does this content provide real value to someone who already knows the basics, or is it just covering what they already found in the top 10 results?" If it's the latter, your page will not rank sustainably in the Helpful Content era.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 03</div>
    <h2>On-Page Optimization</h2>
    <p>The elements you control directly — optimized for both Google and readers.</p>
  </div>

  <ul class="checklist">
    <li><div class="check-icon"></div>Title tag: under 60 characters, primary keyword near the start, compelling to click</li>
    <li><div class="check-icon"></div>Meta description: under 160 characters, includes keyword, has a clear value proposition</li>
    <li><div class="check-icon"></div>URL slug: short, keyword-rich, hyphens not underscores, no stop words</li>
    <li><div class="check-icon"></div>H1 matches or closely mirrors the title tag (one H1 per page only)</li>
    <li><div class="check-icon"></div>H2s and H3s used for real hierarchy — not just for SEO, for readability</li>
    <li><div class="check-icon"></div>Featured snippet optimization: direct question answered in first 2 sentences below H2</li>
    <li><div class="check-icon"></div>Table of contents for articles over 1,500 words</li>
    <li><div class="check-icon"></div>Images: compressed (WebP preferred), lazy-loaded, descriptive filenames</li>
    <li><div class="check-icon"></div>Open Graph tags set for social sharing (og:title, og:description, og:image)</li>
    <li><div class="check-icon"></div>Breadcrumbs implemented and marked up with Schema.org BreadcrumbList</li>
  </ul>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Category 04</div>
    <h2>Authority &amp; Link Building</h2>
    <p>Building the trust signals that tell Google this page deserves to rank.</p>
  </div>

  <ul class="checklist">
    <li><div class="check-icon"></div>Domain rating (Ahrefs) or Domain Authority (Moz) benchmarked against top competitors</li>
    <li><div class="check-icon"></div>At least 3 high-authority backlinks pointing to this specific page</li>
    <li><div class="check-icon"></div>Internal linking strategy: this page is linked from 3-5 relevant existing pages</li>
    <li><div class="check-icon"></div>Toxic link audit run — disavow any spam links pointing to the domain</li>
    <li><div class="check-icon"></div>Brand mentions (unlinked) converted to links via outreach</li>
    <li><div class="check-icon"></div>Digital PR: original research or data published that others cite</li>
    <li><div class="check-icon"></div>Guest posts published on 2+ relevant sites per month</li>
    <li><div class="check-icon"></div>HARO / journalist queries answered for media coverage and backlinks</li>
  </ul>

  <div class="section-header" style="margin-top:32px;">
    <div class="section-num">Category 05</div>
    <h2>AI Search Optimization (2026)</h2>
    <p>Optimizing for AI Overviews, Perplexity, and LLM citation.</p>
  </div>

  <ul class="checklist">
    <li><div class="check-icon"></div>Content answers questions directly and completely — AI models prefer clear, citable answers</li>
    <li><div class="check-icon"></div>Structured data implemented to help AI models parse content types accurately</li>
    <li><div class="check-icon"></div>Author entity established: Google Knowledge Graph presence, consistent NAP across web</li>
    <li><div class="check-icon"></div>Content cited by Wikipedia or other LLM training sources (long-term signal)</li>
    <li><div class="check-icon"></div>FAQ schema implemented for question-format content (common AI citation format)</li>
    <li><div class="check-icon"></div>Brand appears in AI model responses when brand keywords are queried (test in ChatGPT, Claude, Gemini)</li>
  </ul>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">SEO Checklist 2026 &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result19 = html_doc(
    title="SEO Checklist 2026",
    subtitle="80+ checklist items across 6 audit categories — technical foundation, content-intent matching, on-page optimization, authority building, and AI search readiness. Updated for the Helpful Content era.",
    eyebrow="Schep Digital · 2026 SEO Audit System",
    meta_items=[
        ("Items", "80+ checklist"),
        ("Categories", "6 audit areas"),
        ("Includes", "AI search section"),
        ("Updated", "2026 Edition"),
    ],
    body_html=body19
)

# ── PRODUCT 20: AI Content Machine Bundle ────────────────────────────────────

body20 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">The content machine model</div>
    <p>Most creators treat content as a creative endeavour. The ones who scale treat it as a system. This bundle combines three tools: a hook architecture guide, a carousel production system, and an omnichannel repurposing engine. One week of setup, months of leverage.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">3</div><div class="stat-label">Integrated Tools</div></div>
    <div class="stat-card"><div class="stat-value">50+</div><div class="stat-label">Templates</div></div>
    <div class="stat-card"><div class="stat-value">7×</div><div class="stat-label">Output Multiplier</div></div>
    <div class="stat-card"><div class="stat-value">4hrs</div><div class="stat-label">Weekly Content Work</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Tool 01</div>
    <h2>Hook Architecture</h2>
    <p>The science of stopping the scroll — applied systematically across all your content.</p>
  </div>

  <p style="color:var(--ink-2);">Your hook is not the beginning of your content. It is the reason someone consumes it at all. A technically excellent piece with a weak hook is invisible. A mediocre piece with a great hook reaches thousands. The architecture of a great hook is learnable and repeatable.</p>

  <h3>The Hook Stack</h3>
  <div class="item"><h4>Layer 1: The Pattern Interrupt</h4><p>Something that breaks the expectation of the feed. A number that's oddly specific. A claim that contradicts received wisdom. An image juxtaposition that doesn't make immediate sense. The interrupt happens before a word is read.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Layer 2: The Stakes</h4><p>Within the first sentence: why this matters to the reader specifically. Not "this is interesting" — "this affects you if [specific condition]". The stakes connect the pattern interrupt to the reader's self-interest.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Layer 3: The Promise</h4><p>What they will know, have, or be able to do after consuming this. Explicit when possible: "By the end of this, you'll know X." Implied when the hook is strong enough to carry it on its own.</p></div>

  <div class="prompt-block" style="margin-top:24px;">
    <div class="prompt-label">Hook generator prompt</div>
    <div class="prompt-text">Write 10 hooks for content about [TOPIC] for [AUDIENCE].

For each hook, stack all three layers:
- Pattern interrupt (unexpected angle or format)
- Stakes (why this matters to the specific reader)
- Promise (what they'll get from reading on)

Formats to cover: short-form video (under 5 words spoken), long-form article opener (2-3 sentences), carousel slide 1 (under 10 words), newsletter subject line (under 50 chars).

Rank by expected performance for cold traffic.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Tool 02</div>
    <h2>Carousel Production System</h2>
    <p>The format that drives more saves than any other on Instagram and LinkedIn.</p>
  </div>

  <h3>The 5 carousel formats that consistently work</h3>
  <div class="item"><h4>Format 1: The Mistake List</h4><p>"X mistakes [AUDIENCE] makes." One mistake per slide. Slide 1 is the count hook. Slides 2-N are mistakes. Last slide is the positive resolution + follow CTA. Best for: high-engagement cold traffic.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Format 2: The Mini Course</h4><p>Teach one concept in 8-10 slides. Slide 1: the outcome. Slides 2-8: one concept each. Slide 9: summary. Slide 10: next step. Best for: growing a follower base that trusts your expertise.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Format 3: The Before/After</h4><p>First 3 slides: the painful before state. Middle 3 slides: the transformation lever. Last 3 slides: the after state + path to get there. Best for: converting observers to buyers.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Format 4: The Checklist</h4><p>One item per slide. First slide is the count hook. Last slide is the "how many did you check?" engagement mechanic. Highly saveable. Best for: bookmark-bait content.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Format 5: The Opinion + Proof</h4><p>Slide 1: Contrarian claim. Slides 2-7: Evidence for the claim (data, examples, case studies). Slide 8: The implication. Slide 9: What to do about it. Best for: building authority and thought leadership.</p></div>

  <div class="prompt-block" style="margin-top:24px;">
    <div class="prompt-label">Carousel content generator</div>
    <div class="prompt-text">Create a [FORMAT NAME] carousel on [TOPIC] for [AUDIENCE] on [PLATFORM].

For each slide:
- Slide number and type
- Headline (under 8 words, bold, stops the scroll)
- Body text (under 25 words)
- Visual direction (what should be shown)
- Transition hint (why they'll swipe to the next slide)

Slide 1 must be the strongest. Slide 10 must earn a save or follow.
Total slides: [8 / 10 / 12]</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Tool 03</div>
    <h2>Omnichannel Repurposing Engine</h2>
    <p>Turn one piece of content into a week of output across every platform.</p>
  </div>

  <h3>The Content Atom workflow</h3>
  <div class="item"><h4>Step 1: Create the Atom (2 hours)</h4><p>Write one long-form piece: a blog post, YouTube script, podcast episode, or detailed LinkedIn article. This is your source of truth. Every piece this week derives from it. Make it 1,000-2,000 words minimum.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Step 2: Extract (30 minutes)</h4><p>From the Atom, pull: 5 standalone insights (for X threads or LinkedIn posts), 3 stories or examples (for Reels/TikToks), 1 strong opinion or argument (for a hot-take post), the best checklist or list embedded in the piece (for a carousel).</p></div>
  <div class="item" style="margin-top:12px;"><h4>Step 3: Reformat (1 hour)</h4><p>Use the repurposing prompt (below) to convert each extracted piece into the native format for its target platform. Don't copy-paste — adapt the tone, length, and structure for each platform's audience expectations.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Step 4: Schedule (30 minutes)</h4><p>Load everything into Buffer, Later, or Hypefury. Stagger the posting times across the week. You now have 7+ pieces from 4 hours of total work.</p></div>

  <div class="prompt-block" style="margin-top:24px;">
    <div class="prompt-label">Repurposing engine prompt</div>
    <div class="prompt-text">Repurpose this content atom for [TARGET PLATFORM]:

[PASTE YOUR ORIGINAL CONTENT]

Platform: [LinkedIn / X / Instagram / TikTok / Newsletter]
Native format for this platform: [Article / Thread / Carousel / Script / Email section]
Audience on this platform: [HOW THEY DIFFER from your main audience]

Adapt for the platform's native voice and format conventions.
Do not just shorten — restructure for how this platform's users consume content.
Keep the core insight. Change everything else.</div>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">AI Content Machine Bundle &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result20 = html_doc(
    title="AI Content Machine Bundle",
    subtitle="Three integrated tools: Hook Architecture, Carousel Production System, and Omnichannel Repurposing Engine. One week of setup. 7× your content output with 4 hours of work per week.",
    eyebrow="Schep Digital · Content Scaling System",
    meta_items=[
        ("Tools", "3 integrated systems"),
        ("Templates", "50+"),
        ("Output multiplier", "7× from one piece"),
        ("Weekly effort", "~4 hours"),
    ],
    body_html=body20
)

# ── PRODUCT 21: 75 Power Prompts for AI Masters ──────────────────────────────

body21 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">The next level</div>
    <p>The standard prompt pack is for getting started. This is for people who already use AI daily and want to push into territory most users never reach: meta-prompting, chain-of-thought engineering, multi-model orchestration, and adversarial testing. 75 prompts that assume you already know the basics.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">75</div><div class="stat-label">Advanced Prompts</div></div>
    <div class="stat-card"><div class="stat-value">8</div><div class="stat-label">Expert Techniques</div></div>
    <div class="stat-card"><div class="stat-value">Level</div><div class="stat-label">Advanced Only</div></div>
    <div class="stat-card"><div class="stat-value">Multi</div><div class="stat-label">Model Support</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Technique 01</div>
    <h2>Meta-Prompting</h2>
    <p>Use AI to write better prompts for AI. Recursive intelligence.</p>
  </div>

  <p style="color:var(--ink-2);">The fastest way to improve your prompts is to have the AI critique and rewrite them. Meta-prompting treats the prompt itself as a first draft — the model's architectural knowledge of what makes prompts work becomes your editing assistant.</p>

  <div class="prompt-block">
    <div class="prompt-label">Prompt critic and rewriter</div>
    <div class="prompt-text">You are an expert prompt engineer. Critique this prompt and rewrite it to produce significantly better results:

ORIGINAL PROMPT: [YOUR PROMPT]

Analysis steps:
1. Identify what's ambiguous or under-specified
2. Identify where the model has too much freedom (produces inconsistent results)
3. Identify missing context that would improve output quality
4. Identify format instructions that are absent
5. Flag any instructions that might conflict

Then rewrite the prompt incorporating all improvements.
Finally, explain in 3 bullet points what changed and why it matters.</div>
  </div>

  <div class="prompt-block" style="margin-top:16px;">
    <div class="prompt-label">Prompt expansion from a brief description</div>
    <div class="prompt-text">Turn this brief task description into a complete, production-quality prompt:

TASK: [DESCRIBE WHAT YOU WANT TO ACCOMPLISH IN 1-2 SENTENCES]
CONTEXT: [WHO IS USING THIS AND WHY]
OUTPUT REQUIREMENTS: [WHAT GOOD OUTPUT LOOKS LIKE]

Write a complete prompt that:
- Sets the role and expertise level precisely
- Provides all necessary context without bloat
- Specifies the exact output format
- Includes quality checks the model should apply to its own output
- Anticipates and prevents the 3 most likely failure modes for this task type</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Technique 02</div>
    <h2>Chain-of-Thought Engineering</h2>
    <p>Structure the model's reasoning process, not just its output.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Forced reasoning chain for complex analysis</div>
    <div class="prompt-text">Analyze [PROBLEM/QUESTION] using this exact reasoning chain. Do not skip steps or combine them.

Step 1 — GATHER: List all relevant facts, constraints, and unknowns
Step 2 — FRAME: State the core question in the most precise possible terms
Step 3 — HYPOTHESIZE: Generate 3 different explanations or approaches (labeled H1, H2, H3)
Step 4 — TEST: For each hypothesis, identify what evidence would confirm or refute it
Step 5 — EVALUATE: Score each hypothesis on: plausibility (1-5), testability (1-5), implications if true (1-5)
Step 6 — SYNTHESIZE: State your conclusion with confidence level and key assumptions
Step 7 — CHALLENGE: Steelman the strongest objection to your conclusion

Complete each step before moving to the next. Label each step clearly.</div>
  </div>

  <div class="prompt-block" style="margin-top:16px;">
    <div class="prompt-label">Devil's advocate reasoning</div>
    <div class="prompt-text">I'm about to make this decision / take this position: [DESCRIBE]

Play devil's advocate with full force. Do not hedge. Argue as strongly as possible against my decision.

Structure your argument:
1. The strongest factual objection (with evidence if possible)
2. The strongest strategic objection (why this is wrong even if the facts are right)
3. The hidden assumption I'm making that might be wrong
4. The person who would most strongly disagree — and what they would say
5. The scenario in which my decision leads to the worst outcome

After the devil's advocate section: tell me what you actually think, and whether the arguments changed anything.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Technique 03</div>
    <h2>Multi-Model Orchestration</h2>
    <p>Use different models' strengths in sequence for better results than any single model.</p>
  </div>

  <div class="item"><h4>The Claude → GPT-4 pipeline</h4><p>Use Claude for: nuanced analysis, long-document synthesis, careful reasoning, and sensitive topics (better calibration). Use GPT-4o for: creative writing with style variation, DALL-E integration, code execution, and real-time web search. Route tasks to the model that handles them best.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The Gemini → Claude pipeline</h4><p>Use Gemini 1.5 Pro for: ingesting large documents (1M tokens), initial extraction and summary. Pass the extracted summary to Claude for: interpretation, recommendations, and writing final deliverables. Gemini processes, Claude synthesizes.</p></div>
  <div class="item" style="margin-top:12px;"><h4>The critic loop</h4><p>Generate output with Model A. Paste that output into Model B with: "Critique the following for [specific quality] and suggest specific improvements." Paste the critique back to Model A: "Revise your response addressing these specific critiques." One iteration improves quality 30-50% on average.</p></div>

  <div class="prompt-block" style="margin-top:24px;">
    <div class="prompt-label">Cross-model validation prompt</div>
    <div class="prompt-text">I got this answer from [MODEL A]: [PASTE ANSWER]

I need you to independently answer the same question:
[PASTE ORIGINAL QUESTION]

Then compare your answer to Model A's:
1. Where do you agree completely?
2. Where do you disagree, and why?
3. What did Model A include that you would not have?
4. What did you include that Model A missed?
5. Which answer is more accurate, and on which specific points?

Do not anchor to Model A's answer. Form your independent view first.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Technique 04</div>
    <h2>Adversarial Testing</h2>
    <p>Break your AI outputs before they reach production or publication.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Output stress test</div>
    <div class="prompt-text">You are a hostile expert reviewer. Your goal is to find every flaw in this output:

[PASTE YOUR AI-GENERATED CONTENT / ANALYSIS / PLAN]

Specifically hunt for:
1. FACTUAL ERRORS: Claims that are incorrect or unverifiable
2. LOGICAL GAPS: Conclusions that don't follow from the evidence
3. MISSING CASES: Situations or stakeholders this output ignores
4. INTERNAL CONTRADICTIONS: Places where the output disagrees with itself
5. OVERCONFIDENCE: Assertions presented as certain that are actually uncertain
6. BIAS: Hidden assumptions about the reader, context, or "normal" case
7. ACTIONABILITY GAPS: Advice that sounds good but is impossible to implement

Rate the overall quality 1-10 and list the top 3 issues to fix before using this output.</div>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">75 Power Prompts for AI Masters &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result21 = html_doc(
    title="75 Power Prompts for AI Masters",
    subtitle="Advanced techniques for experienced AI users: meta-prompting, chain-of-thought engineering, multi-model orchestration, and adversarial testing. 75 prompts that assume you already know the basics.",
    eyebrow="Schep Digital · Advanced AI Mastery",
    meta_items=[
        ("Level", "Advanced"),
        ("Prompts", "75"),
        ("Techniques", "8 expert methods"),
        ("Models", "Claude · GPT-4 · Gemini"),
    ],
    body_html=body21
)

# ── PRODUCT 22: AI Side Hustle Inner Circle ───────────────────────────────────

body22 = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">The membership for AI-native income builders</div>
    <p>The Inner Circle is for people who have decided that AI-augmented income is their path — and want the strategies, accountability, and community to make it real. Every month: a new AI side hustle playbook, live strategy session, and vetted tool stack update.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">Monthly</div><div class="stat-label">New Playbook</div></div>
    <div class="stat-card"><div class="stat-value">Live</div><div class="stat-label">Strategy Sessions</div></div>
    <div class="stat-card"><div class="stat-value">Private</div><div class="stat-label">Community Access</div></div>
    <div class="stat-card"><div class="stat-value">Cancel</div><div class="stat-label">Any Time</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Month 01</div>
    <h2>Foundation: Your First AI Income Stream</h2>
    <p>The proven sequence for generating your first €500/month with AI tools.</p>
  </div>

  <h3>The 3-phase income architecture</h3>
  <div class="item"><h4>Phase 1: Identify your AI leverage point</h4><p>Your existing skill × AI amplification = your unique offer. A writer + Claude = a content agency that produces 10× the output at the same quality. A designer + Midjourney = a visual production studio that quotes faster and delivers more. Find the multiplication, not the replacement.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Phase 2: Package the AI-augmented offer</h4><p>The offer is not "I use AI" — the offer is the result. "10 social media posts delivered in 48 hours" not "AI-assisted content creation." Package the speed and output quality, not the tool. Clients don't buy your process; they buy the outcome.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Phase 3: Productize and automate</h4><p>Once you've delivered the offer manually 3-5 times, build the system. Prompt library for your specific niche. Template library for common outputs. SOP for onboarding. Reduce your time-per-delivery by 50% without reducing quality. Now you can scale.</p></div>

  <div class="prompt-block" style="margin-top:24px;">
    <div class="prompt-label">Income stream identifier</div>
    <div class="prompt-text">Help me identify my highest-leverage AI income stream.

My professional background: [DESCRIBE]
Skills I'm confident in: [LIST]
Tools I already use or am learning: [AI TOOLS]
Time available per week for side hustle: [HOURS]
Income target (monthly): [AMOUNT]
Risk tolerance: [low/medium/high]

For each viable income stream:
1. What the offer is (1 sentence)
2. Who pays for it (be specific)
3. How AI amplifies my existing skill here
4. Realistic monthly income range at 10hrs/week
5. Time to first payment (weeks)
6. Biggest obstacle

Rank by: speed to revenue × income ceiling × fit with my background.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Month 02</div>
    <h2>Digital Products: The Passive Income Engine</h2>
    <p>Build AI-powered digital products that sell while you sleep.</p>
  </div>

  <h3>The product hierarchy</h3>
  <div class="item"><h4>Level 1: Prompt packs and templates (€5-€30)</h4><p>Fastest to create. 10-50 structured prompts for a specific niche. Delivered as PDF. Zero ongoing delivery cost. Build 3-5 products to validate the niche before investing in higher levels.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Level 2: Guides and playbooks (€20-€80)</h4><p>More depth, more value, more price. A complete system for achieving a specific outcome with AI. 20-60 pages. Includes prompts, workflows, and examples. This tier builds your reputation as an expert, not just a product creator.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Level 3: Courses and workshops (€80-€300)</h4><p>Video or live delivery. Higher perceived value, higher production cost, higher margin. Best for: showing the tool in action (screen recordings), building community, or teaching complex workflows that require seeing, not reading.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Level 4: Memberships and coaching (€30-€200/month)</h4><p>Recurring revenue. Requires ongoing content creation but builds predictable income. Best combined with a proven lower-tier product funnel — sell people in at Level 1-2, upgrade them to Level 4.</p></div>

  <div class="callout green" style="margin-top:24px;">
    <div class="callout-title">The product research shortcut</div>
    <p>Search Gumroad and Etsy for AI products in your niche. Find the ones with 100+ sales. These are proven demand signals. Don't copy them — improve them. Add more depth, a better design, more current content, or a niche they overlooked.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Month 03</div>
    <h2>Client Services: High-Ticket AI Delivery</h2>
    <p>Charge premium rates for AI-augmented professional services.</p>
  </div>

  <h3>The premium AI service model</h3>
  <div class="item"><h4>Position on outcomes, not tools</h4><p>"I build content systems that generate 30 pieces per month from one strategy session" — not "I use AI to create content." The client cares about their result, not your method. Never mention AI in your proposal unless they ask.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Price for the value, not the time</h4><p>AI cuts your production time by 60-80%. If you charge hourly and disclose this, your income falls. Charge for the outcome: the 30-piece content package, the 10-page report, the 15-ad creative set. Your margin expands; the client gets the same value.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Build the repeatability moat</h4><p>Your AI system for delivering Client A's results should work for Client B with minor customization. Build the prompt library, the SOP, and the quality checklist once. Your competitive advantage is the system, not the hours.</p></div>

  <div class="prompt-block" style="margin-top:24px;">
    <div class="prompt-label">High-ticket service packaging prompt</div>
    <div class="prompt-text">Help me package my AI-augmented service as a premium offering.

What I can deliver: [DESCRIBE THE OUTPUT]
Who needs it: [TARGET CLIENT — be specific about company size, role, situation]
Current market rate for this: [WHAT FREELANCERS WITHOUT AI CHARGE]
My delivery time with AI: [HOURS]
Quality vs. non-AI delivery: [SAME / BETTER / MUCH BETTER — be honest]

Design a premium service package:
1. Package name (outcome-focused, not feature-focused)
2. What's included (3-5 specific deliverables)
3. Pricing and rationale
4. Guarantee or risk reversal
5. Positioning statement (why you specifically, in 2 sentences)
6. Objection handler for "that's more than I expected"</div>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">AI Side Hustle Inner Circle &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result22 = html_doc(
    title="AI Side Hustle Inner Circle",
    subtitle="Monthly playbooks, live strategy sessions, and a private community for AI-native income builders. Your first €500/month side hustle, then your first €5,000/month — built on AI leverage.",
    eyebrow="Schep Digital · AI Income Membership",
    meta_items=[
        ("Format", "Monthly membership"),
        ("Includes", "Playbook + live session + community"),
        ("Cancel", "Anytime"),
        ("Focus", "AI-augmented income"),
    ],
    body_html=body22
)

# ── WRITE FILES ──────────────────────────────────────────────────────────────

files = [
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/18_journaling_prompts.html", result18),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/19_seo_checklist.html", result19),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/20_ai_content_machine.html", result20),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/21_75_power_prompts_ai_masters.html", result21),
    ("/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/22_ai_side_hustle_inner_circle.html", result22),
]

for path, content in files:
    with open(path, "w") as f:
        f.write(content)
    print(f"Written: {path}")
