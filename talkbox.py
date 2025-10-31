#!/usr/bin/env python3
import dearpygui.dearpygui as dpg, numpy as np, threading, queue, sounddevice as sd, zmq, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from tts import tts, load_vocoder
from stt import stt_listen

TEXT_IN   = queue.Queue()
AUDIO_OUT = queue.Queue()   # will hold *numpy* arrays
load_vocoder()

def speak(sender, text: str):
    text = text.strip()
    if not text:
        return
    wav = tts(text, voice=dpg.get_value("voice"),
          pitch=dpg.get_value("pitch"),
          speed=dpg.get_value("speed"),
          tone=dpg.get_value("tone"),
          volume=dpg.get_value("volume"))   # <-- add this
    AUDIO_OUT.put(wav)          # <-- array, not bytes

def stt_thread():
    while True:
        text = stt_listen()
        if not text or not text.strip():        # ← ignore silence / empties
            continue
        dpg.set_value("type_box", text)
        speak(None, text)

def socket_thread(port=5555):
    z = zmq.Context().socket(zmq.REP)
    z.bind(f"tcp://*:{port}")
    while True:
        text = z.recv_string()
        z.send_string("ok")
        speak(None, text)

def audio_consumer():
    while True:
        if not AUDIO_OUT.empty():
            sd.play(AUDIO_OUT.get(), samplerate=22050)
        sd.sleep(50)

dpg.create_context()
with dpg.window(tag="main", label="TalkBox",
                width=420,   
                height=320):
    # your existing widgets stay here
    dpg.add_text("Input:")
    dpg.add_input_text(tag="type_box", width=-1)
    dpg.add_button(label="Speak", callback=lambda:
               speak(None, dpg.get_value("type_box").strip()))
    dpg.add_button(label="Push-to-talk", callback=lambda: threading.Thread(target=stt_thread, daemon=True).start())
    dpg.add_radio_button(("Emma","Liam","John"), tag="voice", default_value="Emma")
    dpg.add_slider_int(tag="pitch", label="Pitch /st", default_value=0, min_value=-12, max_value=12)
    dpg.add_slider_float(tag="speed", label="Speed", default_value=1.0, min_value=0.5, max_value=2.0)
    dpg.add_slider_float(tag="tone",  label="Tone",  default_value=0.0, min_value=-1.0, max_value=1.0)
    dpg.add_slider_float(label="Volume", tag="volume", default_value=1.0, min_value=0.0, max_value=1.0)
dpg.create_viewport(title="TalkBox", width=420, height=320)
dpg.setup_dearpygui(); dpg.show_viewport()

threading.Thread(target=socket_thread, daemon=True).start()
threading.Thread(target=audio_consumer, daemon=True).start()
while dpg.is_dearpygui_running(): dpg.render_dearpygui_frame()
dpg.destroy_context()