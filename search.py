import os
import webbrowser
import string
import sys
import pyttsx3
from search_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
# функции
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
        self.ui.pushButton_2.clicked.connect(self.main)
    def main(self):
        a=bool(False)
        file_name = self.ui.lineEdit.text()
        for i in get_disklist():
            for root, dirs, files in os.walk(i+'/'):
                for name in files:
                    if name.endswith(file_name):
                        webbrowser.open(os.path.join(root, name))
                        a=True
                        break
                    if a==True:
                        break
                if a==True:
                        break
            if a==True:
                break
        if a==False:
           speak("Файл не найден")
def get_disklist():
    disk_list = []
    for c in string.ascii_uppercase:
        disk = c+':'
        if os.path.isdir(disk):
            disk_list.append(disk)
    return disk_list
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())