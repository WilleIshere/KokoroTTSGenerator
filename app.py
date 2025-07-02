"""
app.py

Entry point for the Kokoro TTS Generator application.
Initializes and runs the GUI.
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
    App()
