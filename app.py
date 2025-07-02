"""
app.py

Entry point for the Kokoro TTS Generator application.
Initializes and runs the GUI.

Usage:
    python app.py

The main steps performed are:
    1. Configure logging.
    2. Ensure output and temporary directories exist.
    3. Launch the GUI application.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)
logger.info("Starting Kokoro TTS Generator.")


from src.gui import App

if __name__ in {"__main__", "__mp_main__"}:
    # Ensure directories exist
    import os
    os.makedirs('final_audio', exist_ok=True)
    os.makedirs('temp', exist_ok=True)

    logger.info("Ensured required directories exist.")

    # Launch the main GUI application
    logger.info("Launching Kokoro TTS Generator GUI application.")
    App()
