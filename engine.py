import time
from faster_whisper import WhisperModel
import config

class ProductionTranscriber:
    def __init__(self):
        print(f"🔄 Loading {config.MODEL_SIZE} weights onto processing target ({config.DEVICE})...")
        self.model = WhisperModel(
            model_size_or_path=config.MODEL_SIZE,
            device=config.DEVICE,
            compute_type=config.COMPUTE_TYPE
        )
        print("💡 Model weights successfully locked into active memory.")

    def process_file(self, file_path: str):
        """Executes full mathematical audio extraction."""
        print(f"🎙️ Deep analysis started on file: {file_path}")
        start_time = time.time()

        # Execute transcription with high-accuracy parameters
        segments, info = self.model.transcribe(
            file_path,
            beam_size=config.BEAM_SIZE,
            temperature=config.TEMPERATURE_FALLBACK,
            word_timestamps=True  # Vital tracking metric for future diarization alignment
        )

        print(f"🌍 Primary Detected Language: {info.language} ({info.language_probability:.2%})")
        
        compiled_segments = []
        for segment in segments:
            chunk = {
                "start": round(segment.start, 2),
                "end": round(segment.end, 2),
                "text": segment.text.strip()
            }
            # Visual feedback during terminal processing execution
            print(f"[{chunk['start']}s -> {chunk['end']}s]: {chunk['text']}")
            compiled_segments.append(chunk)

        elapsed = time.time() - start_time
        print(f"✅ Finished core processing in {elapsed:.2f} seconds.")
        return compiled_segments