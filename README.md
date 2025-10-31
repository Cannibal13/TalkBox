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

## Troubleshooting `pip install`
If you see  
`ERROR: No matching distribution found for dearpygui==1.9.6`  
just edit `requirements.txt` and replace the pinned version with  

dearpygui>=1.9

(or run `pip install dearpygui>=1.9` manually).  
PyPI does not host the fictional `1.9.6` build; `>=1.9` pulls the latest stable wheel (tested up to 1.11.1).

(Optional) quick one-liner for copy-pasters
```bash
# fast fix without editing the file
pip install dearpygui>=1.9 TTS>=0.22 faster-whisper>=0.10 sounddevice pyzmq flask
