# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(771, 568)
        MainWindow.setStyleSheet(u"background-color: #282828;\n"
"color:#ffffff;\n"
"font: 15pt \"Courier New\";")
        self.actionDa = QAction(MainWindow)
        self.actionDa.setObjectName(u"actionDa")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 360, 141, 41))
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
        self.lineEdit.setGeometry(QRect(80, 190, 631, 31))
        self.lineEdit.setStyleSheet(u"background-color:#E9E3E3;\n"
"border-radius: 5px;\n"
"color:#282828;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 90, 531, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDa.setText(QCoreApplication.translate("MainWindow", u"da", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u0444\u0430\u0439\u043b\u0430 (\u0441 \u0440\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435\u043c):", None))
    # retranslateUi

