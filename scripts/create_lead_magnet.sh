#!/bin/bash
# create_lead_magnet.sh — build + publish the FREE lead magnet that captures emails.
#
# This is the top of the funnel: a free product collects buyer emails we can market
# to forever (see agent/EMAIL_FLOW.md). Run it ONCE; re-running creates a duplicate.
#
#   bash scripts/create_lead_magnet.sh            # build PDF + create + publish
#   bash scripts/create_lead_magnet.sh --build-only   # just build the PDF, no Gumroad calls
#
# Publishing a public product is outward-facing — this script is NOT run automatically.
set -euo pipefail
cd "$(dirname "$0")/.."

SLUG="free-ai-quickstart"
SPEC="agent/specs/${SLUG}.spec.json"
NAME="The AI Quick-Start Pack (Free)"
DESC="12 copy-paste AI prompts and a one-page system that make AI useful in your day. Free starter from Schep Digital — upgrade anytime with code LAUNCH30 for 30% off the full kits."

echo "==> Building PDF from spec via the data-driven engine"
python3 scripts/product_builder.py "$SPEC" --pdf
HTML="downloads/pdfs/${SLUG}.html"
PDF="downloads/pdfs/${SLUG}.pdf"
[ -f "$HTML" ] || { echo "ERROR: HTML not generated"; exit 1; }

if [ "${1:-}" = "--build-only" ]; then
  echo "Built $HTML (and $PDF if Chrome was available). Skipping Gumroad (--build-only)."
  exit 0
fi
[ -f "$PDF" ] || { echo "ERROR: PDF not generated (need Chrome/Chromium on PATH). Aborting publish."; exit 1; }

[ -f .env ] && source .env
command -v gumroad >/dev/null || { echo "ERROR: gumroad CLI not found on PATH"; exit 1; }

echo "==> Creating FREE product on Gumroad"
RESP=$(gumroad products create --name "$NAME" --price 0 --currency eur --description "$DESC" --json --no-input)
echo "$RESP"
ID=$(printf '%s' "$RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('product',{}).get('id') or d.get('id',''))")
[ -n "$ID" ] || { echo "ERROR: could not parse product id from response"; exit 1; }

echo "==> Attaching PDF and publishing (id: $ID)"
gumroad products update "$ID" --file "$PDF" --file-name "AI Quick-Start Pack (Schep Digital).pdf" --json --no-input --yes
gumroad products publish "$ID" --json --no-input

echo ""
echo "✅ Lead magnet live (id: $ID)."
echo "   Next:"
echo "   1) Promote it everywhere (free converts far better than paid) — python3 scripts/launch_kit.py \"$NAME\""
echo "   2) Run the nurture sequence in agent/EMAIL_FLOW.md against new signups."
echo "   3) python3 db/sync.py  to pull it into the local DB."
