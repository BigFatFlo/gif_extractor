# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(418, 397)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.startTimeLabel = QLabel(self.centralwidget)
        self.startTimeLabel.setObjectName(u"startTimeLabel")
        self.startTimeLabel.setMinimumSize(QSize(200, 25))
        self.startTimeLabel.setMaximumSize(QSize(200, 25))
        self.startTimeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.startTimeLabel)

        self.startTimeTextEdit = QTextEdit(self.centralwidget)
        self.startTimeTextEdit.setObjectName(u"startTimeTextEdit")
        self.startTimeTextEdit.setMinimumSize(QSize(200, 25))
        self.startTimeTextEdit.setMaximumSize(QSize(200, 25))
        self.startTimeTextEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.startTimeTextEdit)

        self.endTimeLabel = QLabel(self.centralwidget)
        self.endTimeLabel.setObjectName(u"endTimeLabel")
        self.endTimeLabel.setMinimumSize(QSize(200, 25))
        self.endTimeLabel.setMaximumSize(QSize(200, 25))
        self.endTimeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.endTimeLabel)

        self.endTimeTextEdit = QTextEdit(self.centralwidget)
        self.endTimeTextEdit.setObjectName(u"endTimeTextEdit")
        self.endTimeTextEdit.setMinimumSize(QSize(200, 25))
        self.endTimeTextEdit.setMaximumSize(QSize(200, 25))
        self.endTimeTextEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.endTimeTextEdit)

        self.topLineTextLabel = QLabel(self.centralwidget)
        self.topLineTextLabel.setObjectName(u"topLineTextLabel")
        self.topLineTextLabel.setMinimumSize(QSize(200, 25))
        self.topLineTextLabel.setMaximumSize(QSize(200, 25))
        self.topLineTextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.topLineTextLabel)

        self.topLineTextEdit = QTextEdit(self.centralwidget)
        self.topLineTextEdit.setObjectName(u"topLineTextEdit")
        self.topLineTextEdit.setMinimumSize(QSize(400, 25))
        self.topLineTextEdit.setMaximumSize(QSize(400, 25))
        self.topLineTextEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.topLineTextEdit)

        self.bottomLineTextLabel = QLabel(self.centralwidget)
        self.bottomLineTextLabel.setObjectName(u"bottomLineTextLabel")
        self.bottomLineTextLabel.setMinimumSize(QSize(200, 25))
        self.bottomLineTextLabel.setMaximumSize(QSize(200, 25))
        self.bottomLineTextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.bottomLineTextLabel)

        self.bottomLineTextEdit = QTextEdit(self.centralwidget)
        self.bottomLineTextEdit.setObjectName(u"bottomLineTextEdit")
        self.bottomLineTextEdit.setMinimumSize(QSize(400, 25))
        self.bottomLineTextEdit.setMaximumSize(QSize(400, 25))
        self.bottomLineTextEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.bottomLineTextEdit)

        self.gifNameLabel = QLabel(self.centralwidget)
        self.gifNameLabel.setObjectName(u"gifNameLabel")
        self.gifNameLabel.setMinimumSize(QSize(200, 25))
        self.gifNameLabel.setMaximumSize(QSize(200, 25))
        self.gifNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.gifNameLabel)

        self.gifNameTextEdit = QTextEdit(self.centralwidget)
        self.gifNameTextEdit.setObjectName(u"gifNameTextEdit")
        self.gifNameTextEdit.setMinimumSize(QSize(200, 25))
        self.gifNameTextEdit.setMaximumSize(QSize(200, 25))
        self.gifNameTextEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.gifNameTextEdit)

        self.extractButton = QPushButton(self.centralwidget)
        self.extractButton.setObjectName(u"extractButton")
        self.extractButton.setMinimumSize(QSize(200, 25))
        self.extractButton.setMaximumSize(QSize(200, 25))

        self.verticalLayout.addWidget(self.extractButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 418, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Start Time", None))
        self.endTimeLabel.setText(QCoreApplication.translate("MainWindow", u"End Time", None))
        self.topLineTextLabel.setText(QCoreApplication.translate("MainWindow", u"Top Line Text", None))
        self.bottomLineTextLabel.setText(QCoreApplication.translate("MainWindow", u"Bottom Line Text", None))
        self.gifNameLabel.setText(QCoreApplication.translate("MainWindow", u"Gif name", None))
        self.extractButton.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
    # retranslateUi

