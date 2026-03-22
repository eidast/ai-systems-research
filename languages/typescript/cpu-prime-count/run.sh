#!/usr/bin/env bash
set -euo pipefail
UPPER_BOUND="${1:-100000}"
node "$(dirname "$0")/prime_count.mjs" "$UPPER_BOUND"
