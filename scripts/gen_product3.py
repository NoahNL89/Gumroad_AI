"""Generate Product 3: Gemini Mega Prompt Pack"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

body = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">What makes this pack different</div>
    <p>Gemini's 1M-token context window changes everything. These prompts are engineered for that architecture — no chunking, no splitting, no lost context. Feed Gemini an entire codebase, document library, or research archive and extract structured intelligence in one pass.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">1M</div><div class="stat-label">Token Context Window</div></div>
    <div class="stat-card"><div class="stat-value">50+</div><div class="stat-label">Specialized Prompts</div></div>
    <div class="stat-card"><div class="stat-value">0</div><div class="stat-label">Chunking Required</div></div>
    <div class="stat-card"><div class="stat-value">10×</div><div class="stat-label">Research Speed Gain</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 01</div>
    <h2>The No-Chunk Protocol</h2>
    <p>Load everything. Extract everything. Never split your documents again.</p>
  </div>

  <p style="color:var(--ink-2);">Most people still treat Gemini like a short-context model — pasting excerpts, chunking PDFs, summarizing before asking questions. That's leaving 95% of the capability on the table. These prompts assume you've loaded the full artifact.</p>

  <h3>Master Document Analysis Prompt</h3>
  <div class="prompt-block">
    <div class="prompt-label">Load entire document first, then use this prompt</div>
    <div class="prompt-text">I've uploaded [DOCUMENT TYPE: full report / entire codebase / complete manuscript / research archive].

Do not summarize or sample — process the entire content.

Perform a complete analysis:

1. STRUCTURE MAP: List all major sections, chapters, or modules with their page/line ranges
2. KEY ENTITIES: People, companies, products, concepts mentioned (with frequency count)
3. CORE ARGUMENTS: Main thesis or claims, with supporting evidence locations (quote + location)
4. CONTRADICTIONS: Any internal inconsistencies or tension points
5. DATA EXTRACTION: All numerical data, statistics, dates — output as a structured table
6. GAPS: What's conspicuously missing or underexplored
7. CROSS-REFERENCES: Themes or entities that appear in multiple sections (show the connections)

Output format: structured markdown with section headers. Be exhaustive, not selective.</div>
  </div>

  <div class="callout green">
    <div class="callout-title">Why no chunking works</div>
    <p>When you chunk, the model loses cross-document connections. A reference in chapter 1 that contradicts a claim in chapter 12 becomes invisible. Full-context loads let Gemini maintain the entire semantic graph simultaneously — that's where the real intelligence lives.</p>
  </div>

  <h3>Multi-Document Synthesis</h3>
  <div class="prompt-block">
    <div class="prompt-label">Upload 2-10 documents, then run this</div>
    <div class="prompt-text">I've uploaded [N] documents: [BRIEF LIST OF WHAT THEY ARE].

Synthesize across all documents simultaneously. Do not analyze them separately.

Produce:
1. UNIFIED TIMELINE: All events/dates across all documents in chronological order
2. AGREEMENT MAP: Where all sources agree (with citations from each)
3. CONFLICT MAP: Where sources contradict each other (show the exact conflict)
4. UNIQUE INSIGHTS: What each document contributes that no other document covers
5. COMBINED CONCLUSION: The single most important thing the full corpus reveals
6. MISSING VOICE: What perspective or data source is absent from this corpus?

Format each section with document citations [Doc 1, p.X] or [Doc 2, §Y].</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 02</div>
    <h2>Code Intelligence at Scale</h2>
    <p>Load an entire repository. Get architecture-level insights no linter can give you.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Full codebase analysis — paste or upload all source files</div>
    <div class="prompt-text">I've uploaded the complete source code for [PROJECT NAME].

Analyze the entire codebase holistically — not file-by-file, but as a system.

Produce:
1. ARCHITECTURE DIAGRAM: Text-based diagram of the major components and their relationships
2. DATA FLOW: How data enters, transforms, and exits the system
3. DEPENDENCY GRAPH: Which modules depend on which (flag circular dependencies)
4. SECURITY SURFACE: Every external input point, auth check, and data sanitization location
5. DEAD CODE: Functions/classes that appear defined but never called
6. BOTTLENECKS: Synchronous operations in async contexts, N+1 query patterns, large allocations
7. TESTING GAPS: What has zero test coverage (list file:function)
8. REFACTOR PRIORITIES: Top 5 structural improvements ranked by impact/effort ratio

Do not describe what I can read — tell me what I cannot see by reading individual files.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Cross-file bug hunt</div>
    <div class="prompt-text">I've uploaded [PROJECT] source. A bug is causing [DESCRIBE THE SYMPTOM].

Hunt the root cause across the entire codebase:

1. Trace every code path that could produce this symptom
2. List all functions involved, with file and line numbers
3. Identify where state is modified between the trigger and the symptom
4. Find any race conditions, null propagation, or type coercion that fits this pattern
5. Propose the exact fix — show the before/after diff
6. List any other locations with the same bug pattern (proactive sweep)

Do not guess — cite file names and approximate line numbers for every claim.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 03</div>
    <h2>Research at 1M Scale</h2>
    <p>Upload entire research corpora. Extract structured knowledge in minutes.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Academic paper corpus analysis</div>
    <div class="prompt-text">I've uploaded [N] academic papers / research documents on [TOPIC].

I need a systematic literature review. Process all papers simultaneously:

1. METHODOLOGY TABLE: | Paper | Year | Method | Sample Size | Key Finding | Limitations |
2. CONSENSUS VIEW: What the field agrees on (cite at least 3 papers per claim)
3. OPEN DEBATES: Active disagreements between researchers (quote both sides)
4. METHODOLOGY GAPS: Research designs conspicuously absent from this corpus
5. CITATION NETWORK: Which papers cite each other (identify the most-cited foundational works)
6. RECENCY SHIFT: How the dominant view has shifted over time
7. PRACTICE IMPLICATIONS: What a practitioner should do based on this evidence base

Write the synthesis in clear prose. Tables for data, prose for interpretation.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Competitive intelligence sweep</div>
    <div class="prompt-text">I've uploaded [N] competitor documents: annual reports, product pages, job postings, blog posts, press releases.

Extract competitive intelligence across the full corpus:

1. STRATEGIC PRIORITIES: What each company is investing in (inferred from hiring, language, announcements)
2. CAPABILITY MAP: What each can do that others can't (based on explicit claims + product evidence)
3. POSITIONING GAPS: Market positions no one is claiming strongly
4. LANGUAGE PATTERNS: What words/phrases each company owns in their category
5. TRAJECTORY: Based on recent announcements, where is each headed in 12-24 months?
6. VULNERABILITY SIGNALS: Where are they defensive, vague, or conspicuously silent?

Output as a structured comparison matrix, then a narrative strategic memo (500 words).</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 04</div>
    <h2>Long-Form Content Creation</h2>
    <p>Generate book-length content with consistent voice and structure.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Full-length guide or ebook generator</div>
    <div class="prompt-text">Write a comprehensive guide on [TOPIC] for [AUDIENCE].

This is a long-form document — aim for 8,000-12,000 words. Do not truncate.

Structure:
- Executive summary (300 words)
- Introduction: why this matters now (500 words)
- Chapter 1: [SUBTOPIC 1] (1,200 words, with examples)
- Chapter 2: [SUBTOPIC 2] (1,200 words, with case study)
- Chapter 3: [SUBTOPIC 3] (1,200 words, with framework/model)
- Chapter 4: [SUBTOPIC 4] (1,200 words, with step-by-step implementation)
- Chapter 5: Common mistakes and how to avoid them (800 words)
- Chapter 6: Advanced tactics for [AUDIENCE already doing the basics] (1,000 words)
- Conclusion: The single most important thing to start with (300 words)
- Appendix: Resources, templates, checklists (500 words)

Maintain consistent voice: [describe your voice]. No padding — every paragraph earns its place.</div>
  </div>

  <div class="callout amber">
    <div class="callout-title">Context persistence across a session</div>
    <p>In Gemini, use "Gems" (custom AI personas with saved instructions) to persist your style guide, brand voice, and output requirements across all prompts. Load your style guide as a document once — every subsequent prompt inherits it without repasting.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Consistent multi-chapter voice check</div>
    <div class="prompt-text">I've uploaded [N] chapters of a book/guide I'm writing.

Audit the entire manuscript for consistency:

1. VOICE DRIFT: Sections where the tone shifts significantly from the baseline (chapters 1-2)
2. TERMINOLOGY INCONSISTENCY: Same concept named differently across chapters
3. EXAMPLE REPETITION: Examples or stories used more than once
4. ARGUMENT COHERENCE: Claims in later chapters that contradict or undermine earlier ones
5. PACING ANALYSIS: Chapters that feel rushed vs. padded (estimate reading time per chapter)
6. TRANSITION QUALITY: Score each chapter-to-chapter transition (smooth / abrupt / redundant)

Then rewrite the 3 weakest transitions to make them seamless.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 05</div>
    <h2>Data & Spreadsheet Analysis</h2>
    <p>Upload CSVs, exports, and reports. Get analysis no spreadsheet formula can produce.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Large dataset analysis</div>
    <div class="prompt-text">I've uploaded a dataset: [DESCRIBE: sales data / user analytics / survey results / financial records].

Columns: [LIST COLUMN NAMES]
Date range: [IF APPLICABLE]
Goal: [WHAT DECISION THIS ANALYSIS INFORMS]

Analyze the full dataset. Do not sample.

Produce:
1. DATA QUALITY REPORT: Missing values, outliers, duplicates, formatting inconsistencies
2. DISTRIBUTION SUMMARY: For each numeric column — mean, median, mode, std dev, range
3. CORRELATION MATRIX: Top 10 strongest correlations between variables
4. TREND ANALYSIS: How key metrics have changed over time (if date column exists)
5. SEGMENT BREAKDOWN: Split [KEY METRIC] by [CATEGORICAL VARIABLE] — show top and bottom 5
6. ANOMALY FLAGS: Rows or time periods that deviate significantly from the pattern
7. BUSINESS INSIGHT: The single most actionable finding from this data
8. RECOMMENDED NEXT ANALYSIS: What question you can't answer with this data alone

Output tables where data-heavy, prose where interpretive.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Customer data pattern finder</div>
    <div class="prompt-text">I've uploaded [CUSTOMER DATABASE EXPORT / CRM EXPORT].

Find behavioral patterns that predict [CHURN / HIGH LTV / REPEAT PURCHASE / UPGRADE].

Steps:
1. Identify all customers who [DID THE TARGET BEHAVIOR] and their shared attributes
2. Build a simple scoring model: which 3-5 attributes have the strongest predictive signal?
3. Show the false positive / false negative tradeoff for different threshold settings
4. Identify the "almost there" segment — customers close to [TARGET BEHAVIOR] who haven't triggered it yet
5. Recommend the intervention for each segment (email, offer, feature, support touch)

Output: scoring table + intervention playbook per segment.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 06</div>
    <h2>Video &amp; Audio Transcript Analysis</h2>
    <p>Upload full transcripts. Extract structured value from hours of recorded content.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Podcast or meeting corpus analysis</div>
    <div class="prompt-text">I've uploaded [N] transcripts from [PODCAST EPISODES / SALES CALLS / TEAM MEETINGS / INTERVIEWS].

Analyze the full corpus holistically:

1. TOPIC FREQUENCY MAP: What subjects come up most often, ranked by frequency
2. SPEAKER PATTERN: How different voices/roles speak differently about the same topics
3. RECURRING OBJECTIONS: Questions or pushback that appears across multiple transcripts
4. GOLD NUGGETS: The 10 most quotable, insight-dense passages across all transcripts
5. CUSTOMER LANGUAGE: Exact phrases customers/guests use (mining for marketing copy)
6. UNANSWERED QUESTIONS: Topics raised but never fully resolved across the corpus
7. CONTENT GAPS: Topics your audience clearly cares about that you haven't covered

Output a content brief with the top 5 pieces to create from this analysis.</div>
  </div>

  <div class="callout">
    <div class="callout-title">Pro workflow: audio → Gemini pipeline</div>
    <p>Record Loom → export transcript → paste into Gemini with this prompt. A 3-hour workshop becomes a structured knowledge base in 10 minutes. Use Google's native audio upload for even richer analysis — Gemini processes audio directly without transcription loss.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 07</div>
    <h2>Legal &amp; Contract Review</h2>
    <p>Load full contract documents. Identify risks and non-standard clauses instantly.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Contract risk analysis — not legal advice, strategic flag-raising</div>
    <div class="prompt-text">I've uploaded a [CONTRACT TYPE: SaaS agreement / employment contract / partnership agreement / NDA / vendor contract].

I am the [PARTY TYPE: vendor / employee / partner / buyer].

Analyze the entire document:

1. UNUSUAL CLAUSES: Anything non-standard for this contract type — flag and explain the risk
2. ONE-SIDED LANGUAGE: Clauses that heavily favor the other party with no reciprocal protection
3. MISSING PROTECTIONS: What a fair version of this contract would include that this one omits
4. TERMINATION TRAPS: Exit conditions, notice requirements, penalties for early termination
5. LIABILITY EXPOSURE: Indemnification scope, liability caps, insurance requirements
6. IP OWNERSHIP: What IP is created, who owns it, what licenses are granted
7. DISPUTE RESOLUTION: Jurisdiction, arbitration vs. court, class action waivers
8. RENEWAL TRAPS: Auto-renewal clauses, notice windows, price change provisions

Format: clause reference + risk level (high/medium/low) + plain-English explanation + suggested alternative language.</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Section 08</div>
    <h2>Advanced Gemini Techniques</h2>
    <p>System prompts, Gems, API usage, and multimodal combinations.</p>
  </div>

  <div class="item"><h4>Technique 1: The Standing Context Gem</h4><p>Create a Gem with your company brief, product description, brand voice, and target customer as the system prompt. Every prompt you run inherits this context. Never repaste your background again.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Technique 2: Multimodal + Text Fusion</h4><p>Upload a screenshot, diagram, or image alongside a text document. Ask Gemini to reconcile what the image shows against what the text claims. Useful for auditing slide decks against written strategy docs.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Technique 3: Iterative Document Building</h4><p>Start with a 200-word outline. Ask Gemini to expand section 1 to 500 words. Then upload the result back and ask it to maintain consistency while expanding section 2. The full document stays coherent because each iteration is in context.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Technique 4: The Contradiction Audit</h4><p>Upload your strategy doc, your website copy, your product spec, and your sales deck simultaneously. Ask Gemini: "Find every place these four documents contradict each other." Organizational alignment in minutes.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Technique 5: Historical Corpus + Current Question</h4><p>Upload 3 years of your company's meeting notes, strategy memos, or product decisions. Ask "Why did we decide X in 2023?" and get the full institutional reasoning — not a guess, but the actual documented context.</p></div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Gemini Mega Prompt Pack &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result = html_doc(
    title="Gemini Mega Prompt Pack",
    subtitle="50+ prompts engineered for Gemini's 1M-token context window. No chunking. No splitting. Load entire codebases, document libraries, and research archives — extract structured intelligence in one pass.",
    eyebrow="Schep Digital · Gemini-Native Prompt System",
    meta_items=[
        ("Context", "1M tokens"),
        ("Prompts", "50+"),
        ("Chunking", "Zero required"),
        ("Model", "Gemini 1.5 Pro / 2.0"),
    ],
    body_html=body
)

out = "/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/03_gemini_mega_prompt_pack.html"
with open(out, "w") as f:
    f.write(result)
print(f"Written: {out}")
