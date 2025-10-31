# TalkBox – Offline, Low-Latency Speech I/O Plug-in

A pocket-sized TTS + STT engine with a slider GUI and a socket API, designed to drop straight into any open-source LLM front-end (text-generation-webui, KoboldCpp, LM-Studio, etc.).  A low Latency local TTS + STT easy to build EXE can easy use with LLM programs without the hassle of other ways to get TTS + STT intergraded for an AI assistant.

---

## Features
- **100 % local** – no cloud, no telemetry, no tokens leave your machine  
- **&lt; 200 ms round-trip** mouth-to-ear on CPU or Apple-Silicon  
- **GUI controls** – voice, pitch (±12 st), speed (0.5×-2×), tone (formant)  
- **Triple input** – type, push-to-talk STT, ZeroMQ / REST socket  
- **Dual output** – instant audio + optional phoneme-timing stream for lip-sync  
- **Single-file binary** – `pip install` once, or run the ready-made EXE / AppImage  

---

## Quick Start
```bash
git clone https://github.com/Cannibal13/talkbox.git
cd talkbox
pip install -r requirements.txt   # 30 s, models auto-download
python talkbox.py                 # GUI appears; start talking
