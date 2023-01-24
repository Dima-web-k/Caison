import sys

from PySide6.QtWidgets import QApplication, QMainWindow
import random
from folder_ui import Ui_MainWindow
from os import *
import pyttsx3
import speech_recognition as sr
speak_engine = pyttsx3.init()
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.search)

    def search(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            rand = random.randint(1,2)
            if rand == 1:
                speak('Давайте уточним имя папки')
            if rand == 2:
                speak('Как назовём папку?')
            s = r.listen(source)
        voice = r.recognize_google(s, language="ru-RU").lower()
        choice = self.ui.comboBox.currentText()
        if choice == "Рабочий стол":
            text = path.join(getenv("userprofile"), "Desktop")
            chdir(text)
            mkdir(voice)
            speak('Папка создана')
        elif choice == "Папка пользователя":
            text = path.join(getenv("userprofile"))
            chdir(text)
            mkdir(voice)
            speak('Папка создана')
        elif choice == "Загрузки":
            text = path.join(getenv("userprofile"),"Downloads")
            chdir(text)
            mkdir(voice)
            speak('Папка создана')
        else:
            text = self.ui.lineEdit.text()
            chdir(text)
            mkdir(voice)
            speak('Папка создана')


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())