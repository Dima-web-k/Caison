# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'w.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 572)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color:#14c607;\n"
"font: 15pt \"Courier New\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(36, 100, 331, 20))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(400, 100, 291, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(36, 70, 331, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 70, 481, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 150, 141, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color:#14c607;\n"
"	font:15pt \"Times New Roman\";\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#4de941;\n"
"}\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 0, 831, 41))
        self.label_4.setStyleSheet(u"font: 9pt \"Courier New\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043e\u0440\u043a\u0441\u043f\u0435\u0439\u0441\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0438\u043b\u0438 \u0430\u0434\u0440\u0435\u0441 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0432\u043e\u0440\u043a\u0441\u043f\u0435\u0439\u0441\u0430 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0435\u0433\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435, \u043f\u043e\u0441\u043b\u0435 \u0447\u0435\u0433\u043e \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0440\u0430\u0437 \u043f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 </p><p>\u0438\u043b\u0438 \u0430\u0434\u0440\u0435\u0441 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u043e\u0441\u043b\u0435 \u0447\u0435\u0433\u043e \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 &quot;\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c&quot;</p></body></html>", None))
    # retranslateUi

