#!/usr/bin/env bash
# GET /v2/products — List all products
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"
gumroad_cli products list | jq .
