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
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def read_timestamps_json():
    json_file_name = "timestamps.json"
    try:
        file = open(json_file_name, "r")
    except IOError:
        print("Failed to open timestamps file {}\n".format(json_file_name))
        return ([], None)
    timestamps_data = json.load(file)
    return timestamps_data


def launch_extraction(video, start_timestamp, end_timestamp, top_line_text, bottom_line_text, gif_name):
    start_time_ms = get_ms_from_timestamp(start_timestamp)
    end_time_ms = get_ms_from_timestamp(end_timestamp)
    i=0
    ret = True
    frame_rate_s = video.get(cv2.CAP_PROP_FPS)
    nb_of_frames = int((end_time_ms - start_time_ms) * frame_rate_s / 1000)
    video.set(cv2.CAP_PROP_POS_MSEC, start_time_ms)
    while(video.isOpened() and ret):
        if i == nb_of_frames:
            break
        ret, frame = video.read()
        frame = cv2.resize(frame, (608, 360), interpolation = cv2.INTER_AREA)
        cv2.imwrite('./frames/frame_'+str(i)+'.jpg',frame)
        i+=1
        print("Processing frame n°{}".format(i))

    video.release()
    cv2.destroyAllWindows()

    text_size = 50
    line_spacing = 235
    max_line_length = max(len(top_line_text), len(bottom_line_text))
    if max_line_length > 0:
        ratio = min(25 / max_line_length, 1)
    else:
        ratio = 1
    new_text_size = int(text_size * ratio)
    line_spacing += int((text_size - new_text_size) / ratio)
    text_size = new_text_size

    output = subprocess.check_output(['./gimp_bash.sh', "{}".format(nb_of_frames), top_line_text, bottom_line_text, "{}".format(text_size), "{}".format(line_spacing), gif_name])

    json_file_name = "timestamps.json"
    try:
        file = open(json_file_name, "r", encoding='utf8')
    except IOError:
        print("Failed to open timestamps file {} to read\n".format(json_file_name))
        return
    timestamps_data = json.load(file)
    timestamps_data[gif_name] = {"start" : start_timestamp, "end" : end_timestamp}
    try:
        file = open(json_file_name, "w", encoding='utf8')
    except IOError:
        print("Failed to open timestamps file {} to write\n".format(json_file_name))
        return
    json.dump(timestamps_data, file, indent = 4, ensure_ascii=False)

    print("Gif created: {}".format(gif_name))
    print("Start timestamp = {}".format(start_timestamp))
    print("End timestamp = {}".format(end_timestamp))


class FrameSelectorUI():
    def __init__(self, time_edit, frame_label, previous_button, next_button):
        self.time_edit = time_edit
        self.frame_label = frame_label
        self.previous_button = previous_button
        self.next_button = next_button


class FrameSelector():
    def __init__(self, video, frame_selector_ui):
        self.video = video
        self.ui = frame_selector_ui
        self.ui.time_edit.returnPressed.connect(self.new_frame)
        self.ui.previous_button.clicked.connect(self.previous_frame)
        self.ui.next_button.clicked.connect(self.next_frame)
        self.new_frame()

    def new_frame(self):
        time = get_ms_from_timestamp(self.ui.time_edit.text())
        self.video.set(cv2.CAP_PROP_POS_MSEC, time)
        self.display_frame()

    def next_frame(self):
        current_time = get_ms_from_timestamp(self.ui.time_edit.text())
        frame_rate_s = video.get(cv2.CAP_PROP_FPS)
        ms_per_frame = int((1000/frame_rate_s))
        new_time = current_time + ms_per_frame
        self.ui.time_edit.setText(get_timestamp_from_ms(new_time))
        self.display_frame()

    def previous_frame(self):
        current_time = get_ms_from_timestamp(self.ui.time_edit.text())
        frame_rate_s = video.get(cv2.CAP_PROP_FPS)
        ms_per_frame = int((1000/frame_rate_s))
        new_time = max(current_time - ms_per_frame, 0)
        self.ui.time_edit.setText(get_timestamp_from_ms(new_time))
        self.new_frame()

    def display_frame(self):
        ret, frame = self.video.read()
        frame = cv2.resize(frame, (304, 180), interpolation = cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
        pixmap = QPixmap(304, 180)
        imgQ = QImage(frame, 304, 180, QImage.Format_RGB888)
        pixmap.convertFromImage(imgQ, Qt.ColorOnly)
        self.ui.frame_label.setPixmap(pixmap)


def get_ms_from_timestamp(timestamp):
    times = timestamp.split(":")
    hour = int(times[0])
    minutes = int(times[1])
    seconds = int(times[2])
    ms = int(times[3])
    time_in_ms = hour * 60 * 60 * 1000 + minutes * 60 * 1000 + seconds * 1000 + ms
    return time_in_ms

def get_timestamp_from_ms(time_in_ms):
    time = time_in_ms
    ms = time % 1000
    time = (time - ms) // 1000
    seconds = time % (60)
    time = (time - seconds) // 60
    minutes = time % (60)
    time = (time - minutes) // 60
    hours = time
    return "{:02d}:{:02d}:{:02d}:{:03d}".format(hours, minutes, seconds, ms)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Opens the Video file
    video = cv2.VideoCapture('./test_video.mp4')

    window = MainWindow()
    window.show()

    top_line_text_edit = window.ui.topLineTextEdit
    bottom_line_text_edit = window.ui.bottomLineTextEdit
    gif_name_edit = window.ui.gifNameLineEdit
    extract_button = window.ui.extractButton

    start_frame_ui = FrameSelectorUI(window.ui.startTimeLineEdit,
                                     window.ui.startFrameLabel,
                                     window.ui.previousStartFrameButton,
                                     window.ui.nextStartFrameButton)
    end_frame_ui = FrameSelectorUI(window.ui.endTimeLineEdit,
                                     window.ui.endFrameLabel,
                                     window.ui.previousEndFrameButton,
                                     window.ui.nextEndFrameButton)

    start_frame_selector = FrameSelector(cv2.VideoCapture('./test_video.mp4'), start_frame_ui)
    end_frame_selector = FrameSelector(cv2.VideoCapture('./test_video.mp4'), end_frame_ui)

    extract_button.clicked.connect(lambda: launch_extraction(cv2.VideoCapture('./test_video.mp4'),
                                                             start_frame_selector.ui.time_edit.text(),
                                                             end_frame_selector.ui.time_edit.text(),
                                                             top_line_text_edit.toPlainText(),
                                                             bottom_line_text_edit.toPlainText(),
                                                             gif_name_edit.text()))

    gif_name_edit.returnPressed.connect(lambda: launch_extraction(cv2.VideoCapture('./test_video.mp4'),
                                                                  start_frame_selector.ui.time_edit.text(),
                                                                  end_frame_selector.ui.time_edit.text(),
                                                                  top_line_text_edit.toPlainText(),
                                                                  bottom_line_text_edit.toPlainText(),
                                                                  gif_name_edit.text()))

    sys.exit(app.exec_())
