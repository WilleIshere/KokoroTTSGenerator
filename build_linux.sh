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

# Limit PyInstaller memory usage
export PYINSTALLER_MAX_CONSECUTIVE=1

# Run PyInstaller with UPX for compression and --strip for smaller binaries
uv run pyinstaller app.py \
  -n KokoroTTSGenerator \
  --noconfirm \
  --clean \
  --strip \
  --collect-all "en_core_web_sm" \
  --add-data "src:src" \
  --add-data ".venv/lib/python3.12/site-packages/nicegui:nicegui" \
  --add-data ".venv/lib/python3.12/site-packages/language_data:language_data" \
  --add-data ".venv/lib/python3.12/site-packages/language_tags:language_tags" \
  --add-data ".venv/lib/python3.12/site-packages/espeakng_loader:espeakng_loader" \
  --add-data ".venv/lib/python3.12/site-packages/espeakng_loader-0.2.4.dist-info:espeakng_loader-0.2.4.dist-info" \
  --add-data ".venv/lib/python3.12/site-packages/misaki:misaki" \
  --icon=icon.ico \
  --upx-dir=external/upx/src

echo "Build complete. Executable is in the dist/ directory."
