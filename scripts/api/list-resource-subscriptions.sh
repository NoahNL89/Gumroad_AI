#!/usr/bin/env bash
# GET /v2/resource_subscriptions — List all webhooks
# Usage: ./list-resource-subscriptions.sh
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"
gumroad_get "resource_subscriptions" | jq .
