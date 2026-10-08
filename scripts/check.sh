#!/usr/bin/env bash
# Validates the marketplace file and every mod in it, then runs each mod's tests.
set -euo pipefail
cd "$(dirname "$0")/.."

claude plugin validate .
for dir in */; do
  dir="${dir%/}"
  [[ -f "$dir/.claude-plugin/plugin.json" ]] || continue
  echo "== $dir"
  claude plugin validate "$dir"
  if compgen -G "$dir/tests/*.test.ts*" > /dev/null; then
    claude plugin test "$dir"
  fi
done
