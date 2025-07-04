import os
import shutil
import soundfile as sf
import numpy as np
import uuid
import logging
import torch

# Set up logging for this module
logger = logging.getLogger(__name__)

class Pipeline:
    """
    Pipeline class for managing the Kokoro TTS (Text-to-Speech) generation process.
    Handles loading the TTS model and generating audio from text input.
    """

    def __init__(self):
        """
        Initialize the Pipeline object.
        The actual TTS pipeline is loaded separately via the load() method.
        """
        self.pipeline = None

    def load(self):
        """
        Load the Kokoro TTS pipeline.
        This should be called before attempting to generate audio.
        """
        logger.info("Loading TTS pipeline...")
        from kokoro import KPipeline
        self.pipeline = KPipeline(lang_code='a')
        logger.info("TTS pipeline loaded.")

    def generate(self, text, voice, speed, pitch):
        """
        Generate speech audio from the given text using the loaded TTS pipeline.

        Args:
            text (str): The input text to synthesize.
            voice (str): The voice preset or identifier to use.
            speed (float): The speed multiplier for speech.
            pitch (float): The pitch adjustment for speech. (No use yet)

        Returns:
            str: The path to the generated WAV audio file, or None if generation failed.

        Raises:
            RuntimeError: If the pipeline has not been loaded before calling this method.
        """
        logger.info(
            f"Generating audio: text='{text[:30]}...', voice={voice}, speed={speed}, pitch={pitch}"
        )
        temp_dir = 'temp'
        final_dir = 'final_audio'

        # Clean and recreate temp directory
        if os.path.isdir(temp_dir):
            logger.debug(f"Removing existing temp directory: {temp_dir}")
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)
        logger.debug(f"Created temp directory: {temp_dir}")

        # Ensure final_audio directory exists
        os.makedirs(final_dir, exist_ok=True)
        logger.debug(f"Ensured final audio directory exists: {final_dir}")

        # Generate a unique filename for each output to avoid browser caching issues
        unique_id = uuid.uuid4().hex
        out_path = os.path.join(final_dir, f'output_{unique_id}.wav')

        # Generate audio chunks using the pipeline
        if self.pipeline is None:
            logger.error("Pipeline not loaded. Call load() before generate().")
            raise RuntimeError("Pipeline not loaded. Call load() before generate().")

        generator = self.pipeline(
            text, voice=voice,
            speed=speed, split_pattern=r'\n+'
        )

        chunk_files = []
        for i, (_, _, data) in enumerate(generator):
            chunk_path = os.path.join(temp_dir, f'{i}.wav')
            sf.write(chunk_path, data, 24000)
            logger.debug(f"Wrote chunk {i} to {chunk_path} (shape={data.shape})")
            chunk_files.append(chunk_path)

        if not chunk_files:
            logger.warning("No audio chunks were generated.")
            return None

        # Read and concatenate all chunk audio data
        audio_datas = []
        for fname in chunk_files:
            data, _ = sf.read(fname)
            audio_datas.append(data)
            logger.debug(f"Read chunk file {fname} (shape={data.shape})")
        combined = np.concatenate(audio_datas)

        # If stereo or multi-channel, convert to mono
        if combined.ndim > 1:
            logger.debug("Converting multi-channel audio to mono.")
            combined = combined.mean(axis=1)
        combined = combined.astype(np.float32)

        logger.info(
            f"Writing final WAV {out_path}, shape={combined.shape}, dtype={combined.dtype}, min={combined.min()}, max={combined.max()}"
        )
        sf.write(out_path, combined, 24000)

        logger.info(f"Audio generation complete: {out_path}")
        return out_path
