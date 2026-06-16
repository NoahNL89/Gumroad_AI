#!/usr/bin/env bash
# PUT /v2/resource_subscriptions — Create a webhook
# Usage: ./create-resource-subscription.sh <resource_name> <post_url>
# resource_name: sale | refund | dispute | dispute_won | cancellation |
#                subscription_updated | subscription_ended | subscription_restarted
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIR/_base.sh"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
RESOURCE="${1:?Provide resource_name (e.g. sale)}"
URL="${2:?Provide post_url}"
gumroad_put "resource_subscriptions" \
  --data-urlencode "resource_name=$RESOURCE" \
  --data-urlencode "post_url=$URL" | jq .
