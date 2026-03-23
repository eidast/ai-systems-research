#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
dotnet run --project "$DIR/ParallelReduction.csproj" -- "${1:-200000}"
