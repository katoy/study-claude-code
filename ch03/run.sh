#!/usr/bin/env bash
set -euo pipefail

# ch03/run.sh - Run multiply.py using uv

cd "$(dirname "$0")"

# Ensure dependencies are synced
uv sync --quiet

# Run multiply.py
uv run python multiply.py "$@"

