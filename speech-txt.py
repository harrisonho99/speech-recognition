import speech_recognition as sr
import os
import playsound
import time
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "speech.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(
                audio_data=audio, language="en-US", key=None, show_all=False)
            print(said)
        except Exception as e:
            print("Error: ", + str(e))
    return said


speak("start talk")
term = get_audio()
if "hello" in term:
    speak("hi there")
elif "your name" in term:
    speak("My name is Harrison")
