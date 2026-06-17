#!/usr/bin/env bash
# DELETE /v2/resource_subscriptions/:id — Delete a webhook subscription
# Usage: ./delete-resource-subscription.sh SUBSCRIPTION_ID
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"

SUB_ID="${1:?Usage: delete-resource-subscription.sh SUBSCRIPTION_ID}"
gumroad_delete "resource_subscriptions/$SUB_ID" | jq .
