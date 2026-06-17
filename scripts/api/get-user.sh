#!/usr/bin/env bash
# GET /v2/user — Get current user info
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"
gumroad_get "user" | jq .
