# KokoroTTSGenerator

KokoroTTSGenerator is a Python 3.12+ project for generating text-to-speech (TTS) audio. It is set up to use [uv](https://github.com/astral-sh/uv) as the package and virtual environment manager for fast, reliable dependency management.

## Features

- Python 3.12+ support
- Fast dependency management with uv
- Linting with [ruff](https://github.com/astral-sh/ruff)
- Formatting with [black](https://github.com/psf/black)
- Testing with [pytest](https://docs.pytest.org/)
- Simple entry point: `app.py`

## Getting Started

### 1. Install uv

If you don't have uv installed, follow the instructions at [uv installation](https://github.com/astral-sh/uv#installation).

### 2. Create a virtual environment

```bash
uv venv
```

### 3. Activate the virtual environment

On Linux/macOS:
```bash
source .venv/bin/activate
```

On Windows:
```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt  # If you have a requirements.txt
# or, for pyproject.toml-based projects:
uv pip install .
```

Or, to install development dependencies:
```bash
uv pip install .[dev]
```

### 5. Run the project

```bash
python app.py
```

Or use the provided shortcut script:
```bash
bash run.sh
```

## Project Structure

```
KokoroTTSGenerator/
├── app.py          # Main entry point
├── pyproject.toml  # Project metadata and dependencies
├── run.sh          # Shortcut to run the project
├── README.md       # This file
└── .venv/          # Virtual environment (created by uv)
```

## Development

- **Lint:** `ruff .`
- **Format:** `black .`
- **Test:** `pytest`

## License

MIT License. See [LICENSE](LICENSE) for details.

---
Feel free to customize this project structure and documentation to fit your needs!