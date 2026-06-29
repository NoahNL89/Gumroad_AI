#!/usr/bin/env bash
# List webhooks for one Gumroad resource.
# Usage: ./list-resource-subscriptions.sh <resource_name>
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[ -f "$DIR/../../.env" ] && source "$DIR/../../.env"
source "$DIR/_base.sh"
RESOURCE="${1:?Provide resource_name (e.g. sale)}"
gumroad_cli webhooks list --resource "$RESOURCE" | jq .
