#!/usr/bin/env bash
# GET /v2/user — Get current user info
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIR/_base.sh"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
gumroad_get "user" | jq .
