import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    
    # Optional: Change voice properties
    engine.setProperty('rate', 150)     # Speed (default is ~200)
    engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index to pick different voice
    
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech:\n")
    speak_text(text)