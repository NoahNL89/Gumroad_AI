#!/usr/bin/env bash
# GET /v2/resource_subscriptions — List all webhooks
# Usage: ./list-resource-subscriptions.sh
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIR/_base.sh"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
gumroad_get "resource_subscriptions" | jq .
