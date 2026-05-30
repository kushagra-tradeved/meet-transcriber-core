import os

def ensure_directories():
    """Ensures input workspace targets exist cleanly."""
    from config import RECORDINGS_DIR
    if not os.path.exists(RECORDINGS_DIR):
        os.makedirs(RECORDINGS_DIR)
        print(f"📁 Created input folder directory at: {RECORDINGS_DIR}")

def validate_audio_file(file_path: str) -> bool:
    """Verifies format compatibility before spinning up heavy neural weights."""
    valid_extensions = ('.mp3', '.wav', '.m4a', '.mp4', '.webm', '.mkv')
    return file_path.lower().endswith(valid_extensions) and os.path.exists(file_path)