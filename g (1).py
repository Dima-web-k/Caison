from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from work_ui import Ui_MainWindow
import json, speech_recognition as sr, webbrowser, pyttsx3
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
        self.ui.pushButton_2.clicked.connect(self.add)

    def add(self):
        global worf
        with open('data.json', 'r') as (f):
            worf = json.loads(f.read())
        str1 = ''
        workspace_name = self.ui.lineEdit.text()
        value = self.ui.lineEdit_2.text()
        if workspace_name not in worf:
            worf[workspace_name] = [value]
        else:
            worf[workspace_name].append(value)
        with open('data.json', 'w') as (f):
            f.write(json.dumps(worf))


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
# okay decompiling g.pyc
