#!/usr/bin/env bash
# Base helpers for direct Gumroad API calls
# Source this file: source scripts/api/_base.sh

GUMROAD_API_BASE="https://api.gumroad.com/v2"

: "${GUMROAD_ACCESS_TOKEN:?GUMROAD_ACCESS_TOKEN not set. Run: source .env}"

gumroad_get() {
  local endpoint="$1"
  shift
  curl -s -G "$GUMROAD_API_BASE/$endpoint" \
    --data-urlencode "access_token=$GUMROAD_ACCESS_TOKEN" \
    "$@"
}

gumroad_post() {
  local endpoint="$1"
  shift
  curl -s -X POST "$GUMROAD_API_BASE/$endpoint" \
    --data-urlencode "access_token=$GUMROAD_ACCESS_TOKEN" \
    "$@"
}

gumroad_put() {
  local endpoint="$1"
  shift
  curl -s -X PUT "$GUMROAD_API_BASE/$endpoint" \
    --data-urlencode "access_token=$GUMROAD_ACCESS_TOKEN" \
    "$@"
}

gumroad_delete() {
  local endpoint="$1"
  shift
  curl -s -X DELETE "$GUMROAD_API_BASE/$endpoint" \
    --data-urlencode "access_token=$GUMROAD_ACCESS_TOKEN" \
    "$@"
}
