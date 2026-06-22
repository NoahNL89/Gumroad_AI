"""Shared CSS and HTML template for all Schep Digital PDF products."""

FONTS = "https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Epilogue:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap"

CSS = """
:root {
  --bg:        oklch(0.10 0.02 285);
  --surface:   oklch(0.14 0.025 285);
  --surface2:  oklch(0.17 0.03 285);
  --border:    oklch(0.24 0.03 285);
  --accent:    oklch(0.62 0.22 295);
  --accent-dim:oklch(0.50 0.16 295);
  --ink:       oklch(0.97 0.005 285);
  --ink-2:     oklch(0.78 0.01 285);
  --ink-3:     oklch(0.55 0.015 285);
  --green:     oklch(0.72 0.18 155);
  --amber:     oklch(0.80 0.18 75);
  --red:       oklch(0.65 0.22 25);
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 16px; }
body {
  font-family: 'Epilogue', system-ui, sans-serif;
  background: var(--bg);
  color: var(--ink);
  line-height: 1.65;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
h1,h2,h3,h4,h5 {
  font-family: 'Syne', system-ui, sans-serif;
  line-height: 1.2;
  letter-spacing: -0.02em;
}
code, pre, .mono {
  font-family: 'JetBrains Mono', monospace;
}

/* ── COVER ── */
.cover {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px 72px;
  background: linear-gradient(160deg, oklch(0.13 0.04 295) 0%, var(--bg) 60%);
  page-break-after: always;
}
.cover-eyebrow {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 32px;
}
.cover h1 {
  font-size: clamp(2.8rem, 6vw, 5rem);
  font-weight: 800;
  color: var(--ink);
  max-width: 820px;
  margin-bottom: 24px;
}
.cover-sub {
  font-size: 1.2rem;
  color: var(--ink-2);
  max-width: 560px;
  margin-bottom: 56px;
  line-height: 1.6;
}
.cover-meta {
  display: flex;
  gap: 40px;
  flex-wrap: wrap;
}
.cover-meta-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.cover-meta-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink-3);
}
.cover-meta-value {
  font-size: 1rem;
  font-weight: 600;
  color: var(--accent);
}
.brand-mark {
  margin-top: auto;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  color: var(--ink-3);
  text-transform: uppercase;
}

/* ── LAYOUT ── */
.page { max-width: 860px; margin: 0 auto; padding: 64px 72px; }
.page-break { page-break-after: always; }

/* ── SECTION HEADERS ── */
.section-header {
  padding: 40px 48px;
  background: linear-gradient(135deg, oklch(0.62 0.22 295 / 0.1) 0%, var(--surface) 100%);
  border: 1px solid oklch(0.62 0.22 295 / 0.25);
  border-radius: 12px;
  margin-bottom: 40px;
}
.section-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent-dim);
  margin-bottom: 8px;
}
.section-header h2 {
  font-size: 2rem;
  font-weight: 800;
  color: var(--ink);
}
.section-header p {
  margin-top: 12px;
  color: var(--ink-2);
  font-size: 1rem;
}

/* ── PROMPT / CODE BLOCKS ── */
.prompt-block {
  background: oklch(0.16 0.035 285);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 20px 24px;
  margin: 20px 0;
  position: relative;
}
.prompt-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent-dim);
  margin-bottom: 10px;
}
.prompt-text {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.82rem;
  line-height: 1.7;
  color: oklch(0.88 0.02 285);
  white-space: pre-wrap;
  word-break: break-word;
}

/* ── CALLOUTS ── */
.callout {
  background: oklch(0.62 0.22 295 / 0.07);
  border: 1px solid oklch(0.62 0.22 295 / 0.3);
  border-radius: 8px;
  padding: 20px 24px;
  margin: 24px 0;
}
.callout-title {
  font-family: 'Syne', system-ui, sans-serif;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 8px;
}
.callout p { color: var(--ink-2); font-size: 0.95rem; }

.callout.green {
  background: oklch(0.72 0.18 155 / 0.07);
  border-color: oklch(0.72 0.18 155 / 0.3);
}
.callout.green .callout-title { color: var(--green); }

.callout.amber {
  background: oklch(0.80 0.18 75 / 0.07);
  border-color: oklch(0.80 0.18 75 / 0.3);
}
.callout.amber .callout-title { color: var(--amber); }

/* ── ITEMS / LISTS ── */
.item {
  padding: 20px 24px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  margin: 12px 0;
}
.item h4 {
  font-size: 1rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 6px;
}
.item p { font-size: 0.92rem; color: var(--ink-2); }

.item-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  background: oklch(0.62 0.22 295 / 0.15);
  border: 1px solid oklch(0.62 0.22 295 / 0.35);
  border-radius: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--accent);
  margin-right: 12px;
  flex-shrink: 0;
}
.item-row {
  display: flex;
  align-items: flex-start;
  gap: 0;
}

/* ── GRID ── */
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 24px 0; }

/* ── STAT CARDS ── */
.stat-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 24px;
  text-align: center;
}
.stat-value {
  font-family: 'Syne', system-ui, sans-serif;
  font-size: 2.4rem;
  font-weight: 800;
  color: var(--accent);
  line-height: 1;
  margin-bottom: 8px;
}
.stat-label {
  font-size: 0.85rem;
  color: var(--ink-2);
}

/* ── CHECKLIST ── */
.checklist { list-style: none; margin: 16px 0; }
.checklist li {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
  font-size: 0.95rem;
  color: var(--ink-2);
}
.checklist li:last-child { border-bottom: none; }
.check-icon {
  width: 20px;
  height: 20px;
  border: 2px solid var(--border);
  border-radius: 4px;
  flex-shrink: 0;
  margin-top: 2px;
}

/* ── TABLE ── */
table { width: 100%; border-collapse: collapse; margin: 24px 0; }
th {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink-3);
  text-align: left;
  padding: 12px 16px;
  background: var(--surface);
  border: 1px solid var(--border);
}
td {
  padding: 12px 16px;
  border: 1px solid var(--border);
  font-size: 0.9rem;
  color: var(--ink-2);
  vertical-align: top;
}
tr:nth-child(even) td { background: oklch(0.12 0.02 285); }

/* ── TYPOGRAPHY UTILITIES ── */
p { margin-bottom: 16px; }
p:last-child { margin-bottom: 0; }
h2 { font-size: 1.8rem; font-weight: 700; margin: 40px 0 16px; }
h3 { font-size: 1.3rem; font-weight: 700; margin: 32px 0 12px; color: var(--ink); }
h4 { font-size: 1rem; font-weight: 700; margin: 24px 0 8px; }
.text-accent { color: var(--accent); }
.text-muted { color: var(--ink-2); }
.text-dim { color: var(--ink-3); }
.mb-8 { margin-bottom: 8px; }
.mb-16 { margin-bottom: 16px; }
.mb-32 { margin-bottom: 32px; }
.mt-32 { margin-top: 32px; }
.mt-48 { margin-top: 48px; }

/* ── IMAGES ── */
.img-cover-hero {
  width: 100%;
  max-height: 300px;
  object-fit: cover;
  object-position: center top;
  border-radius: 10px;
  margin: 28px 0 36px;
  display: block;
}
.img-interior-wrap {
  margin: 0 0 36px;
  page-break-inside: avoid;
}
.img-interior {
  width: 100%;
  max-height: 240px;
  object-fit: cover;
  object-position: center;
  border-radius: 8px;
  display: block;
}
.img-interior-caption {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink-3);
  text-align: center;
  margin-top: 8px;
}

/* ── PRINT ── */
@media print {
  body { background: var(--bg); }
  .cover { min-height: 100vh; }
  @page { margin: 0; size: A4; }
}
"""

def html_doc(title, subtitle, eyebrow, meta_items, body_html, cover_color=None):
    """Wrap body HTML in the full document shell."""
    meta_tags = "".join(
        f'<div class="cover-meta-item"><span class="cover-meta-label">{k}</span>'
        f'<span class="cover-meta-value">{v}</span></div>'
        for k, v in meta_items
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<div class="cover">
  <div class="cover-eyebrow">{eyebrow}</div>
  <h1>{title}</h1>
  <p class="cover-sub">{subtitle}</p>
  <div class="cover-meta">{meta_tags}</div>
  <p class="brand-mark" style="margin-top:64px;">Schep Digital &mdash; schephenk.gumroad.com</p>
</div>

{body_html}

</body>
</html>"""
