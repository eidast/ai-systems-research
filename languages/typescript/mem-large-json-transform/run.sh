#!/usr/bin/env bash
set -euo pipefail
DATASET="${1:?dataset path required}"
node "$(dirname "$0")/transform.mjs" "$DATASET"
