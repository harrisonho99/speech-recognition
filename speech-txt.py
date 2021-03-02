import speech_recognition as sr
import os
import playsound
import time
from gtts import gTTS

language = {"english": "en", "vietnamese": "vi",
            "french": "fr", "dutch": "nl", "chinese_spl": "zh-CN", "korean": "ko"}


def speak():
    text = input("enter terms: ")
    tts = gTTS(text, lang=language["vietnamese"])
    filename = "speech.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


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


speak()
# speak = get_audio()
# if "hello" in term:
# speak("hi there")
# elif "your name" in term:
# speak("My name is Harrison")
