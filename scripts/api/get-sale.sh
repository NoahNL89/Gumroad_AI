#!/usr/bin/env bash
# GET /v2/sales/:id — Get a single sale by ID
# Usage: ./get-sale.sh SALE_ID
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"

SALE_ID="${1:?Usage: get-sale.sh SALE_ID}"
gumroad_cli sales view "$SALE_ID" | jq .
