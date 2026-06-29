#!/usr/bin/env bash
# PUT /v2/resource_subscriptions — Create a webhook
# Usage: ./create-resource-subscription.sh <resource_name> <post_url>
# resource_name: sale | refund | dispute | dispute_won | cancellation |
#                subscription_updated | subscription_ended | subscription_restarted
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"
RESOURCE="${1:?Provide resource_name (e.g. sale)}"
URL="${2:?Provide post_url}"
gumroad_cli webhooks create --resource "$RESOURCE" --url "$URL" | jq .
