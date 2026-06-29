#!/usr/bin/env bash
# Compatibility entry point: authenticate through the Gumroad CLI.
# The old direct OAuth code exchange has been intentionally removed.

set -euo pipefail

if [[ $# -gt 0 ]]; then
  echo "This script no longer accepts OAuth codes or redirect URLs." >&2
  echo "Starting the Gumroad CLI authentication flow instead." >&2
fi

exec gumroad auth login
