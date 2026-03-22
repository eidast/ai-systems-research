#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
dotnet run --project "$DIR/MemLargeJsonTransform.csproj" -- "${1:?dataset path required}"
