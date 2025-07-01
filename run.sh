KokoroTTSGenerator/run.sh
#!/bin/bash
# Run KokoroTTSGenerator using the project's virtual environment

VENV_DIR=".venv"
PYTHON_BIN="$VENV_DIR/bin/python"

if [ ! -d "$VENV_DIR" ]; then
  echo "Virtual environment not found. Please run 'uv venv' or create the venv first."
  exit 1
fi

if [ ! -f "$PYTHON_BIN" ]; then
  echo "Python binary not found in venv. Something went wrong with the venv setup."
  exit 1
fi

exec "$PYTHON_BIN" -m kokoro_tts_generator "$@"
