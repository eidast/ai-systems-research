#!/usr/bin/env bash
set -euo pipefail
node "$(dirname "$0")/pipeline.mjs" "${1:-100000}"
