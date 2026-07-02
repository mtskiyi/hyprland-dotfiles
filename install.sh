#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is not installed."
  echo "Install it with: sudo pacman -S python"
  exit 1
fi

python3 installer.py
