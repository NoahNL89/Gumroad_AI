#!/usr/bin/env bash
# Shared helper for legacy script entry points backed by the Gumroad CLI.
# Source this file: source scripts/api/_base.sh

gumroad_cli() {
  command gumroad "$@" --json --no-input --no-color
}
