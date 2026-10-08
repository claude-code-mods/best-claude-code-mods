#!/usr/bin/env bash
# Rebuilds the catalogue and validates the marketplace file.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/build-catalog.py
claude plugin validate .
