#!/usr/bin/env bash
set -euo pipefail
node "$(dirname "$0")/parallel_reduction.mjs" "${1:-200000}"
