import os, numpy as np, sounddevice as sd
from TTS.api import TTS

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models", "tts")
os.makedirs(MODEL_DIR, exist_ok=True)

model = TTS("tts_models/en/ljspeech/tacotron2-DDC", gpu=False).to("cpu")
vocoder = None

def load_vocoder():
    global vocoder
#    from TTS.utils.synthesizer import Synthesizer          # low-level loader
#    vocoder = Synthesizer(
#        tts_config_path=None,
#        vocoder_checkpoint="vocoder_models/en/ljspeech/hifigan_v2/model.pth",
#        vocoder_config="vocoder_models/en/ljspeech/hifigan_v2/config.json",
#        use_cuda=False
#    )
    pass

def tts(text: str, voice="emma", pitch=0, speed=1.0, tone=0.0):
    text = text.strip()
    if not text:                                        # empty → 0.1 s silence
        return np.zeros(int(0.1 * 22050), dtype=np.int16)

    wav = model.tts(text)
    wav = np.array(wav, dtype=np.float32)
    if speed != 1.0:
        wav = np.interp(np.arange(0, len(wav), speed), np.arange(len(wav)), wav)
    wav = np.clip(wav, -1.0, 1.0)
    return (wav * 32767).astype(np.int16)