#! /usr/bin/python

# This Python file uses the following encoding: utf-8
import cv2
import subprocess
import sys
import time
import serial
from threading import Thread, RLock
import signal
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import QFile, QThread, Signal, QObject, QRunnable, QThreadPool, QPoint, QRect, QByteArray, QTimer, Qt
from PySide2.QtGui import QTextCursor, QIcon, QPixmap, QImage, QPainter, QPen, QColor, QPainterPath, QPainterPathStroker, QBrush
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QStyleFactory;
import struct

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def launch_extraction(video, start_time_ms, end_time_ms, top_line_text, bottom_line_text, gif_name):
    print("Start time = {}".format(start_time_ms))
    print("End time = {}".format(end_time_ms))
    print("Total time = {}".format(end_time_ms - start_time_ms))
    i=0
    ret = True
    frame_rate_s = video.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {}".format(frame_rate_s))
    nb_of_frames = int((end_time_ms - start_time_ms) * frame_rate_s / 1000)
    print("nb_of_frames = {}".format(nb_of_frames))
    video.set(cv2.CAP_PROP_POS_MSEC, start_time_ms)
    while(video.isOpened() and ret):
        ret, frame = video.read()
        frame = cv2.resize(frame, (608, 360), interpolation = cv2.INTER_AREA)
        cv2.imwrite('frame_'+str(i)+'.jpg',frame)
        i+=1
        if i == nb_of_frames:
            break
        print("Processing image n°{}".format(i))

    video.release()
    cv2.destroyAllWindows()

    output = subprocess.check_output(['./gimp_bash.sh', "{}".format(nb_of_frames), top_line_text, bottom_line_text, gif_name])
    print("Done")


def update_frame(frame_label, video, time):
    video.set(cv2.CAP_PROP_POS_MSEC, time)
    ret, frame = video.read()
    frame = cv2.resize(frame, (304, 180), interpolation = cv2.INTER_AREA)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
    pixmap = QPixmap(304, 180)
    imgQ = QImage(frame, 304, 180, QImage.Format_RGB888)
    pixmap.convertFromImage(imgQ, Qt.ColorOnly)
    frame_label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Opens the Video file
    video = cv2.VideoCapture('./test_video.mp4')

    window = MainWindow()
    window.show()

    start_time_edit = window.ui.startTimeLineEdit
    end_time_edit = window.ui.endTimeLineEdit
    top_line_text_edit = window.ui.topLineTextEdit
    bottom_line_text_edit = window.ui.bottomLineTextEdit
    gif_name_edit = window.ui.gifNameTextEdit
    extract_button = window.ui.extractButton
    start_frame_label = window.ui.startFrameLabel
    end_frame_label = window.ui.endFrameLabel

    start_time_edit.returnPressed.connect(lambda : update_frame(start_frame_label, video, int(start_time_edit.text())))
    end_time_edit.returnPressed.connect(lambda : update_frame(end_frame_label, video, int(end_time_edit.text())))

    extract_button.clicked.connect(lambda: launch_extraction(video,
                                                             int(start_time_edit.text()),
                                                             int(end_time_edit.text()),
                                                             top_line_text_edit.toPlainText(),
                                                             bottom_line_text_edit.toPlainText(),
                                                             gif_name_edit.toPlainText()))

    sys.exit(app.exec_())
