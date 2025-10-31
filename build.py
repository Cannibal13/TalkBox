#!/usr/bin/env python3
import PyInstaller.__main__, os, shutil, sys
PyInstaller.__main__.run([
    "talkbox.py",
    "--onefile",
    "--add-data", "tts.py:.",
    "--add-data", "stt.py:.",
    "--add-data", "socket_server.py:.",
    "--name", "talkbox",
    "--distpath", "dist",
    "--workpath", "build",
    "--specpath", ".",
    "--clean",
])
print("Binary ready → dist/talkbox.exe (or talkbox)")