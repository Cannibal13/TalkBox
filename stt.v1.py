import faster_whisper as whisper, sounddevice as sd, numpy as np, os
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models", "stt")
os.makedirs(MODEL_DIR, exist_ok=True)
model = whisper.load_model("tiny", download_root=MODEL_DIR)

def stt_listen(seconds: float = 3, sr: int = 16000):
    print("[STT]  listening…")
    audio = sd.rec(int(seconds * sr), samplerate=sr, channels=1, dtype="float32")
    sd.wait()
    result = model.transcribe(audio.flatten(), language="en", fp16=False)
    return result["text"].strip()