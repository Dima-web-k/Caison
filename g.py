import os
import json
import speech_recognition as sr
import webbrowser
import pyttsx3
speak_engine = pyttsx3.init()

worf = dict()

def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def call():
    parent_dir = os.path.dirname(os.path.abspath("caison.exe"))
    storage_path = os.path.join(parent_dir, 'work_add\data.json')
    with open(storage_path) as json_file:
        worf = json.load(json_file)

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        speak('Начнём работу?')
        s = r.listen(source)
        voice = r.recognize_google(s, language="ru-RU").lower()

    print(voice)

    if voice in worf:
        for i in worf[voice]:
            webbrowser.open(i)
    else:
        speak("Рабочего пространства с таким именем не существует")