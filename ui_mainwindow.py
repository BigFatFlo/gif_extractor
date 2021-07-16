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
        MainWindow.resize(740, 773)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.videoComboBox = QComboBox(self.centralwidget)
        self.videoComboBox.addItem("")
        self.videoComboBox.setObjectName(u"videoComboBox")
        self.videoComboBox.setMinimumSize(QSize(200, 25))
        self.videoComboBox.setMaximumSize(QSize(200, 25))

        self.verticalLayout.addWidget(self.videoComboBox, 0, Qt.AlignHCenter)

        self.gifComboBox = QComboBox(self.centralwidget)
        self.gifComboBox.addItem("")
        self.gifComboBox.setObjectName(u"gifComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gifComboBox.sizePolicy().hasHeightForWidth())
        self.gifComboBox.setSizePolicy(sizePolicy1)
        self.gifComboBox.setMinimumSize(QSize(200, 25))
        self.gifComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout.addWidget(self.gifComboBox, 0, Qt.AlignHCenter)

        self.startFrameLayout = QHBoxLayout()
        self.startFrameLayout.setObjectName(u"startFrameLayout")
        self.startTimeLayout = QVBoxLayout()
        self.startTimeLayout.setObjectName(u"startTimeLayout")
        self.startTimeLabel = QLabel(self.centralwidget)
        self.startTimeLabel.setObjectName(u"startTimeLabel")
        self.startTimeLabel.setMinimumSize(QSize(200, 25))
        self.startTimeLabel.setMaximumSize(QSize(200, 25))
        self.startTimeLabel.setAlignment(Qt.AlignCenter)

        self.startTimeLayout.addWidget(self.startTimeLabel, 0, Qt.AlignHCenter)

        self.startTimeLineEdit = QLineEdit(self.centralwidget)
        self.startTimeLineEdit.setObjectName(u"startTimeLineEdit")
        self.startTimeLineEdit.setMinimumSize(QSize(200, 25))
        self.startTimeLineEdit.setMaximumSize(QSize(200, 25))

        self.startTimeLayout.addWidget(self.startTimeLineEdit, 0, Qt.AlignHCenter)

        self.startFrameButtonsLayout = QHBoxLayout()
        self.startFrameButtonsLayout.setObjectName(u"startFrameButtonsLayout")
        self.previousStartFrameButton = QPushButton(self.centralwidget)
        self.previousStartFrameButton.setObjectName(u"previousStartFrameButton")
        self.previousStartFrameButton.setMinimumSize(QSize(200, 25))
        self.previousStartFrameButton.setMaximumSize(QSize(200, 25))

        self.startFrameButtonsLayout.addWidget(self.previousStartFrameButton)

        self.nextStartFrameButton = QPushButton(self.centralwidget)
        self.nextStartFrameButton.setObjectName(u"nextStartFrameButton")
        self.nextStartFrameButton.setMinimumSize(QSize(200, 25))
        self.nextStartFrameButton.setMaximumSize(QSize(200, 25))

        self.startFrameButtonsLayout.addWidget(self.nextStartFrameButton)


        self.startTimeLayout.addLayout(self.startFrameButtonsLayout)


        self.startFrameLayout.addLayout(self.startTimeLayout)

        self.startFrameLabel = QLabel(self.centralwidget)
        self.startFrameLabel.setObjectName(u"startFrameLabel")
        self.startFrameLabel.setMinimumSize(QSize(304, 180))
        self.startFrameLabel.setMaximumSize(QSize(304, 180))

        self.startFrameLayout.addWidget(self.startFrameLabel)


        self.verticalLayout.addLayout(self.startFrameLayout)

        self.endFrameLayout = QHBoxLayout()
        self.endFrameLayout.setObjectName(u"endFrameLayout")
        self.endTimeLayout = QVBoxLayout()
        self.endTimeLayout.setObjectName(u"endTimeLayout")
        self.endTimeLabel = QLabel(self.centralwidget)
        self.endTimeLabel.setObjectName(u"endTimeLabel")
        self.endTimeLabel.setMinimumSize(QSize(200, 25))
        self.endTimeLabel.setMaximumSize(QSize(200, 25))
        self.endTimeLabel.setAlignment(Qt.AlignCenter)

        self.endTimeLayout.addWidget(self.endTimeLabel, 0, Qt.AlignHCenter)

        self.endTimeLineEdit = QLineEdit(self.centralwidget)
        self.endTimeLineEdit.setObjectName(u"endTimeLineEdit")
        self.endTimeLineEdit.setMinimumSize(QSize(200, 25))
        self.endTimeLineEdit.setMaximumSize(QSize(200, 25))

        self.endTimeLayout.addWidget(self.endTimeLineEdit, 0, Qt.AlignHCenter)

        self.endFrameButtonsLayout = QHBoxLayout()
        self.endFrameButtonsLayout.setObjectName(u"endFrameButtonsLayout")
        self.previousEndFrameButton = QPushButton(self.centralwidget)
        self.previousEndFrameButton.setObjectName(u"previousEndFrameButton")
        self.previousEndFrameButton.setMinimumSize(QSize(200, 25))
        self.previousEndFrameButton.setMaximumSize(QSize(200, 25))

        self.endFrameButtonsLayout.addWidget(self.previousEndFrameButton)

        self.nextEndFrameButton = QPushButton(self.centralwidget)
        self.nextEndFrameButton.setObjectName(u"nextEndFrameButton")
        self.nextEndFrameButton.setMinimumSize(QSize(200, 25))
        self.nextEndFrameButton.setMaximumSize(QSize(200, 25))

        self.endFrameButtonsLayout.addWidget(self.nextEndFrameButton)


        self.endTimeLayout.addLayout(self.endFrameButtonsLayout)


        self.endFrameLayout.addLayout(self.endTimeLayout)

        self.endFrameLabel = QLabel(self.centralwidget)
        self.endFrameLabel.setObjectName(u"endFrameLabel")
        self.endFrameLabel.setMinimumSize(QSize(304, 180))
        self.endFrameLabel.setMaximumSize(QSize(304, 180))

        self.endFrameLayout.addWidget(self.endFrameLabel)


        self.verticalLayout.addLayout(self.endFrameLayout)

        self.topLineTextLabel = QLabel(self.centralwidget)
        self.topLineTextLabel.setObjectName(u"topLineTextLabel")
        self.topLineTextLabel.setMinimumSize(QSize(200, 25))
        self.topLineTextLabel.setMaximumSize(QSize(200, 25))
        self.topLineTextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.topLineTextLabel, 0, Qt.AlignHCenter)

        self.topLineTextEdit = QTextEdit(self.centralwidget)
        self.topLineTextEdit.setObjectName(u"topLineTextEdit")
        self.topLineTextEdit.setMinimumSize(QSize(400, 25))
        self.topLineTextEdit.setMaximumSize(QSize(400, 25))
        self.topLineTextEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.topLineTextEdit, 0, Qt.AlignHCenter)

        self.bottomLineTextLabel = QLabel(self.centralwidget)
        self.bottomLineTextLabel.setObjectName(u"bottomLineTextLabel")
        self.bottomLineTextLabel.setMinimumSize(QSize(200, 25))
        self.bottomLineTextLabel.setMaximumSize(QSize(200, 25))
        self.bottomLineTextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.bottomLineTextLabel, 0, Qt.AlignHCenter)

        self.bottomLineTextEdit = QTextEdit(self.centralwidget)
        self.bottomLineTextEdit.setObjectName(u"bottomLineTextEdit")
        self.bottomLineTextEdit.setMinimumSize(QSize(400, 25))
        self.bottomLineTextEdit.setMaximumSize(QSize(400, 25))
        self.bottomLineTextEdit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.bottomLineTextEdit, 0, Qt.AlignHCenter)

        self.videoNameLabel = QLabel(self.centralwidget)
        self.videoNameLabel.setObjectName(u"videoNameLabel")
        self.videoNameLabel.setMinimumSize(QSize(200, 25))
        self.videoNameLabel.setMaximumSize(QSize(200, 25))
        self.videoNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.videoNameLabel, 0, Qt.AlignHCenter)

        self.videoNameLineEdit = QLineEdit(self.centralwidget)
        self.videoNameLineEdit.setObjectName(u"videoNameLineEdit")
        self.videoNameLineEdit.setMinimumSize(QSize(200, 25))
        self.videoNameLineEdit.setMaximumSize(QSize(200, 25))

        self.verticalLayout.addWidget(self.videoNameLineEdit, 0, Qt.AlignHCenter)

        self.gifNameLabel = QLabel(self.centralwidget)
        self.gifNameLabel.setObjectName(u"gifNameLabel")
        self.gifNameLabel.setMinimumSize(QSize(200, 25))
        self.gifNameLabel.setMaximumSize(QSize(200, 25))
        self.gifNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.gifNameLabel, 0, Qt.AlignHCenter)

        self.gifNameLineEdit = QLineEdit(self.centralwidget)
        self.gifNameLineEdit.setObjectName(u"gifNameLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gifNameLineEdit.sizePolicy().hasHeightForWidth())
        self.gifNameLineEdit.setSizePolicy(sizePolicy2)
        self.gifNameLineEdit.setMinimumSize(QSize(200, 25))
        self.gifNameLineEdit.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.gifNameLineEdit, 0, Qt.AlignHCenter)

        self.saveGifDataCheckBox = QCheckBox(self.centralwidget)
        self.saveGifDataCheckBox.setObjectName(u"saveGifDataCheckBox")
        self.saveGifDataCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.saveGifDataCheckBox, 0, Qt.AlignHCenter)

        self.extractButton = QPushButton(self.centralwidget)
        self.extractButton.setObjectName(u"extractButton")
        self.extractButton.setMinimumSize(QSize(200, 25))
        self.extractButton.setMaximumSize(QSize(200, 25))

        self.verticalLayout.addWidget(self.extractButton, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 740, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.videoComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New video", None))

        self.gifComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New gif", None))

        self.startTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Start Time", None))
        self.startTimeLineEdit.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.previousStartFrameButton.setText(QCoreApplication.translate("MainWindow", u"Previous Frame", None))
        self.nextStartFrameButton.setText(QCoreApplication.translate("MainWindow", u"Next Frame", None))
        self.startFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Start Frame", None))
        self.endTimeLabel.setText(QCoreApplication.translate("MainWindow", u"End Time", None))
        self.endTimeLineEdit.setText(QCoreApplication.translate("MainWindow", u"00:00:00:000", None))
        self.previousEndFrameButton.setText(QCoreApplication.translate("MainWindow", u"Previous Frame", None))
        self.nextEndFrameButton.setText(QCoreApplication.translate("MainWindow", u"Next Frame", None))
        self.endFrameLabel.setText(QCoreApplication.translate("MainWindow", u"EndFrame", None))
        self.topLineTextLabel.setText(QCoreApplication.translate("MainWindow", u"Top Line Text", None))
        self.bottomLineTextLabel.setText(QCoreApplication.translate("MainWindow", u"Bottom Line Text", None))
        self.videoNameLabel.setText(QCoreApplication.translate("MainWindow", u"Video name", None))
        self.videoNameLineEdit.setText("")
        self.gifNameLabel.setText(QCoreApplication.translate("MainWindow", u"Gif name", None))
        self.gifNameLineEdit.setText("")
        self.saveGifDataCheckBox.setText(QCoreApplication.translate("MainWindow", u"Save gif data", None))
        self.extractButton.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
    # retranslateUi

