from flask import Flask, request
from talkbox import speak
app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts_route():
    text = request.get_data(as_text=True)
    speak(None, text)
    return "ok\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)