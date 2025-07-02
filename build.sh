#!/bin/bash
set -e

# Check for cmake
if ! command -v cmake &> /dev/null; then
  echo "Error: cmake is not installed. Please install it (e.g., sudo apt install cmake) and try again."
  exit 1
fi

# Build script for KokoroTTSGenerator using uv and pyinstaller

# Ensure we're in the script's directory
cd "$(dirname "$0")"

# Clean previous build artifacts
rm -rf build dist KokoroTTSGenerator.spec

# Build UPX from source if not already built
if [ ! -f external/upx/src/upx ]; then
  echo "Building UPX from source..."
  if [ ! -d external/upx ]; then
    git clone https://github.com/upx/upx.git external/upx
  fi
  cd external/upx
  git submodule update --init
  make all
  cd ../../
else
  echo "UPX already built, skipping build."
fi

# Run PyInstaller with the required options using uv, using the built UPX
uv run pyinstaller app.py \
  -n KokoroTTSGenerator \
  --noconfirm \
  --add-data "src:src" \
  --add-data ".venv/lib/python3.12/site-packages/nicegui:nicegui" \
  --add-data ".venv/lib/python3.12/site-packages/language_data:language_data" \
  --add-data ".venv/lib/python3.12/site-packages/language_tags:language_tags" \
  --upx-dir=external/upx/src

echo "Build complete. Executable is in the dist/ directory."
