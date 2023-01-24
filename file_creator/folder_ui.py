# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'folder_maker.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 570)
        MainWindow.setStyleSheet(u"background-color: #282828;\n"
"color:#ffffff;\n"
"font: 15pt \"Courier New\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 531, 16))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 440, 141, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color:#61B458;\n"
"	font:15pt \"Times New Roman\";\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#4de941;\n"
"}")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 350, 611, 31))
        self.lineEdit.setStyleSheet(u"background-color:#E9E3E3;\n"
"border-radius: 5px;\n"
"color:#282828;")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 100, 231, 22))
        self.comboBox.setStyleSheet(u"background-color:#E9E3E3;\n"
"border-radius: 5px;\n"
"color:#282828;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 270, 761, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0433\u0434\u0435 \u0445\u043e\u0442\u0438\u0442\u0435 \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0441\u0442\u043e\u043b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0438", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043b\u0438 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u0438 \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0445\u043e\u0442\u0438\u0442\u0435 \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443:", None))
    # retranslateUi

