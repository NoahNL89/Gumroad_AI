#!/usr/bin/env bash
# auth-check.sh — Quick Gumroad auth status check
# Usage: ./scripts/auth-check.sh

set -euo pipefail

echo "=== Gumroad Auth Check ==="
echo ""

if ! gumroad auth status --json --no-input 2>/dev/null | jq -e '.seller' > /dev/null 2>&1; then
  echo "❌ Not authenticated."
  echo ""
  echo "To authenticate:"
  echo "  gumroad auth login              # Interactive device flow"
  echo "  export GUMROAD_ACCESS_TOKEN=xxx # CI/Agent mode"
  exit 1
fi

echo "✅ Authenticated. Account info:"
echo ""
gumroad user --json --no-input | jq '{
  name: .user.name,
  email: .user.email,
  url: .user.profile_url
}'
