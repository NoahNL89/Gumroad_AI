#!/usr/bin/env python3
"""
Schep Digital — data-driven product PDF builder.

Replaces the one-off `gen_*.py` scripts (one ~600-line file per product) with a
single engine. A new product is now a JSON spec, not a new Python script.

Usage:
    python3 scripts/product_builder.py <spec.json>            # writes HTML
    python3 scripts/product_builder.py <spec.json> --pdf      # also renders PDF via headless Chrome
    python3 scripts/product_builder.py --demo                 # write a sample spec + HTML to verify the engine

Spec format (see build_demo_spec() for a complete example):
    {
      "slug": "ai-meeting-mastery",
      "title": "...", "subtitle": "...", "eyebrow": "Schep Digital · ...",
      "meta": [["Format", "PDF"], ["Pages", "26"]],
      "intro_callout": {"title": "...", "body": "...", "variant": "green"},   # optional
      "stats": [["€0", "Per-token cost"], ...],                                # optional
      "chapters": [
        {"num": "Chapter 01", "title": "...", "sub": "...",
         "blocks": [
            {"type": "p", "text": "..."},
            {"type": "h3", "text": "..."},
            {"type": "callout", "title": "...", "body": "...", "variant": "amber"},
            {"type": "prompt", "label": "...", "text": "code..."},
            {"type": "item", "h4": "...", "body": "..."},
            {"type": "checklist", "items": ["...", "..."]},
            {"type": "table", "headers": ["A","B"], "rows": [["1","2"]]},
            {"type": "stats", "cards": [["v","label"], ...]}
         ]}
      ],
      "closing": {"line": "Product — Schep Digital", "url": "schephenk.gumroad.com"}  # optional
    }
"""
import html
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from shared_css import html_doc  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "downloads" / "pdfs"

_VALID_CALLOUTS = {"", "green", "amber"}


def esc(text) -> str:
    """HTML-escape any text content. Newlines are preserved by CSS (pre-wrap) where used."""
    return html.escape(str(text), quote=False)


# ── Block renderers ─────────────────────────────────────────────────────────
def _callout(title, body, variant="") -> str:
    variant = variant if variant in _VALID_CALLOUTS else ""
    cls = f"callout {variant}".strip()
    return (f'<div class="{cls}"><div class="callout-title">{esc(title)}</div>'
            f'<p>{esc(body)}</p></div>')


def _prompt(label, text) -> str:
    return (f'<div class="prompt-block"><div class="prompt-label">{esc(label)}</div>'
            f'<div class="prompt-text">{esc(text)}</div></div>')


def _item(h4, body) -> str:
    return f'<div class="item"><h4>{esc(h4)}</h4><p>{esc(body)}</p></div>'


def _checklist(items) -> str:
    lis = "".join(
        f'<li><span class="check-icon"></span><span>{esc(i)}</span></li>' for i in items
    )
    return f'<ul class="checklist">{lis}</ul>'


def _table(headers, rows) -> str:
    head = "".join(f"<th>{esc(h)}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>" for row in rows
    )
    return f"<table><tr>{head}</tr>{body}</table>"


def _stats(cards) -> str:
    inner = "".join(
        f'<div class="stat-card"><div class="stat-value">{esc(v)}</div>'
        f'<div class="stat-label">{esc(label)}</div></div>'
        for v, label in cards
    )
    return f'<div class="grid-2">{inner}</div>'


_BLOCK_RENDERERS = {
    "p":         lambda b: f'<p class="text-muted">{esc(b["text"])}</p>',
    "h3":        lambda b: f'<h3>{esc(b["text"])}</h3>',
    "callout":   lambda b: _callout(b.get("title", ""), b.get("body", ""), b.get("variant", "")),
    "prompt":    lambda b: _prompt(b.get("label", ""), b.get("text", "")),
    "item":      lambda b: _item(b.get("h4", ""), b.get("body", "")),
    "checklist": lambda b: _checklist(b.get("items", [])),
    "table":     lambda b: _table(b.get("headers", []), b.get("rows", [])),
    "stats":     lambda b: _stats(b.get("cards", [])),
}


def _render_block(block) -> str:
    t = block.get("type")
    renderer = _BLOCK_RENDERERS.get(t)
    if not renderer:
        raise ValueError(f"Unknown block type: {t!r}. Valid: {sorted(_BLOCK_RENDERERS)}")
    return renderer(block)


def _render_chapter(ch) -> str:
    header = (
        '<div class="section-header">'
        f'<div class="section-num">{esc(ch.get("num", ""))}</div>'
        f'<h2>{esc(ch["title"])}</h2>'
        + (f'<p>{esc(ch["sub"])}</p>' if ch.get("sub") else "")
        + "</div>"
    )
    blocks = "\n".join(_render_block(b) for b in ch.get("blocks", []))
    return f'<div class="page page-break">\n{header}\n{blocks}\n</div>'


# ── Spec validation + assembly ──────────────────────────────────────────────
_REQUIRED = ("slug", "title", "subtitle", "eyebrow", "chapters")


def validate_spec(spec) -> list:
    """Return a list of human-readable problems; empty list means the spec is valid."""
    errs = []
    for key in _REQUIRED:
        if not spec.get(key):
            errs.append(f"missing required field: {key}")
    for i, ch in enumerate(spec.get("chapters", [])):
        if not ch.get("title"):
            errs.append(f"chapter[{i}] missing title")
        for j, b in enumerate(ch.get("blocks", [])):
            if b.get("type") not in _BLOCK_RENDERERS:
                errs.append(f"chapter[{i}].block[{j}] invalid type: {b.get('type')!r}")
    return errs


def build_html(spec) -> str:
    """Assemble a full HTML document from a product spec. Raises ValueError on invalid spec."""
    errs = validate_spec(spec)
    if errs:
        raise ValueError("Invalid product spec:\n  - " + "\n  - ".join(errs))

    intro_parts = []
    if spec.get("intro_callout"):
        ic = spec["intro_callout"]
        intro_parts.append(_callout(ic.get("title", ""), ic.get("body", ""), ic.get("variant", "")))
    if spec.get("stats"):
        intro_parts.append(_stats(spec["stats"]))
    intro_html = (
        f'<div class="page page-break">\n{chr(10).join(intro_parts)}\n</div>'
        if intro_parts else ""
    )

    chapters_html = "\n\n".join(_render_chapter(ch) for ch in spec["chapters"])

    closing_html = ""
    if spec.get("closing"):
        c = spec["closing"]
        closing_html = (
            '<div style="margin-top:64px;padding-top:32px;border-top:1px solid var(--border);'
            'text-align:center;">'
            f'<p class="text-dim" style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;'
            f'letter-spacing:0.08em;text-transform:uppercase;">{esc(c.get("line", ""))}</p>'
            f'<p style="font-size:0.9rem;color:var(--accent);margin-top:16px;font-weight:600;">'
            f'{esc(c.get("url", "schephenk.gumroad.com"))}</p></div>'
        )

    body = "\n\n".join(p for p in (intro_html, chapters_html, closing_html) if p)
    return html_doc(
        title=spec["title"],
        subtitle=spec["subtitle"],
        eyebrow=spec["eyebrow"],
        meta_items=[tuple(m) for m in spec.get("meta", [])],
        body_html=body,
    )


def render_pdf(html_path: Path, pdf_path: Path) -> bool:
    """Render HTML → PDF via headless Chrome. Returns True on success, False if Chrome is unavailable."""
    chrome = next((c for c in ("google-chrome", "chromium", "chromium-browser")
                   if subprocess.run(["which", c], capture_output=True).returncode == 0), None)
    if not chrome:
        print("  (skipping PDF — no Chrome/Chromium on PATH)")
        return False
    subprocess.run([
        chrome, "--headless", "--no-sandbox", "--disable-gpu",
        f"--print-to-pdf={pdf_path}", "--print-to-pdf-no-header", "--no-pdf-header-footer",
        f"file://{html_path}",
    ], check=True)
    return True


def build(spec, make_pdf=False) -> Path:
    """Build a product from a spec dict. Writes HTML (and optionally PDF) into downloads/pdfs/."""
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    slug = spec["slug"]
    html_path = PDF_DIR / f"{slug}.html"
    html_path.write_text(build_html(spec), encoding="utf-8")
    print(f"Wrote HTML: {html_path}")
    if make_pdf:
        pdf_path = PDF_DIR / f"{slug}.pdf"
        if render_pdf(html_path, pdf_path):
            print(f"Wrote PDF:  {pdf_path}")
    return html_path


# ── Demo spec (also used by the smoke tests) ────────────────────────────────
def build_demo_spec() -> dict:
    return {
        "slug": "_demo_product",
        "title": "Demo Product",
        "subtitle": "A minimal spec that exercises every block type in the builder.",
        "eyebrow": "Schep Digital · Builder Self-Test",
        "meta": [["Format", "PDF"], ["Pages", "2"], ["Compatibility", "Any reader"]],
        "intro_callout": {"title": "Why this exists", "body": "Proves the engine renders.",
                          "variant": "green"},
        "stats": [["100%", "Coverage"], ["8", "Block types"], ["1", "Engine"], ["0", "Bespoke scripts"]],
        "chapters": [
            {"num": "Chapter 01", "title": "Every Block", "sub": "One of each.",
             "blocks": [
                 {"type": "p", "text": "A paragraph of body copy with an & ampersand and <tag>."},
                 {"type": "h3", "text": "A subheading"},
                 {"type": "callout", "title": "Note", "body": "A callout.", "variant": "amber"},
                 {"type": "prompt", "label": "Example prompt", "text": "Role: editor\nTask: tighten copy"},
                 {"type": "item", "h4": "An item", "body": "With a description."},
                 {"type": "checklist", "items": ["First check", "Second check"]},
                 {"type": "table", "headers": ["Key", "Value"], "rows": [["a", "1"], ["b", "2"]]},
             ]},
        ],
        "closing": {"line": "Demo Product — Schep Digital", "url": "schephenk.gumroad.com"},
    }


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    make_pdf = "--pdf" in argv
    if "--demo" in argv:
        spec = build_demo_spec()
        Path(PDF_DIR).mkdir(parents=True, exist_ok=True)
        (PDF_DIR / "_demo_product.spec.json").write_text(json.dumps(spec, indent=2))
        build(spec, make_pdf=make_pdf)
        return 0
    spec_path = next((a for a in argv if not a.startswith("-")), None)
    if not spec_path:
        print("Provide a spec JSON path, or --demo. See --help.")
        return 1
    spec = json.loads(Path(spec_path).read_text())
    build(spec, make_pdf=make_pdf)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
