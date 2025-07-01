import os
import shutil
import soundfile as sf
import numpy as np
import uuid

class Pipeline:
    def __init__(self):
        self.pipeline = None

    def load(self):
        from kokoro import KPipeline
        self.pipeline = KPipeline(lang_code='a')

    def generate(self, text, voice, speed, pitch):
        temp_dir = 'temp'
        final_dir = 'final_audio'

        # Clean and recreate temp directory
        if os.path.isdir(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)

        # Ensure final_audio directory exists
        os.makedirs(final_dir, exist_ok=True)

        # Generate a unique filename for each output to avoid browser caching issues
        unique_id = uuid.uuid4().hex
        out_path = os.path.join(final_dir, f'output_{unique_id}.wav')

        # Generate audio chunks using the pipeline
        if self.pipeline is None:
            raise RuntimeError("Pipeline not loaded. Call load() before generate().")

        generator = self.pipeline(
            text, voice=voice,
            speed=speed, split_pattern=r'\n+'
        )

        chunk_files = []
        for i, (_, _, data) in enumerate(generator):
            chunk_path = os.path.join(temp_dir, f'{i}.wav')
            sf.write(chunk_path, data, 24000)
            chunk_files.append(chunk_path)

        if not chunk_files:
            return None

        # Read and concatenate all chunk audio data
        audio_datas = []
        for fname in chunk_files:
            data, _ = sf.read(fname)
            audio_datas.append(data)
        combined = np.concatenate(audio_datas)


        if combined.ndim > 1:
            combined = combined.mean(axis=1)
        combined = combined.astype(np.float32)

        print(f"DEBUG: Writing WAV {out_path}, shape={combined.shape}, dtype={combined.dtype}, min={combined.min()}, max={combined.max()}")
        sf.write(out_path, combined, 24000)

        return out_path
