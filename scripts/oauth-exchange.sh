#!/usr/bin/env bash
# oauth-exchange.sh — Exchange OAuth authorization code for access token
# Usage: ./scripts/oauth-exchange.sh "http://localhost:3003/endpoint?code=XXXX"
# Or:    ./scripts/oauth-exchange.sh "XXXX"  (just the code itself)

set -euo pipefail

INPUT="${1:?Provide the full redirect URL or just the auth code}"
ENV_FILE="$(dirname "$0")/../.env"

# Extract code from full URL or use as-is
if [[ "$INPUT" == http* ]]; then
  CODE=$(echo "$INPUT" | grep -oP '(?<=code=)[^&]+')
else
  CODE="$INPUT"
fi

echo "=== Gumroad OAuth Token Exchange ==="
echo "Code: ${CODE:0:12}..."
echo ""

CLIENT_ID="${GUMROAD_CLIENT_ID:-lrTDL-2m1VyDQt9clyMOeZ5NuyjBrB3a9TW_t0OAiOE}"
CLIENT_SECRET="${GUMROAD_CLIENT_SECRET:-KlPgzjxVAuiiq33JyCo4b_tuTKLdyFnoZ4XaHBDr9KM}"
REDIRECT_URI="${GUMROAD_REDIRECT_URI:-http://localhost:3003/endpoint}"

RESPONSE=$(curl -s -X POST "https://api.gumroad.com/oauth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "code=$CODE" \
  --data-urlencode "client_id=$CLIENT_ID" \
  --data-urlencode "client_secret=$CLIENT_SECRET" \
  --data-urlencode "redirect_uri=$REDIRECT_URI" \
  --data-urlencode "grant_type=authorization_code")

echo "Response: $RESPONSE"
echo ""

# Extract token
ACCESS_TOKEN=$(echo "$RESPONSE" | jq -r '.access_token // empty')

if [[ -z "$ACCESS_TOKEN" ]]; then
  echo "❌ Failed to get access token."
  echo "Raw response: $RESPONSE"
  exit 1
fi

echo "✅ Got access token: ${ACCESS_TOKEN:0:16}..."
echo ""

# Update .env file
if [[ -f "$ENV_FILE" ]]; then
  if grep -q "^GUMROAD_ACCESS_TOKEN=" "$ENV_FILE"; then
    sed -i "s|^GUMROAD_ACCESS_TOKEN=.*|GUMROAD_ACCESS_TOKEN=$ACCESS_TOKEN|" "$ENV_FILE"
  else
    echo "GUMROAD_ACCESS_TOKEN=$ACCESS_TOKEN" >> "$ENV_FILE"
  fi
  echo "✅ Saved to $ENV_FILE"
fi

echo ""
echo "To use immediately in this shell:"
echo "  export GUMROAD_ACCESS_TOKEN=$ACCESS_TOKEN"
echo ""
echo "Verify with:"
echo "  gumroad auth status --json --no-input"
