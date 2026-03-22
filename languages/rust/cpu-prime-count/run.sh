#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
cargo run --quiet --manifest-path "$DIR/Cargo.toml" -- "${1:-100000}"
