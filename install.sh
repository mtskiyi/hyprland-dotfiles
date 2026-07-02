#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v pacman >/dev/null 2>&1; then
  echo "Error: this installer is made for Arch Linux / pacman."
  exit 1
fi

if ! command -v sudo >/dev/null 2>&1; then
  echo "Error: sudo is not installed."
  echo "Install sudo first or run on a proper Arch setup."
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo ":: python3 not found. Installing Python..."
  sudo pacman -Syu --needed python
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 still not found after installing python."
  exit 1
fi

echo ":: Checking Python modules..."

python3 - <<'PY'
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

print(":: Python modules OK.")
PY

chmod +x installer.py

echo ":: Starting installer..."
python3 installer.py
