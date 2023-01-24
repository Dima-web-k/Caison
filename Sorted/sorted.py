import sys
from os import *
from shutil import *
from time import ctime
from easygui import diropenbox
from sorted_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6 import QtCore
import pyttsx3

speak_engine = pyttsx3.init()

def speak(what):
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.main)
        self.ui.pushButton_4.clicked.connect(self.set_dir)
        self.ui.comboBox_2.setEnabled(False)
        self.ui.comboBox.currentTextChanged.connect(self.do_something)
        speak('Пожалуйста, укажите папку для сортировки.')
    def do_something(self):
        if self.ui.comboBox.currentText() == "По дате создания":
            self.ui.comboBox_2.setEnabled(True)
        else:
            self.ui.comboBox_2.setEnabled(False)
    def main(self):
        setenn = self.ui.lineEdit_3.text()
        if setenn != '':
            pathe = str(setenn)
            rash = str()
            l = str()
            modes = self.ui.comboBox.currentText()
            d = str()
            m = str()
            y = str()
            if modes == "По типу файлов":  # Сортировка по типу файлов
                for i in listdir(pathe):
                    if i.rfind('.') != -1:
                        rash = i[i.rfind('.') + 1::]
                        if rash == 'txt' or rash == 'text' or rash == 'log':
                            l = 'Текстовые файлы'
                        elif rash == 'jpg' or rash == 'png' or rash == 'bmp' or rash == 'gif' or rash == 'tif' or rash == 'raw':
                            l = 'Изображения'
                        elif rash == 'doc' or rash == 'docx' or rash == 'pdf':
                            l = 'Документы'
                        elif rash == 'xls' or rash == 'xlsx':
                            l = 'Таблицы'
                        elif rash == 'lnk':
                            l = 'Ярлыки'
                        elif rash == 'zip' or rash == 'rar' or rash == '7z':
                            l = 'Архивы'
                        elif rash == 'mp4' or rash == 'avi':
                            l = 'Видео'
                        elif rash == 'mp3' or rash == 'wav':
                            l = 'Музыка'
                        else:
                            l = 'Другое'
                        if l not in listdir(pathe):
                            mkdir(pathe + l)
                        move(pathe + i, pathe + l)
            elif modes == "По дате создания":
                modes2 = self.ui.comboBox_2.currentText()
                for i in listdir(pathe):
                    l = path.getctime(pathe + i)
                    l1 = ctime(l).split(' ')
                    while l1.count("") > 0:
                        l1.remove("")
                    d = l1[2]
                    m = l1[1]
                    y = l1[4]

                    if m == 'Jan':
                        m = '01'
                    elif m == 'Feb':
                        m = '02'
                    elif m == 'Mar':
                        m = '03'
                    elif m == 'Apr':
                        m = '04'
                    elif m == 'May':
                        m = '05'
                    elif m == 'Jun':
                        m = '06'
                    elif m == 'Jul':
                        m = '07'
                    elif m == 'Aug':
                        m = '08'
                    elif m == 'Sep':
                        m = '09'
                    elif m == 'Oct':
                        m = '10'
                    elif m == 'Nov':
                        m = '11'
                    elif m == 'Dec':
                        m = '12'
                    if modes2 == "Год Месяц День":
                        l = d + '.' + m + '.' + y
                    elif modes2 == "Год Месяц":
                        l = m + '.' + y
                    elif modes2 == "Год":
                        l = y
                    if l not in listdir(pathe):
                        mkdir(pathe + l)
                    move(pathe + i, pathe + l)
            elif modes == "По размеру файла":  # сортировка по размеру
                for i in listdir(pathe):
                    if path.getsize(pathe + i) < 1024:
                        l = 'Очень маленькие'
                    elif path.getsize(pathe + i) < 1024 ** 2:
                        l = 'Маленькие'
                    elif path.getsize(pathe + i) < 1024 ** 3:
                        l = 'Средние'
                    else:
                        l = 'Тяжёлые'
                    if l not in listdir(pathe):
                        mkdir(pathe + l)
                    move(pathe + i, pathe + l)
            speak('Файлы отсортированны')
            sys.exit()
    def set_dir(self):
        direct = diropenbox()
        self.ui.lineEdit_3.setText(direct + "\\")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())