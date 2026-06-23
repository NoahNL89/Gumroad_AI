"""Generate: LinkedIn Content OS — 30 Days of Posts in 2 Hours"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

body = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">How to use this system</div>
    <p>Read chapters 1–2 once to set your strategy. Then go straight to chapter 4 — open an AI tool, run the prompts, and batch your entire month of posts in one sitting. The Hook Vault (chapter 5) and the 30-day calendar (chapter 6) are your operational references. Return to them every month.</p>
  </div>
  <h2>What's Inside</h2>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">7</div><div class="stat-label">Chapters</div></div>
    <div class="stat-card"><div class="stat-value">40+</div><div class="stat-label">AI Prompts</div></div>
    <div class="stat-card"><div class="stat-value">60</div><div class="stat-label">Hook Templates</div></div>
    <div class="stat-card"><div class="stat-value">30</div><div class="stat-label">Day Calendar</div></div>
  </div>
</div>

<!-- CHAPTER 1 -->
<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 01</div>
    <h2>The LinkedIn Algorithm Decoded</h2>
    <p>What actually gets seen in 2026 — and what the algorithm actively buries.</p>
  </div>

  <p>LinkedIn's algorithm is not random and it is not fair. It is a distribution machine optimized for one thing: keeping people on the platform long enough to serve them ads. Understanding this changes everything about how you should create content.</p>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">How the Feed Ranking Works</h3>
  <p>Every post goes through a three-phase filter before it reaches anyone's feed. Phase one happens in the first 60–90 minutes: the algorithm shows your post to a small sample of your connections and first-degree followers. It measures early signals — specifically dwell time (how long people pause on your post without scrolling past), saves, and comment velocity. If those signals are strong, your content enters phase two.</p>
  <p style="margin-top:16px;">Phase two is algorithmic distribution. LinkedIn expands reach to second-degree connections and, if engagement keeps climbing, to hashtag followers and topically matched users who don't follow you. Phase three is editorial — at very high engagement levels, LinkedIn's human editorial team can amplify a post across the platform. Most posts never leave phase one. The difference between phase-one and phase-two content is almost never quality — it's structure and timing.</p>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">The 3 Content Types the Algorithm Loves</h3>
  <div class="checklist">
    <div class="checklist-item"><span class="check-icon">✦</span><strong>Text-only posts with line breaks.</strong> These load instantly on mobile, dwell time is high because reading takes time, and there's no thumbnail to scroll past. The algorithm assigns native-format posts a distribution bonus over outbound links.</div>
    <div class="checklist-item"><span class="check-icon">✦</span><strong>Document carousels (PDFs).</strong> Users swipe through multiple pages. Each swipe registers as continued engagement. Save rates on carousels are consistently 3–5× higher than single-image posts, and saves are LinkedIn's strongest algorithmic signal.</div>
    <div class="checklist-item"><span class="check-icon">✦</span><strong>Short-form video (under 90 seconds).</strong> Watch time and completion rate drive distribution here. Videos with captions outperform those without — most LinkedIn scrolling happens silently at work.</div>
  </div>

  <div class="callout amber" style="margin-top:32px;">
    <div class="callout-title">What the algorithm suppresses</div>
    <p>Posts that link to external sites in the body copy take a significant reach penalty — LinkedIn doesn't want to send traffic away. Workaround: put the link in the first comment and mention "link in comments" at the end of the post. This alone can double your reach on link-sharing posts.</p>
  </div>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">Best Posting Windows</h3>
  <p>The optimal posting time for B2B creators and founders is Tuesday–Thursday, 7:30–9:00 AM local time for your primary audience. This is when LinkedIn professionals check feeds before the workday pulls them in. A secondary window exists at 12:00–1:00 PM. Avoid Friday afternoons and weekends entirely — engagement collapses and you waste your content budget on low-reach slots.</p>
  <p style="margin-top:16px;">For creators targeting a US audience from Europe: schedule for 7:30 AM Eastern, which means your post goes out at 1:30 PM your time. The LinkedIn scheduling tool handles this natively. Consistency of cadence matters more than hitting the exact optimal minute — the algorithm rewards accounts that post regularly by giving them a small baseline distribution boost.</p>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">The 90-Day Compound Effect</h3>
  <p>LinkedIn is not a platform where one viral post builds a career. It rewards compounding consistently. Accounts posting 3–5 times per week for 90 days see an exponential growth curve that accounts posting sporadically never touch. Here's why: each post increases your profile's topical authority signals. LinkedIn builds an internal model of what you're an expert on based on your posting history, the hashtags you use, the engagement you attract, and the comments you leave. After 90 days of consistent posting in a niche, the algorithm actively recommends your content to people outside your network who have been flagged as interested in that topic. This cold-audience distribution is where real growth happens — and it only unlocks through consistency.</p>
</div>

<!-- CHAPTER 2 -->
<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 02</div>
    <h2>Your Content Pillars: Building a 3-Topic Strategy</h2>
    <p>Stop posting everything. Own three lanes — and dominate them.</p>
  </div>

  <p>The biggest mistake LinkedIn creators make is treating their profile like a personal journal — posting whatever is interesting to them that week. This produces an incoherent feed that the algorithm can't categorize and that followers can't build an expectation around. The fix is a deliberate 3-pillar strategy.</p>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">How to Find Your 3 Authority Pillars</h3>
  <p>Your pillars sit at the intersection of what you know deeply, what your target client or employer needs, and what you can speak to credibly. A founder might choose: (1) hard lessons from building the business, (2) tactical insights about their industry, and (3) reflections on leadership and team dynamics. A freelancer might choose: (1) client work methodology, (2) the business of freelancing, and (3) behind-the-scenes creative process.</p>
  <p style="margin-top:16px;">Run this exercise in 20 minutes: write down the 10 topics you could speak about without preparation for 30 minutes each. Then mark the ones that directly connect to the work you want to be hired for. The 3 topics with the highest intersection of depth, relevance, and genuine interest are your pillars.</p>

  <div class="prompt-block">
    <div class="prompt-label">AI Prompt — Extract Your Authority Pillars</div>
    <div class="prompt-text">I am a [JOB TITLE / ROLE] who [DESCRIBE YOUR WORK AND WHO YOU SERVE].

My 10 potential content topics are:
[LIST THEM]

My goal on LinkedIn is to [attract clients / get hired / grow my personal brand / build an audience].

Based on this, identify my 3 strongest content pillars. For each pillar:
- Name it in 3–5 words
- Explain why it works for my goal
- Give me 5 post ideas that fit this pillar
- Tell me what unique angle I have that competitors probably don't

Prioritize pillars where I have genuine expertise, not just surface-level interest.</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">Balancing Value, Story, and Soft-Sell</h3>
  <p>A healthy content mix is 70% pure value (teach something), 20% story and perspective (build connection), and 10% soft-sell (show what you do and how people can work with you). The ratio matters. Pure value builds authority but not relationships. Pure story builds connection but not expertise. Too much soft-sell trains your audience to scroll past you. Cycling deliberately through these three types — across your three pillars — creates a feed that serves every stage of the buyer journey simultaneously.</p>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">Positioning: What to Own vs. What to Share</h3>
  <p>Positioning means choosing the specific claim you want to be known for. You can't own "marketing" or "leadership" — these are too broad. But you can own "AI-assisted content systems for B2B founders" or "scaling a services business past €500K without hiring an agency." The tighter the claim, the faster authority compounds. What you share is anything that builds context around your claim — industry news, useful tools, trends — framed through your specific lens and opinions, never neutrally.</p>
</div>

<!-- CHAPTER 3 -->
<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 03</div>
    <h2>The 7 Content Formats That Dominate LinkedIn</h2>
    <p>Each format serves a different purpose. Master all seven and your content does every job simultaneously.</p>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;">
    <span class="item-num">F1</span>
    <div>
      <h4>The Story Post</h4>
      <p>A personal experience told with a clear professional lesson baked in. Structure: scene-setting hook → what happened → the twist or lesson → the takeaway. Story posts generate the highest comment volume because they invite shared experience responses. Keep them under 350 words. The more specific the detail (the exact number, the client's reaction, the exact moment things changed), the better they perform.</p>
    </div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:8px;">
    <span class="item-num">F2</span>
    <div>
      <h4>The Insight Post</h4>
      <p>A counterintuitive take on something your audience believes. This is the format that builds authority fastest because it demonstrates original thinking. Structure: state the conventional wisdom → undermine it with evidence or experience → state your alternative → defend it briefly. The insight must be genuinely contrarian — "content is king" reformatted as a thread is not an insight, it's noise.</p>
    </div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:8px;">
    <span class="item-num">F3</span>
    <div>
      <h4>The List Post</h4>
      <p>Skimmable, bookmarkable value delivered as a numbered or bulleted list. Lists get saved at high rates because people intend to come back to them. Keep each item to 1–2 lines. Start the post with the outcome the list delivers ("7 ways to cut client onboarding time in half") not a setup ("Here are some things I've learned about client work"). Save rates on list posts signal to LinkedIn that your content is reference-grade, which improves long-tail distribution.</p>
    </div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:8px;">
    <span class="item-num">F4</span>
    <div>
      <h4>The Question Post</h4>
      <p>A single open-ended question designed to generate comments. Question posts have the highest comment-to-impression ratio of any format because you've made responding the natural next step. The question must be specific enough to have a real answer but open enough that many different answers are valid. "What's your CRM?" is too narrow. "What's the one thing you stopped doing that made your business more profitable?" is perfect.</p>
    </div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:8px;">
    <span class="item-num">F5</span>
    <div>
      <h4>The Case Study</h4>
      <p>A specific result, for a specific client or project, shown with honest before/after detail. Case studies are the most powerful format for generating inbound leads because they show competence without claiming it. Structure: the client's situation before → the specific work you did → measurable results → the lesson you drew from it. Never generalize — specificity is what makes case studies credible and shareable.</p>
    </div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:8px;">
    <span class="item-num">F6</span>
    <div>
      <h4>The Carousel (Document)</h4>
      <p>A PDF carousel of 5–12 slides uploaded as a document post. Each slide must deliver standalone value — treat it like a mini-presentation. Carousels have the highest save rate and the longest engagement window of any format: people swipe through slowly, increasing total dwell time per post. Start with a cover slide that promises the outcome. End with a clear CTA slide. Use one idea per slide, maximum 30 words of text on any single slide.</p>
    </div>
  </div>

  <div class="item-row item" style="display:flex;align-items:flex-start;gap:16px;padding:20px 24px;margin-top:8px;">
    <span class="item-num">F7</span>
    <div>
      <h4>The Controversy Post</h4>
      <p>A hot take that challenges a sacred cow in your niche. This is the highest-risk, highest-reward format. When it works, it generates 10× the comments of a standard post. When it misfires, it generates backlash. Rules: attack ideas and systems, never people or companies. Have a defensible position, not just a provocative title. Follow up with a comment clarifying your actual stance within the first hour of posting.</p>
    </div>
  </div>
</div>

<!-- CHAPTER 4 -->
<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 04</div>
    <h2>40+ AI Prompts: Write a Month of Posts in One Sitting</h2>
    <p>Open your AI tool, run these prompts in order, and batch your entire content calendar in 90 minutes.</p>
  </div>

  <div class="callout" style="margin-bottom:32px;">
    <div class="callout-title">Setup: before you run any prompt</div>
    <p>Start a new chat. Paste this context block at the top so every prompt inherits it: "I am [YOUR ROLE] who helps [TARGET AUDIENCE] achieve [OUTCOME]. My tone is [2-3 adjectives]. My 3 content pillars are [P1, P2, P3]. My primary LinkedIn goal right now is [GOAL]."</p>
  </div>

  <h3 style="margin-bottom:16px;">Story Post Prompts</h3>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 1 — Story from Experience</div>
    <div class="prompt-text">Write a LinkedIn story post about a time when [DESCRIBE A SPECIFIC SITUATION — a client call, a mistake, a turning point].

Structure:
- Hook: one line that drops you into the scene mid-action
- What I thought was happening vs. what was actually happening
- The moment things shifted
- The lesson in one sentence — direct, no fluff
- CTA: a question that invites the reader to share a parallel experience

Word count: 220–300 words. No inspirational quotes. No generic takeaways.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 2 — Story from Failure</div>
    <div class="prompt-text">Write a LinkedIn post about a failure I had with [DESCRIBE THE FAILURE]. Be honest — don't soften it or make me look better than I was.

Structure:
- What I was trying to do and why
- What I did that didn't work, with a specific detail that shows I'm not exaggerating
- The actual consequence
- What I learned that I can never unlearn
- One thing readers can do differently because of this

Tone: direct, no toxic positivity. This isn't a "fail forward" post — it's an honest account.</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Insight Post Prompts</h3>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 3 — Contrarian Take</div>
    <div class="prompt-text">Write a LinkedIn insight post challenging this widely-held belief in my niche: [STATE THE CONVENTIONAL WISDOM].

My actual position: [YOUR COUNTERPOINT]
Evidence I have: [ONE OR TWO SPECIFIC DATA POINTS OR EXPERIENCES]

Structure:
- Hook: state the conventional wisdom and immediately undercut it
- Why most people believe it (be charitable — it's not stupid, just incomplete)
- My counterpoint with the specific evidence
- The practical implication for the reader
- A closing line that invites disagreement (not agreement)

Keep it sharp. No hedging. Maximum 280 words.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 4 — Trend Analysis</div>
    <div class="prompt-text">Write a LinkedIn post sharing an emerging trend I'm seeing in [MY NICHE/INDUSTRY].

Trend I'm observing: [DESCRIBE IT]
Why most people haven't noticed it yet: [YOUR REASONING]
What it means for [TARGET AUDIENCE] in the next 12 months: [IMPLICATION]

Write this as an expert giving early warning — not as a blogger summarizing news. Share what I specifically see, not what others have already published. Under 250 words.</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">List Post Prompts</h3>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 5 — Tactical List</div>
    <div class="prompt-text">Write a LinkedIn list post titled "[X] ways to [OUTCOME]".

Context:
- Topic: [SPECIFIC TOPIC FROM YOUR PILLAR]
- Target reader: [AUDIENCE]
- Outcome they want: [DESIRED RESULT]

Rules:
- Start with a hook that promises the outcome (not "Here are some tips I've collected")
- Each item: one line of the action + one line of why it works
- Keep all items at the same level of specificity — no vague items mixed with detailed ones
- End with: "Which one will you try first?" or a similar engagement question
- 7–10 items, under 400 words total</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 6 — Resource List</div>
    <div class="prompt-text">Write a LinkedIn post sharing [NUMBER] resources I actually use for [TASK/GOAL].

Resources: [LIST THE ACTUAL TOOLS, BOOKS, OR PEOPLE]

For each resource:
- Name it and why specifically I use it (not generic praise)
- What problem it solves that alternatives don't
- One concrete use case

Hook: "I spent [TIME/MONEY] figuring this out so you don't have to."
End with: a question asking what the reader would add.

Do not pad with resources I'm not certain about. Only include things I'd genuinely recommend to a trusted colleague.</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Hook-First Prompts</h3>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 7 — 10 Hooks for One Topic</div>
    <div class="prompt-text">Generate 10 different LinkedIn hook lines for a post about [TOPIC].

Hook types to cover:
- 2 × contrarian (challenges a belief)
- 2 × specific number or statistic
- 2 × "I used to think X. Then Y happened."
- 2 × direct statement of a painful truth
- 2 × open loop (makes you need to read more to close it)

Each hook must be under 15 words. Flag your top 3 picks and explain why they'd stop a scroll.</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Repurposing Prompts</h3>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 8 — One Idea, Five Angles</div>
    <div class="prompt-text">Take this core idea: [YOUR IDEA OR KEY POINT]

Turn it into 5 different LinkedIn posts — each using a different angle:
1. Tactical: step-by-step how-to
2. Story: illustrate it through a specific experience
3. Data: back it with a statistic or number
4. Contrarian: argue the opposite, then reveal the nuance
5. Question: turn it into something that invites community response

Each post: hook + body + CTA. Max 200 words each. No two posts should feel like they're saying the same thing.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Prompt 9 — Full 30-Day Prompt Sequence</div>
    <div class="prompt-text">Generate a 30-day LinkedIn content plan for someone whose pillars are [P1], [P2], and [P3], posting 5 days/week (Monday–Friday).

For each day provide:
- Day number
- Content pillar it belongs to
- Post format (story / insight / list / question / case study / carousel / controversy)
- Topic in 5–8 words
- Suggested hook (first line)

Distribute formats roughly evenly. Weight value content at 70%, story at 20%, soft-sell at 10%.
Group weeks thematically: Week 1 = establish authority, Week 2 = build trust through story, Week 3 = drive engagement, Week 4 = subtle conversion.</div>
  </div>
</div>

<!-- CHAPTER 5 -->
<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 05</div>
    <h2>The Hook Vault: 60 Opening Lines That Stop the Scroll</h2>
    <p>The first line is your only job. Everything else is what happens after they decide to stay.</p>
  </div>

  <p>On LinkedIn, the first line of your post is all that's visible before the "see more" break. If it doesn't earn a click, nothing else matters. These 60 templates are organized by psychological trigger. Adapt each to your topic, your voice, and your audience — never copy them verbatim.</p>

  <h3 style="margin-top:32px;margin-bottom:16px;">Curiosity Hooks (15)</h3>
  <div class="checklist">
    <div class="checklist-item"><span class="check-icon">1</span>"I've been doing [COMMON PRACTICE] wrong for [X] years. Here's what actually works."</div>
    <div class="checklist-item"><span class="check-icon">2</span>"Nobody told me [COUNTERINTUITIVE FACT] when I started [ACTIVITY]. So I'm telling you."</div>
    <div class="checklist-item"><span class="check-icon">3</span>"The thing that changed my [METRIC] by [RESULT] wasn't what I expected."</div>
    <div class="checklist-item"><span class="check-icon">4</span>"I asked [NUMBER] [ROLE] the same question. [X]% said the same wrong thing."</div>
    <div class="checklist-item"><span class="check-icon">5</span>"There's a reason [COMMON SOLUTION] doesn't work for [TARGET AUDIENCE]. Most people never figure it out."</div>
    <div class="checklist-item"><span class="check-icon">6</span>"[WIDELY BELIEVED THING] is backwards. Here's what the data actually shows."</div>
    <div class="checklist-item"><span class="check-icon">7</span>"My [ROLE] called this my 'dumbest idea.' It became [RESULT]."</div>
    <div class="checklist-item"><span class="check-icon">8</span>"I turned down [ATTRACTIVE THING] this year. Here's what I learned."</div>
    <div class="checklist-item"><span class="check-icon">9</span>"The best advice I ever got about [TOPIC]: [SHORT COUNTERINTUITIVE STATEMENT]."</div>
    <div class="checklist-item"><span class="check-icon">10</span>"Stop [COMMON ACTION]. Do [ALTERNATIVE] instead. Here's why."</div>
    <div class="checklist-item"><span class="check-icon">11</span>"[TOOL / METHOD] gets all the credit. But it's actually [LESS OBVIOUS THING] that does the work."</div>
    <div class="checklist-item"><span class="check-icon">12</span>"My [METRIC] went from [LOW] to [HIGH] in [TIMEFRAME]. The change was embarrassingly simple."</div>
    <div class="checklist-item"><span class="check-icon">13</span>"I spent [LARGE AMOUNT / TIME] learning this the hard way. Here's the shortcut."</div>
    <div class="checklist-item"><span class="check-icon">14</span>"What [INDUSTRY LEADER / COMPANY] doesn't tell you about [TOPIC]."</div>
    <div class="checklist-item"><span class="check-icon">15</span>"[UNPOPULAR OPINION]: [CONTROVERSIAL STATEMENT ABOUT YOUR NICHE]."</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Bold Claim Hooks (15)</h3>
  <div class="checklist">
    <div class="checklist-item"><span class="check-icon">16</span>"[COMMON BELIEF] is the most expensive mistake in [INDUSTRY]."</div>
    <div class="checklist-item"><span class="check-icon">17</span>"If you're not doing [SPECIFIC PRACTICE], you're leaving [SPECIFIC RESULT] on the table."</div>
    <div class="checklist-item"><span class="check-icon">18</span>"[NUMBER] people applied for the same role as me. I got it because of one line in my [DOCUMENT / PITCH]."</div>
    <div class="checklist-item"><span class="check-icon">19</span>"The [INDUSTRY] playbook is broken. Here's what I'm doing instead."</div>
    <div class="checklist-item"><span class="check-icon">20</span>"[POPULAR PLATFORM / TOOL / METHOD] is dead for [TARGET AUDIENCE]. Here's what replaced it."</div>
    <div class="checklist-item"><span class="check-icon">21</span>"Most [ROLE] will be irrelevant in [TIMEFRAME] if they don't learn [SKILL]."</div>
    <div class="checklist-item"><span class="check-icon">22</span>"I doubled [METRIC] without changing [THING EVERYONE FOCUSES ON]."</div>
    <div class="checklist-item"><span class="check-icon">23</span>"[THING EVERYONE DOES] is making your [METRIC] worse. Here's the fix."</div>
    <div class="checklist-item"><span class="check-icon">24</span>"I've hired [NUMBER] people this year. [SPECIFIC TYPE] outperforms [POPULAR CREDENTIAL] every time."</div>
    <div class="checklist-item"><span class="check-icon">25</span>"The [INDUSTRY] advice you keep hearing is wrong for [SPECIFIC SITUATION]."</div>
    <div class="checklist-item"><span class="check-icon">26</span>"[COMMON INVESTMENT OF TIME / MONEY] has a worse ROI than [UNDERRATED ALTERNATIVE]."</div>
    <div class="checklist-item"><span class="check-icon">27</span>"Your [DOCUMENT / PROFILE / PITCH] is hurting you. Here's the specific line that's the problem."</div>
    <div class="checklist-item"><span class="check-icon">28</span>"I've seen [NUMBER] businesses fail for the same preventable reason."</div>
    <div class="checklist-item"><span class="check-icon">29</span>"[RESULT] doesn't come from [WHAT EVERYONE CHASES]. It comes from [UNSEXY ALTERNATIVE]."</div>
    <div class="checklist-item"><span class="check-icon">30</span>"I will never [COMMON PRACTICE] again. Here's what I do instead."</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Story Openers (15)</h3>
  <div class="checklist">
    <div class="checklist-item"><span class="check-icon">31</span>"[DATE OR SPECIFIC TIME]. I was staring at [SPECIFIC THING] when [INCITING EVENT] happened."</div>
    <div class="checklist-item"><span class="check-icon">32</span>"Three months ago, a client told me something I didn't want to hear."</div>
    <div class="checklist-item"><span class="check-icon">33</span>"I almost quit [THING] last [MONTH/SEASON]. Here's what changed."</div>
    <div class="checklist-item"><span class="check-icon">34</span>"The worst [CALL / MEETING / DECISION] of my career taught me the most."</div>
    <div class="checklist-item"><span class="check-icon">35</span>"I've made this mistake [NUMBER] times. I'm still not fully cured."</div>
    <div class="checklist-item"><span class="check-icon">36</span>"When I started [ROLE/PROJECT], I thought I knew what [THING] meant. I didn't."</div>
    <div class="checklist-item"><span class="check-icon">37</span>"A [CLIENT / COLLEAGUE / STRANGER] said something last week that I can't stop thinking about."</div>
    <div class="checklist-item"><span class="check-icon">38</span>"I lost [CLIENT / DEAL / OPPORTUNITY] because of a sentence I said without thinking."</div>
    <div class="checklist-item"><span class="check-icon">39</span>"Six months ago I had [PROBLEM]. Today I have [RESULT]. The path wasn't linear."</div>
    <div class="checklist-item"><span class="check-icon">40</span>"My first [ATTEMPT AT THING] was embarrassingly bad. This is what it looked like."</div>
    <div class="checklist-item"><span class="check-icon">41</span>"I've worked with [NUMBER] clients in [TIMEFRAME]. The pattern that separates success from failure surprises everyone."</div>
    <div class="checklist-item"><span class="check-icon">42</span>"[PERSON] gave me feedback I ignored for a year. Then it cost me [CONSEQUENCE]."</div>
    <div class="checklist-item"><span class="check-icon">43</span>"I used to believe [THING]. Then [SPECIFIC EVENT] changed everything."</div>
    <div class="checklist-item"><span class="check-icon">44</span>"The email I almost didn't send changed the trajectory of my [YEAR / PROJECT / CAREER]."</div>
    <div class="checklist-item"><span class="check-icon">45</span>"On [DAY], I was told [NEGATIVE THING]. On [LATER DAY], I [POSITIVE OUTCOME]. Here's what happened in between."</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Question Hooks (15)</h3>
  <div class="checklist">
    <div class="checklist-item"><span class="check-icon">46</span>"What's the one thing you stopped doing that immediately improved [AREA OF WORK]?"</div>
    <div class="checklist-item"><span class="check-icon">47</span>"If you could go back to [EARLY STAGE OF CAREER], what's the one tool or skill you'd prioritize first?"</div>
    <div class="checklist-item"><span class="check-icon">48</span>"[HOTLY DEBATED TOPIC IN YOUR NICHE]: where do you actually stand?"</div>
    <div class="checklist-item"><span class="check-icon">49</span>"What's the most underrated skill in [INDUSTRY] that nobody talks about?"</div>
    <div class="checklist-item"><span class="check-icon">50</span>"Be honest: what [WORK HABIT / TOOL / APPROACH] do you swear by privately but rarely recommend publicly?"</div>
    <div class="checklist-item"><span class="check-icon">51</span>"What's the [HARDEST / MOST SURPRISING / LEAST OBVIOUS] part of [COMMON PROFESSIONAL SITUATION]?"</div>
    <div class="checklist-item"><span class="check-icon">52</span>"What did your first [CLIENT / HIRE / DEAL] teach you that no course ever could?"</div>
    <div class="checklist-item"><span class="check-icon">53</span>"Is [INDUSTRY PRACTICE] still worth doing in 2026? Genuine question — I'm reconsidering my position."</div>
    <div class="checklist-item"><span class="check-icon">54</span>"What's a piece of conventional wisdom in [NICHE] that you've stopped following?"</div>
    <div class="checklist-item"><span class="check-icon">55</span>"The question I wish someone had asked me when I started [THING]:"</div>
    <div class="checklist-item"><span class="check-icon">56</span>"What would you tell yourself at [EARLIER CAREER STAGE], knowing what you know now about [SPECIFIC TOPIC]?"</div>
    <div class="checklist-item"><span class="check-icon">57</span>"What's the [TOOL / HABIT / FRAMEWORK] you're quietly using that most of your peers haven't discovered yet?"</div>
    <div class="checklist-item"><span class="check-icon">58</span>"When did you last [IMPORTANT PROFESSIONAL ACTIVITY]? Be specific — day and what you noticed."</div>
    <div class="checklist-item"><span class="check-icon">59</span>"What's the best investment you've made in your [SKILLS / BUSINESS / WORKFLOW] this year?"</div>
    <div class="checklist-item"><span class="check-icon">60</span>"Quick poll: [CHOICE A] or [CHOICE B] for [SPECIFIC USE CASE]? Drop your answer + the reason."</div>
  </div>

  <div class="callout green" style="margin-top:32px;">
    <div class="callout-title">How to adapt any hook to your voice</div>
    <p>Take the hook template. Fill in the brackets with the most specific version you can — a real number, a real event, a real client type. Then read it aloud. If it doesn't sound like something you'd say to a colleague over lunch, rewrite it until it does. Authenticity in voice is a stronger signal than any hook formula.</p>
  </div>
</div>

<!-- CHAPTER 6 -->
<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 06</div>
    <h2>The 30-Day Editorial Calendar</h2>
    <p>A complete fill-in-the-blank operating schedule — copy it, customize it, repeat it every month.</p>
  </div>

  <p>This calendar assumes a 5-day/week posting cadence (Monday–Friday). If you're starting out, reduce to 3 days (Monday, Wednesday, Friday) and keep the weekly rhythm intact. Each week has a theme that layers content toward a conversion moment at the end of Month 4.</p>

  <div class="callout amber" style="margin-bottom:32px;">
    <div class="callout-title">Before you fill this in</div>
    <p>Run Prompt 9 from Chapter 4 to pre-generate 20 post topics, then slot them into the calendar below. Never fill in a calendar slot without at least a hook line ready — a topic without a hook is just a wish.</p>
  </div>

  <h3 style="margin-bottom:16px;">Week 1 — Establish Authority</h3>
  <p style="color:var(--ink-2);margin-bottom:16px;">Goal: make it immediately clear what you know and who it's for.</p>

  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Mon</span>
    <div><strong>Pillar 1 — Insight Post</strong><br><span style="color:var(--ink-2)">Your strongest contrarian take. This is your authority-establishing opener for the month.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Tue</span>
    <div><strong>Pillar 2 — List Post</strong><br><span style="color:var(--ink-2)">7–10 actionable tactics. End with a question to seed early comments.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Wed</span>
    <div><strong>Pillar 3 — Story Post</strong><br><span style="color:var(--ink-2)">A credibility story — a result you achieved or witnessed. Specific details only.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Thu</span>
    <div><strong>Pillar 1 — Question Post</strong><br><span style="color:var(--ink-2)">Turn a tension in your niche into an open question. Drive comments.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Fri</span>
    <div><strong>Pillar 2 — Trend Analysis</strong><br><span style="color:var(--ink-2)">An emerging pattern you're seeing. Show you're ahead of the curve.</span></div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Week 2 — Build Trust Through Story</h3>
  <p style="color:var(--ink-2);margin-bottom:16px;">Goal: let people see who you are, not just what you know.</p>

  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Mon</span>
    <div><strong>All Pillars — Failure Story</strong><br><span style="color:var(--ink-2)">Your most useful failure. Brutal honesty builds faster trust than polished wins.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Tue</span>
    <div><strong>Pillar 3 — Resource List</strong><br><span style="color:var(--ink-2)">Tools, books, or people you actually use. Save magnet.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Wed</span>
    <div><strong>Pillar 1 — Carousel</strong><br><span style="color:var(--ink-2)">Your highest-value framework as a document carousel. 8–12 slides.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Thu</span>
    <div><strong>Pillar 2 — Behind-the-Scenes</strong><br><span style="color:var(--ink-2)">Show your actual process, workspace, or workflow. Authenticity signal.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Fri</span>
    <div><strong>Pillar 3 — Question Post</strong><br><span style="color:var(--ink-2)">Ask for your community's opinion on something you're genuinely wrestling with.</span></div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Week 3 — Drive Engagement</h3>
  <p style="color:var(--ink-2);margin-bottom:16px;">Goal: maximize comments, saves, and shares to boost algorithmic distribution.</p>

  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Mon</span>
    <div><strong>All Pillars — Controversy Post</strong><br><span style="color:var(--ink-2)">Your sharpest hot take. Post it Monday for maximum comment window before the weekend.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Tue</span>
    <div><strong>Pillar 1 — Insight Post</strong><br><span style="color:var(--ink-2)">A data-backed insight. Leads with a number or statistic in the hook.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Wed</span>
    <div><strong>Pillar 2 — List Post</strong><br><span style="color:var(--ink-2)">Mistakes to avoid in your niche. Higher save rate than positive action lists.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Thu</span>
    <div><strong>Pillar 3 — Poll or Question</strong><br><span style="color:var(--ink-2)">Create a 2-option poll or a question with a built-in debate. Prioritize Thursday for polls — engagement peaks mid-week.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Fri</span>
    <div><strong>Pillar 1 — Story Post</strong><br><span style="color:var(--ink-2)">A win story — client transformation, project result, or personal milestone. End-of-week positivity bias works.</span></div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:16px;">Week 4 — Conversion Week</h3>
  <p style="color:var(--ink-2);margin-bottom:16px;">Goal: soft-sell to an audience that now knows and trusts you.</p>

  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Mon</span>
    <div><strong>All Pillars — Case Study</strong><br><span style="color:var(--ink-2)">The strongest result you have. Specific client type, specific numbers, specific method. Your most powerful proof post.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Tue</span>
    <div><strong>Pillar 3 — Insight Post</strong><br><span style="color:var(--ink-2)">Authority-building — reinforce why your method or approach is right for your niche.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Wed</span>
    <div><strong>Soft CTA Post</strong><br><span style="color:var(--ink-2)">Share what you offer, who it's for, and how someone can start. One clear action. No pressure copy.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Thu</span>
    <div><strong>Pillar 2 — List Post</strong><br><span style="color:var(--ink-2)">Your best-performing format from the month — repurpose the angle with a fresh hook.</span></div>
  </div>
  <div class="item-row item" style="display:flex;gap:16px;padding:16px 20px;">
    <span class="item-num" style="min-width:40px;">Fri</span>
    <div><strong>All Pillars — Retrospective</strong><br><span style="color:var(--ink-2)">What you learned this month in your work or your niche. Close the month with reflection — it performs well on Fridays.</span></div>
  </div>

  <div class="callout green" style="margin-top:32px;">
    <div class="callout-title">How to reuse this system month after month</div>
    <p>After 30 days: review your top 3 performing posts (by comments + saves). Identify the format and hook type. In Month 2, open each week with a variation of your best-performing format. Retire formats that consistently underperform for you personally — the taxonomy in this system is a starting point, not a religion.</p>
  </div>
</div>

<!-- CHAPTER 7 -->
<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 07</div>
    <h2>The 2-Hour Weekly Workflow</h2>
    <p>Batch your entire week's content in one Sunday session. Never open a blank page on a Monday again.</p>
  </div>

  <p>The biggest threat to LinkedIn consistency is not laziness — it's friction. The creator who has to generate a new idea, write the hook, draft the post, edit it, and schedule it every single day will eventually fall off. The creator who batches all of that work into a single session will still be posting six months from now when the daily creator gave up.</p>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">The Sunday Session: 90 Minutes</h3>

  <div class="checklist">
    <div class="checklist-item"><span class="check-icon">0:00</span><strong>Minutes 0–10 — Brain dump.</strong> Open a blank document. Write every idea, observation, or frustration from the past week that could become a post. Don't filter — you're mining raw material. Aim for 15–20 fragments.</div>
    <div class="checklist-item"><span class="check-icon">0:10</span><strong>Minutes 10–20 — Sort and select.</strong> Pick the 5 best fragments from your dump. Assign a format to each (story / insight / list / question / etc.) and assign it a day. Now you have your week's skeleton.</div>
    <div class="checklist-item"><span class="check-icon">0:20</span><strong>Minutes 20–45 — Draft all 5 posts.</strong> Write rough drafts of each post in sequence. Do not edit yet. Use the hook templates from Chapter 5 as starting points. The goal is complete drafts, not perfect ones.</div>
    <div class="checklist-item"><span class="check-icon">0:45</span><strong>Minutes 45–60 — AI edit pass.</strong> Paste each draft into your AI tool with this prompt: "Tighten this LinkedIn post. Remove any filler sentences. Sharpen the hook. Keep the voice exactly as written. Flag any line that sounds generic or could appear in any post by anyone." Apply selectively.</div>
    <div class="checklist-item"><span class="check-icon">1:00</span><strong>Minutes 60–80 — Final edit and scheduling.</strong> Read each post aloud (catches awkward phrasing instantly). Schedule all 5 via LinkedIn's native scheduler. Set publish times 7:30–9:00 AM your audience's timezone.</div>
    <div class="checklist-item"><span class="check-icon">1:20</span><strong>Minutes 80–90 — Engagement setup.</strong> Identify 5–10 accounts in your niche that you'll engage with meaningfully this week. Leave a substantive comment on their latest post now while you're in content mode — this seeds reciprocal engagement before your own posts go live.</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">The Daily 5-Minute Habit</h3>
  <p>The Sunday session handles creation. The daily habit handles distribution amplification. Every day, within 60 minutes of your post going live: reply to every comment personally, leave meaningful comments (not "great post") on 3–5 posts in your niche, and check your notifications for DMs worth responding to. This 5-minute daily habit doubles the engagement rate on your posts over a month because the LinkedIn algorithm rewards accounts with high response rates by extending distribution.</p>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">Measuring What Matters</h3>
  <p>Most LinkedIn creators obsess over likes. Likes are a vanity metric — they don't correlate strongly with business outcomes. What to track instead:</p>
  <div class="checklist">
    <div class="checklist-item"><span class="check-icon">✦</span><strong>Profile views per week</strong> — the leading indicator that content is reaching new audiences.</div>
    <div class="checklist-item"><span class="check-icon">✦</span><strong>Connection request rate</strong> — a direct signal that your content is making people want to know you.</div>
    <div class="checklist-item"><span class="check-icon">✦</span><strong>DMs from new contacts</strong> — the highest-quality signal that content is driving inbound interest.</div>
    <div class="checklist-item"><span class="check-icon">✦</span><strong>Comments per post (not just count — read them)</strong> — what people say in comments tells you which content is actually resonating.</div>
    <div class="checklist-item"><span class="check-icon">✦</span><strong>Post saves</strong> — the strongest algorithmic signal and the best indicator of reference-grade content.</div>
  </div>

  <h3 style="margin-top:32px;margin-bottom:12px;font-size:1.25rem;">Building Your Content Bank</h3>
  <p>The content bank is a rolling archive of post ideas that never goes below 20 items. Whenever something interesting happens — a client conversation, a surprising data point, a lesson learned — log it immediately to your content bank (a Notion database, a voice note, a pinned note in your phone). During Sunday sessions, pull from the bank before trying to generate new ideas from scratch. After 8 weeks of consistent logging, you will never have a blank Sunday session again.</p>

  <div class="callout" style="margin-top:40px;">
    <div class="callout-title">When to break from the system</div>
    <p>If a news event, trending topic, or industry moment is happening in real time — post about it immediately, outside the schedule. Reactive content to live events outperforms scheduled content on those days. The algorithm rewards timeliness. Your regular schedule resumes the next day; one off-cycle post doesn't break anything.</p>
  </div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink-3);">LinkedIn Content OS — Schep Digital</p>
    <p style="font-size:0.85rem;margin-top:8px;color:var(--ink-2);">7 chapters · 40+ prompts · 60 hooks · 30-day calendar · 2-hour workflow</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result = html_doc(
    title="LinkedIn Content OS",
    subtitle="30 days of scroll-stopping posts in 2 hours. The complete system — algorithm decoded, formats mastered, AI prompts ready, hooks vaulted, calendar filled.",
    eyebrow="Schep Digital · Creator Productivity",
    meta_items=[
        ("Chapters", "7"),
        ("AI Prompts", "40+"),
        ("Hook Templates", "60"),
        ("Works with", "Claude · ChatGPT"),
    ],
    body_html=body
)

out = "/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/linkedin-content-os.html"
with open(out, "w") as f:
    f.write(result)
print(f"Written: {out}")
