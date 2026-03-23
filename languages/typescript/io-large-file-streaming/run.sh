#!/usr/bin/env bash
set -euo pipefail
node "$(dirname "$0")/stream.mjs" "${1:?dataset path required}"
