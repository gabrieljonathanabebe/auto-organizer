#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
printf "Project directory: %s\n" "$PROJECT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  printf "Error: Python 3 is required.\n" >&2
  exit 1
fi

VENV_DIR="$PROJECT_DIR/.venv"

if [[ ! -d "$VENV_DIR" ]]; then
  printf "Creating virtual environment...\n"
  python3 -m venv "$VENV_DIR"
else
  printf "Virtual environment already exists.\n"
fi

VENV_PYTHON="$VENV_DIR/bin/python"

printf "Installing runtime dependencies...\n"
"$VENV_PYTHON" -m pip install -r "$PROJECT_DIR/requirements.txt"