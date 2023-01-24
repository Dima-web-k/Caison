# Голосовой ассистент Кейсон 1.0 BETA
import os
import webbrowser
import g
import speech_recognition as sr
from fuzzywuzzy.fuzz import ratio
import pyttsx3
import datetime
import subprocess
import sys
import json
# настройки
# opts = {
#     "alias": ("кейсон","кейс","кайсон","кайс","кейси","куйсон","тайсон","джейсон","казино","песня","кессон","козино","пейсон"),
#     "tbr": ("скажи","расскажи","покажи","сколько","произнеси","включи","активируй","подключи",),
#     "cmds": {
#         "ctime": ("текущее время", "сейчас времени", "который час"),
#         "files": ("найди файл", "открой файл", "мне нужен файл"),
#         "folder": ("создай папку", "сделай папку"),
#         "workspace": ("активируй воркспэйс", "воркспэйс","запусти воркспейс"),
#         "work_add": ("создай воркспэйс", "добавь воркспэйс", "мне нужен новый воркспейс"),
#         "searcher": ("что ты знаешь про", "что такое"),
#         "sorted": ("сортировка","отсортируй файлы","приступи к сортировке"),
#         "exit": ("закройся","выключись","пока")
#     }
# }
opts = dict()
with open('comands.json', 'r') as com_file:
    opts = json.load(com_file)
# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice in opts["alias"]:
            speak("Слушаю вас")
        # обращаются к Кейсону
        cmd = voice

        for x in opts["alias"]:
            cmd = cmd.replace(x, "").strip()

        for x in opts["tbr"]:
            cmd = cmd.replace(x, "").strip()

        # распознаем и выполняем команду
        cmd1 = cmd
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd["cmd"], cmd1)

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

# Распознование
def recognize_cmd(cmd):
    RC = {"cmd": "", "percent": 50}
    for c, v in opts["cmds"].items():

        for x in v:
            vrt = ratio(cmd, x)
            if vrt > RC["percent"]:
                RC["cmd"] = c
                RC["percent"] = vrt

    return RC

# Выполнение команды
def execute_cmd(cmd,cmd1):

    if cmd == "ctime":
        # сказать текущее время
        now = datetime.datetime.now()
        hour = str()
        if str(now.hour) in ["11","12","13","14","15","16","17","18","19"]:
            hour = " часов "
        elif str(now.hour)[-1] == "1":
            hour = " час "
        elif str(now.hour)[-1] in ["2","3","4"]:
            hour = " часа "
        elif str(now.hour)[-1] in ["5","6","7","8","9","0"]:
            hour = " часов "
        minute = str()
        if str(now.minute) in ["11","12","13","14","15","16","17","18","19"]:
            minute = " минут "
        elif str(now.minute)[-1] == "1":
            minute = " минута "
        elif str(now.minute)[-1] in ["2","3","4"]:
            minute = " минуты "
        elif str(now.minute)[-1] in ["5","6","7","8","9","0"]:
            minute = " минут "
        speak("Сейчас " + str(now.hour) + hour + " : " + str(now.minute)+ minute)

    elif cmd == "files":
        #поиск файла
        parent_dir = os.path.dirname(os.path.abspath("caison.exe"))
        subprocess.Popen(os.path.join(parent_dir, "search.exe"))

    elif cmd == "folder":
       #Создание папок
       parent_dir = os.path.dirname(os.path.abspath("caison.exe"))
       subprocess.Popen(os.path.join(parent_dir, "file_creator\\folder_maker.exe"))

    elif cmd == "searcher":
       # поиск в интернете
       webbrowser.open("https://yandex.ru/search/?lr=66&text=" + cmd1.split()[-1] + "&src=suggest_Pers")

    elif cmd == "workspace":
       # workspase
       g.call()

    elif cmd == "exit":
       # workspase
       speak('Досвидания')
       sys.exit()

    elif cmd == "work_add":
       # создание воркспейсов
       parent_dir = os.path.dirname(os.path.abspath("caison.exe"))
       parent_dir = parent_dir.replace("dist\caison", "")
       subprocess.Popen(os.path.join(parent_dir, 'work_add\work_add.exe'))

    elif cmd == "sorted":
       # сортировка файлов
       parent_dir = os.path.dirname(os.path.abspath("caison.exe"))
       parent_dir = parent_dir.replace("dist\caison", "")
       subprocess.Popen(os.path.join(parent_dir, 'Sorted\sorted.exe'))

    else:
        print("Команда не распознана, повторите!")

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

speak_engine = pyttsx3.init()

speak("Кейсон слушает")

while True:
    with m as source:
        audio = r.listen(source)
    callback(r, audio)  # infinity loop
