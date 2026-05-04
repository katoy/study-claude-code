#!/usr/bin/env bash
set -euo pipefail

# ch03/run.sh - Run multiply.py with arguments

if [ ! -d ".venv" ]; then
  echo "Setting up virtual environment..."
  python -m venv .venv
  source .venv/bin/activate
  pip install -e .
else
  source .venv/bin/activate
fi

python multiply.py "$@"
