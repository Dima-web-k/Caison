# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sorted2.ui'
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
        MainWindow.resize(677, 440)
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #282828;\n"
"color:#ffffff;\n"
"font: 15pt \"Courier New\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 330, 201, 51))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color:#61B458;\n"
"	font:15pt \"Times New Roman\";\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#4de941;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 50, 271, 41))
        self.label_4.setFont(font)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(510, 140, 131, 41))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color:#61B458;\n"
"	font:15pt \"Times New Roman\";\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#4de941;\n"
"}")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(60, 140, 461, 41))
        self.lineEdit_3.setStyleSheet(u"background-color:#E9E3E3;\n"
"border-radius: 5px;\n"
"color:#282828;")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 260, 201, 22))
        self.comboBox.setStyleSheet(u"background-color:#E9E3E3;\n"
"border-radius: 5px;\n"
"color:#282828;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 200, 291, 41))
        self.label_5.setFont(font)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(340, 260, 201, 22))
        self.comboBox_2.setStyleSheet(u"background-color:#E9E3E3;\n"
"border-radius: 5px;\n"
"color:#282828;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 200, 321, 41))
        self.label_6.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0434\u043e \u043f\u0430\u043f\u043a\u0438:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0442\u0438\u043f\u0443 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0434\u0430\u0442\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0443 \u0444\u0430\u0439\u043b\u0430", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438:", None))
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u041c\u0435\u0441\u044f\u0446", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u041c\u0435\u0441\u044f\u0446 \u0414\u0435\u043d\u044c", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u043e\u0440\u043c\u0430\u0442 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438:", None))
    # retranslateUi

