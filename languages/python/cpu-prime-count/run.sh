#!/usr/bin/env bash
set -euo pipefail
UPPER_BOUND="${1:-100000}"
python3 "$(dirname "$0")/prime_count.py" "$UPPER_BOUND"
