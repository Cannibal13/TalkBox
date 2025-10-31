import os, numpy as np, TTS.api, sounddevice as sd
from TTS.api import TTS          # ← add this import
model = TTS("tts_models/en/ljspeech/tacotron2-DDC", gpu=False).to("cpu")
os.makedirs(MODEL_DIR, exist_ok=True)
model = TTS("tts_models/en/ljspeech/tacotron2-DDC", gpu=False).to("cpu")
vocoder = None

def load_vocoder():
    global vocoder
    vocoder = TTS("vocoder_models/en/ljspeech/hifigan_v2", gpu=False).to("cpu")

def tts(text: str, voice: str = "emma", pitch: int = 0, speed: float = 1.0, tone: float = 0.0):
    wav = model.tts(text)
    wav = np.array(wav, dtype=np.float32)
    # quick speed change (resample)
    if speed != 1.0:
        wav = np.interp(np.arange(0, len(wav), speed), np.arange(len(wav)), wav)
    wav = np.clip(wav, -1.0, 1.0)
    return (wav * 32767).astype(np.int16)