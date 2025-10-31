import os, sounddevice as sd, numpy as np
from faster_whisper import WhisperModel      #  <-- new import

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models", "stt")
os.makedirs(MODEL_DIR, exist_ok=True)

# tiny.en ≈ 39 MB, fastest load
model = WhisperModel("tiny", device="cpu", compute_type="int8", download_root=MODEL_DIR)

def stt_listen(seconds=3, sr=16000):
    print("[STT]  listening…")
    audio = sd.rec(int(seconds * sr), samplerate=sr, channels=1, dtype="float32")
    sd.wait()
    # faster-whisper returns an iterator → grab first sentence
    segments, _ = model.transcribe(audio.flatten(), language="en", word_timestamps=False)
    text = " ".join(s.text for s in segments).strip()
    return text