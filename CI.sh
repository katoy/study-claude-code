#!/usr/bin/env bash
set -euo pipefail

# CI.sh - Run complete CI pipeline using uv

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR/ch03"

echo "=== GitHub Copilot Study - CI Pipeline ==="
echo

# Sync dependencies (includes dev dependencies)
echo "📦 Syncing dependencies with uv..."
uv sync --quiet

# Linting
echo "🔍 Running linter (ruff)..."
uv run ruff check .

# Type checking
echo "🔍 Running type checker (mypy)..."
uv run mypy .

# Tests
echo "🧪 Running tests with coverage..."
uv run pytest --cov=multiply --cov-report=term-missing --cov-fail-under=100

echo
echo "✅ All checks passed!"

