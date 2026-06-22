"""Generate Product 4: Gemini 1.5 Pro Guide — High-Context Architecture"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

body = """
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">What this guide covers</div>
    <p>Gemini 1.5 Pro's 1M-token context window isn't just a bigger box — it requires a different architecture of thought. This guide teaches you how to structure your inputs, manage context budgets, and build multi-step workflows that exploit long-context as a competitive advantage.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">1M</div><div class="stat-label">Token Context Window</div></div>
    <div class="stat-card"><div class="stat-value">~750K</div><div class="stat-label">Words in One Pass</div></div>
    <div class="stat-card"><div class="stat-value">11hrs</div><div class="stat-label">Audio You Can Analyze</div></div>
    <div class="stat-card"><div class="stat-value">30K</div><div class="stat-label">Lines of Code at Once</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 01</div>
    <h2>Understanding the Context Window</h2>
    <p>Why 1M tokens is not just "more of the same" — it's a paradigm shift.</p>
  </div>

  <h3>The old mental model (and why it breaks)</h3>
  <p style="color:var(--ink-2);">With 4K or 32K context models, you were forced to curate ruthlessly. Summarize before you analyze. Chunk before you process. The model was a spotlight — you pointed it at pieces of your problem one at a time.</p>
  <p style="color:var(--ink-2);">With 1M tokens, you can fit the entire problem space in one call. That changes not just what you can do — it changes how you should structure your thinking.</p>

  <h3>What fits in 1M tokens</h3>
  <table>
    <tr><th>Content Type</th><th>Approximate Volume</th><th>Use Case</th></tr>
    <tr><td>Plain text</td><td>~750,000 words</td><td>Entire book manuscripts, research archives</td></tr>
    <tr><td>Source code</td><td>~30,000 lines</td><td>Medium-sized codebases, monorepos</td></tr>
    <tr><td>PDFs (text-based)</td><td>~1,500 pages</td><td>Legal document sets, technical manuals</td></tr>
    <tr><td>Audio transcripts</td><td>~11 hours</td><td>Podcast archives, meeting recordings</td></tr>
    <tr><td>CSV/tabular data</td><td>~500,000 rows (simple)</td><td>Sales exports, user analytics</td></tr>
    <tr><td>Images</td><td>~1,500 images</td><td>Product catalogs, design systems</td></tr>
  </table>

  <div class="callout amber">
    <div class="callout-title">Context budget reality</div>
    <p>In practice, reserve 20% of the context for the model's working memory and output. Aim for 800K tokens of input maximum for 1M-context models. Overfilling causes attention degradation — the model starts missing things near the middle of the context window.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 02</div>
    <h2>Structuring Your Inputs</h2>
    <p>Document architecture matters. How you format inputs determines output quality.</p>
  </div>

  <h3>The PRIME framework for long-context inputs</h3>

  <div class="item"><h4>P — Preamble</h4><p>Start every long-context session with a role assignment and a description of what you've uploaded. "You are an expert [X]. I've given you [what]. Your task is [goal]." The model's attention is biased toward the beginning of context — use it.</p></div>

  <div class="item" style="margin-top:12px;"><h4>R — Reference Index</h4><p>For multi-document uploads, provide a brief index after the preamble: "Document 1 is the Q4 report. Document 2 is the competitor analysis. Document 3 is the product spec." This creates an anchor for cross-document citations.</p></div>

  <div class="item" style="margin-top:12px;"><h4>I — Instruction Clarity</h4><p>State exactly what format you want for the output before the documents. If you want a table, say table. If you want markdown, say markdown. Putting this after the documents buries it in a low-attention zone.</p></div>

  <div class="item" style="margin-top:12px;"><h4>M — Markers</h4><p>Use clear delimiters between documents: ===== BEGIN DOCUMENT 1 ===== and ===== END DOCUMENT 1 =====. Gemini respects these and uses them for citation accuracy.</p></div>

  <div class="item" style="margin-top:12px;"><h4>E — End Anchor</h4><p>After all documents, repeat your main question or task in one sentence. This exploits the recency bias — the model's attention is also elevated near the end of context.</p></div>

  <h3>Document ordering strategy</h3>
  <p style="color:var(--ink-2);">Gemini 1.5 Pro has a slight "lost in the middle" effect — attention is stronger at the beginning and end of the context window than in the middle. Put your most important documents first and last. Put supporting material in the middle.</p>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 03</div>
    <h2>Multi-Step Workflow Architecture</h2>
    <p>Chain Gemini calls to build pipelines that would take days of human work.</p>
  </div>

  <h3>The Refine-and-Expand Pattern</h3>
  <div class="prompt-block">
    <div class="prompt-label">Step 1 — Generate the skeleton</div>
    <div class="prompt-text">Create a detailed outline for [DELIVERABLE].
For each section, include:
- The main argument or point
- 3 specific sub-points
- What evidence or examples support it
- Approximate word count

Do not write the full content yet. Output the outline only.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Step 2 — Expand one section at a time (paste outline back in)</div>
    <div class="prompt-text">Here is the complete outline I'm working from:
[PASTE OUTLINE]

Write the full content for Section [N] only.
Maintain consistency with the tone established in sections already written:
[PASTE ANY COMPLETED SECTIONS]

Do not repeat content from earlier sections. Build on it.</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Step 3 — Coherence audit (upload all completed sections)</div>
    <div class="prompt-text">I've uploaded all sections of [DOCUMENT].
It was written in stages — check for:
1. Voice drift between sections
2. Repeated examples or statistics
3. Arguments in later sections that weaken earlier ones
4. Transitions that feel abrupt

Rewrite any transitions that score below 7/10 for smoothness.</div>
  </div>

  <h3>The Parallel Analysis Pattern</h3>
  <p style="color:var(--ink-2);">Upload the same document and run three simultaneous analysis prompts in separate Gemini windows. Combine the three outputs. Each window focuses on a different lens (financial, strategic, operational) — then synthesize the combined output with a fourth call.</p>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 04</div>
    <h2>Multimodal Architecture</h2>
    <p>Combining text, images, audio, and video in single Gemini sessions.</p>
  </div>

  <h3>Text + Image combinations</h3>
  <div class="prompt-block">
    <div class="prompt-label">Document + screenshot audit</div>
    <div class="prompt-text">I've uploaded [STRATEGY DOCUMENT] and [SCREENSHOTS OF YOUR PRODUCT/WEBSITE/APP].

Compare what the document promises against what the screenshots show.

Find:
1. Claims in the document not reflected in the product
2. Product features visible in screenshots not mentioned in the document
3. Tone or positioning inconsistencies between the written strategy and the visual product
4. The 3 highest-priority alignment gaps to fix

Be specific — quote the document claim and reference the screenshot that contradicts it.</div>
  </div>

  <h3>Audio + text combinations</h3>
  <div class="prompt-block">
    <div class="prompt-label">Sales call + product spec cross-reference</div>
    <div class="prompt-text">I've uploaded [N] sales call recordings and our product specification document.

Analyze:
1. What customers ask about that isn't in the spec (missing documentation)
2. What the spec promises that customers never ask about (likely not valued)
3. Objections customers raise vs. how the spec addresses them (gap analysis)
4. Exact customer phrases that should be in our marketing copy

Output: product documentation priorities + marketing copy improvements.</div>
  </div>

  <div class="callout green">
    <div class="callout-title">The multimodal advantage</div>
    <p>Text-only AI analysis misses 40-60% of the information in a real business context. Your strategy lives in documents, your execution lives in screenshots, your customer insights live in recordings. Gemini 1.5 Pro is the first model that can hold all three simultaneously — use this.</p>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 05</div>
    <h2>API & Programmatic Use</h2>
    <p>Automate Gemini 1.5 Pro for production workflows and batch processing.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Python — basic long-context API call</div>
    <div class="prompt-text">import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-pro")

with open("your_document.txt", "r") as f:
    document = f.read()

prompt = "Analyze the document and extract all action items:\\n\\n" + document
prompt += "\\n\\nFormat as JSON: owner, task, deadline, priority"

response = model.generate_content(
    prompt,
    generation_config=genai.GenerationConfig(
        temperature=0.1,
        max_output_tokens=8192
    )
)
print(response.text)</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Batch processing multiple documents</div>
    <div class="prompt-text">import os, json, time
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-pro")

docs_folder = "./documents"
results = []

for filename in os.listdir(docs_folder):
    if filename.endswith((".txt", ".md")):
        with open(os.path.join(docs_folder, filename)) as f:
            content = f.read()
        response = model.generate_content(
            "Summarize in 3 bullet points:\n\n" + content
        )
        results.append({"file": filename, "summary": response.text})
        time.sleep(1)

with open("summaries.json", "w") as f:
    json.dump(results, f, indent=2)
print("Processed", len(results), "documents")</div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 06</div>
    <h2>Common Mistakes &amp; How to Avoid Them</h2>
    <p>The errors that make long-context models produce poor results.</p>
  </div>

  <div class="item"><h4>Mistake 1: Burying the instruction</h4><p>Putting your actual question at line 200 of a 10,000-line prompt. Gemini's attention is biased toward beginning and end. Front-load the task, then upload content, then repeat the key question at the end.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Mistake 2: No output format specification</h4><p>Asking for analysis without specifying the format. Specify tables vs. prose, section headers, JSON keys, or bullet structure before uploading documents. The model inherits the format from its instructions, not from guessing your preference.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Mistake 3: Mixing unrelated documents</h4><p>Loading 10 documents that aren't thematically related and asking for synthesis. The model will hallucinate connections that don't exist. Group your uploads by question — one session per analytical goal.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Mistake 4: Using 1M context for short tasks</h4><p>For tasks under 2,000 tokens, Gemini Flash is faster and cheaper. Use Pro for tasks that genuinely require the long context. Don't use a bulldozer to plant a flower.</p></div>

  <div class="item" style="margin-top:12px;"><h4>Mistake 5: Not verifying citations</h4><p>Gemini will cite documents it was given — but with long context, citation accuracy can slip for documents in the middle of the window. Always spot-check 3-5 citations when the output will be used for decisions or published work.</p></div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Gemini 1.5 Pro High-Context Guide &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result = html_doc(
    title="Gemini 1.5 Pro: High-Context Architecture",
    subtitle="Master the 1M-token context window. Learn input structuring, multi-step workflow design, multimodal combinations, and API automation — the complete guide to exploiting Gemini's long-context advantage.",
    eyebrow="Schep Digital · Gemini Deep-Dive Guide",
    meta_items=[
        ("Context", "1M tokens"),
        ("Chapters", "6"),
        ("Includes", "Code examples"),
        ("Level", "Intermediate–Advanced"),
    ],
    body_html=body
)

out = "/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/04_gemini_15_pro_high_context.html"
with open(out, "w") as f:
    f.write(result)
print(f"Written: {out}")
