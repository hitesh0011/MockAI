import pyttsx3
import speech_recognition as sr

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def get_answer():
    """Record user's answer using microphone and convert to text."""
    r = sr.Recognizer()
    r.pause_threshold = 2.0
    r.energy_threshold = 300

    with sr.Microphone() as mic:
        print("Record your answer...")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
        print("Answer captured. Processing...")

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
