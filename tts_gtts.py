# gTTS (Google TTS, .mp3, requires internet)
from gtts import gTTS
import os
import platform
import subprocess

def save_and_play_speech(text, filename="output.mp3"):
    try:
        # Generate speech and save to file
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        print(f"✅ Saved to {filename}")

        # Auto-play
        system = platform.system()
        if system == "Darwin":  # macOS
            subprocess.call(["afplay", filename])
        elif system == "Windows":
            os.startfile(filename)
        elif system == "Linux":
            subprocess.call(["mpg123", filename])
        else:
            print("⚠️ Unsupported OS for auto-play.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    text = input("📝 Enter text to convert to speech:\n")
    save_and_play_speech(text)