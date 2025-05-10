import pyttsx3
import os
import platform
import subprocess


def speak_text(text):
    engine = pyttsx3.init()
    
    # Optional: Change voice properties
    engine.setProperty('rate', 150)     # Speed (default is ~200)
    engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index to pick different voice
    
    engine.say(text)
    engine.runAndWait()
    
def save_and_play_speech(text, filename="output.wav"):
    # Initialize TTS engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speech rate
    engine.setProperty('volume', 1.0)  # Max volume

    # Save to file
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"✅ Saved to {filename}")

    # Auto-play audio based on OS
    system = platform.system()

    try:
        if system == "Windows":
            os.startfile(filename)
        elif system == "Darwin":  # macOS
            subprocess.call(["afplay", filename])
        elif system == "Linux":
            subprocess.call(["aplay", filename])  # or use mpg123/ffplay for mp3
        else:
            print("⚠️ Unsupported OS for auto-play.")
    except Exception as e:
        print(f"❌ Failed to play audio: {e}")

if __name__ == "__main__":
    text = input("📝 Enter text to convert to speech:\n")
    save_and_play_speech(text)