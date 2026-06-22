"""Generate Product 5: Local LLM Guide"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc

OLLAMA_SETUP = (
    "# Install\ncurl -fsSL https://ollama.com/install.sh | sh\n\n"
    "# Pull a model\nollama pull llama3.1\n\n"
    "# Run it\nollama run llama3.1\n\n"
    "# List models\nollama list"
)

API_EXAMPLE = (
    "import ollama\n\n"
    "response = ollama.chat(\n"
    "    model='llama3.1',\n"
    "    messages=[{'role': 'user', 'content': 'Write a Python CSV parser'}]\n"
    ")\n"
    "print(response['message']['content'])"
)

BATCH_SCRIPT = (
    "import ollama, json\nfrom pathlib import Path\n\n"
    "results = {}\n"
    "for doc in Path('./inbox').glob('*.txt'):\n"
    "    text = doc.read_text()\n"
    "    r = ollama.chat(model='llama3.1', messages=[\n"
    "        {'role': 'user', 'content': 'Summarize in 3 bullets:\\n\\n' + text}\n"
    "    ])\n"
    "    results[doc.name] = r['message']['content']\n\n"
    "with open('summaries.json', 'w') as f:\n"
    "    json.dump(results, f, indent=2)\n"
    "print('Done:', len(results), 'files')"
)

DOCKER_CMD = (
    "docker run -d -p 3000:8080 \\\n"
    "  --add-host=host.docker.internal:host-gateway \\\n"
    "  -v open-webui:/app/backend/data \\\n"
    "  --name open-webui --restart always \\\n"
    "  ghcr.io/open-webui/open-webui:main\n\n"
    "# Open http://localhost:3000"
)

body = f"""
<div class="page page-break">
  <div class="callout">
    <div class="callout-title">Why run AI locally?</div>
    <p>Privacy, cost control, offline capability, and unlimited rate limits. Local LLMs have crossed the quality threshold for most business tasks. This guide gets you from zero to productive in one afternoon.</p>
  </div>
  <div class="grid-2">
    <div class="stat-card"><div class="stat-value">€0</div><div class="stat-label">Per-Token Cost</div></div>
    <div class="stat-card"><div class="stat-value">100%</div><div class="stat-label">Data Privacy</div></div>
    <div class="stat-card"><div class="stat-value">∞</div><div class="stat-label">Rate Limit</div></div>
    <div class="stat-card"><div class="stat-value">Offline</div><div class="stat-label">No Internet Needed</div></div>
  </div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 01</div>
    <h2>Hardware Requirements</h2>
    <p>What you actually need — and what you can skip.</p>
  </div>

  <table>
    <tr><th>Model Size</th><th>VRAM Needed</th><th>RAM (CPU)</th><th>Quality Level</th></tr>
    <tr><td>3B–7B</td><td>4–8 GB GPU</td><td>8–16 GB</td><td>Drafting, Q&amp;A, summarization</td></tr>
    <tr><td>13B–14B</td><td>10–16 GB GPU</td><td>24–32 GB</td><td>Reasoning, coding, analysis</td></tr>
    <tr><td>30B–34B</td><td>24–40 GB GPU</td><td>48–64 GB</td><td>Near GPT-4 quality</td></tr>
    <tr><td>70B</td><td>40–80 GB GPU</td><td>80–128 GB</td><td>Competitive with frontier</td></tr>
  </table>

  <div class="callout amber">
    <div class="callout-title">No GPU? Start on CPU.</div>
    <p>Quantized models (Q4) run on CPU RAM at 2–5 tokens/second — slow but usable for batch tasks. A 7B Q4 on 16GB RAM handles most content tasks. Start here, upgrade later.</p>
  </div>

  <h3>Recommended setups</h3>
  <div class="item"><h4>Budget: CPU-only</h4><p>Ollama + Llama 3.1 8B Q4 on any 16GB RAM machine. 2–4 tokens/second. Good for overnight batch processing.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Mid-range: Consumer GPU</h4><p>RTX 3060 (12GB VRAM) + Mistral 7B Q8. 30–50 tokens/second. The productivity sweet spot for &lt;€400.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Power: RTX 4090</h4><p>24GB VRAM + Qwen 2.5 32B or Llama 3.3 70B Q4. 15–25 tokens/second at near-frontier quality.</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 02</div>
    <h2>Setting Up Ollama</h2>
    <p>10 minutes from zero to running a local model.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Install and run (macOS / Linux)</div>
    <div class="prompt-text">{OLLAMA_SETUP}</div>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Python API usage</div>
    <div class="prompt-text">{API_EXAMPLE}</div>
  </div>

  <h3>Model recommendations by task</h3>
  <table>
    <tr><th>Task</th><th>Best Local Model</th><th>Why</th></tr>
    <tr><td>Coding</td><td>Qwen2.5-Coder 14B</td><td>Best code quality under 20B params</td></tr>
    <tr><td>Writing</td><td>Llama 3.3 70B Q4</td><td>Best instruction following</td></tr>
    <tr><td>Reasoning</td><td>DeepSeek-R1 14B</td><td>Chain-of-thought built in</td></tr>
    <tr><td>Fast drafting</td><td>Mistral 7B Q8</td><td>Fastest quality-per-token</td></tr>
    <tr><td>Long documents</td><td>Qwen2.5 72B</td><td>128K context window</td></tr>
  </table>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 03</div>
    <h2>Open WebUI Setup</h2>
    <p>A ChatGPT-like interface for your local models.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Install with Docker</div>
    <div class="prompt-text">{DOCKER_CMD}</div>
  </div>

  <h3>Key features</h3>
  <div class="item"><h4>Model switching</h4><p>Switch between any Ollama model mid-conversation. Compare Llama vs. Mistral side by side.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Document RAG</h4><p>Upload PDFs, Word docs, or websites. Open WebUI builds a local vector index — answer questions from your documents without sending data anywhere.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Saved Personas</h4><p>Create "coding assistant", "copywriter", "analyst" personas each pre-loaded with context. Switch instantly.</p></div>
</div>

<div class="page page-break">
  <div class="section-header">
    <div class="section-num">Chapter 04</div>
    <h2>Batch Processing Workflows</h2>
    <p>Automate document processing, analysis, and content generation at scale.</p>
  </div>

  <div class="prompt-block">
    <div class="prompt-label">Process an entire folder of documents</div>
    <div class="prompt-text">{BATCH_SCRIPT}</div>
  </div>

  <div class="callout">
    <div class="callout-title">Where local beats cloud</div>
    <p>Sensitive client data, legal documents, financial records, HR files — anything you cannot legally send to external servers. Local models handle these with zero compliance risk. Also: iterative batch processing where API costs would reach hundreds of euros per month.</p>
  </div>

  <h3>Customization options</h3>
  <div class="item"><h4>System prompt injection</h4><p>Load a 2,000-word context about your business into every session without repasting. Create a Modelfile that bakes it in permanently.</p></div>
  <div class="item" style="margin-top:12px;"><h4>LoRA fine-tuning</h4><p>With 500+ examples of ideal outputs, fine-tune a 7B model with LoRA on a single GPU in 2–4 hours. Produces consistent style and domain knowledge without prompting.</p></div>
  <div class="item" style="margin-top:12px;"><h4>Modelfile customization</h4><p>Bake system prompts and generation parameters into a named Ollama model and share it with your team. No cloud account needed.</p></div>

  <div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);text-align:center;">
    <p class="text-dim" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;">Local LLM Guide &mdash; Schep Digital</p>
    <p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">schephenk.gumroad.com</p>
  </div>
</div>
"""

result = html_doc(
    title="Local LLM Setup Guide",
    subtitle="Run powerful AI on your own hardware. Zero API costs, total privacy, unlimited rate limits. From hardware selection to Ollama setup to production batch workflows — in one afternoon.",
    eyebrow="Schep Digital · Local AI Infrastructure Guide",
    meta_items=[
        ("Cost", "€0/month after setup"),
        ("Setup time", "~1 hour"),
        ("Includes", "Code examples"),
        ("Models", "Llama · Mistral · Qwen · DeepSeek"),
    ],
    body_html=body
)

out = "/home/administrator/NewGitHub/GumRoad_AI/downloads/pdfs/05_local_llm_guide.html"
with open(out, "w") as f:
    f.write(result)
print(f"Written: {out}")
