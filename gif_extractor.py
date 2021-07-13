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
from PySide2.QtGui import QTextCursor, QIcon, QPixmap, QImage, QPainter, QPen, QColor, QPainterPath, QPainterPathStroker, QBrush, QFontMetrics
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QStyleFactory;
import struct
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Timestamps(QObject):
    updated = Signal()

    def __init__(self, file):
        QObject.__init__(self)
        self.file = file
        self.timestamps_data = None
        self.read_timestamps_json()
        self.fill_structure()

    def read_timestamps_json(self):
        try:
            file = open(self.file, "r", encoding='utf8')
        except IOError:
            print("Failed to open timestamps file {} to read\n".format(json_file_name))
            return
        self.timestamps_data = json.load(file)

    def write_timestamps_json(self, data):
        self.timestamps_data = data
        try:
            file = open(self.file, "w", encoding='utf8')
        except IOError:
            print("Failed to open timestamps file {} to write\n".format(json_file_name))
            return
        json.dump(self.timestamps_data, file, indent = 4, ensure_ascii=False)
        self.fill_structure()

    def fill_structure(self):
        self.videos = []
        self.gifs = {}
        for video_name in self.timestamps_data:
            self.videos.append(video_name)
            self.gifs[video_name] = []
            for gif in self.timestamps_data[video_name]:
                self.gifs[video_name].append(gif)
        self.updated.emit()


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
        frame_rate_s = self.video.get(cv2.CAP_PROP_FPS)
        ms_per_frame = int((1000/frame_rate_s))
        new_time = current_time + ms_per_frame
        self.ui.time_edit.setText(get_timestamp_from_ms(new_time))
        self.display_frame()

    def previous_frame(self):
        current_time = get_ms_from_timestamp(self.ui.time_edit.text())
        frame_rate_s = self.video.get(cv2.CAP_PROP_FPS)
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


class HidableGifBox():
    def __init__(self, box, window):
        self.box = box
        self.window = window

    def set_visibility(self, visible):
        self.box.setVisible(visible)
        _timer = QTimer()
        _timer.singleShot(30, self.resize_window)

    def fill_box(self, video_name, timestamps):
        self.box.clear()
        if video_name in timestamps.videos:
            gif_list = timestamps.gifs[video_name]
            self.set_visibility(True)
            self.box.addItems(gif_list)
        else:
            gif_list = []
            self.set_visibility(False)

    def resize_window(self):
        self.window.resize(self.window.width(), self.window.minimumSizeHint().height())


class GifExtractor():
    def __init__(self, video_file, window):
        self.video_file = video_file
        self.window = window
        self.count = 0
        self.init_ui()
        self.init_timestamps()
        self.init_frame_selectors()
        self.connect_signals()

    def init_ui(self):
        self.top_line_text_edit = self.window.ui.topLineTextEdit
        self.bottom_line_text_edit = self.window.ui.bottomLineTextEdit
        self.gif_name_edit = self.window.ui.gifNameLineEdit
        self.video_name_edit = self.window.ui.videoNameLineEdit
        self.extract_button = self.window.ui.extractButton
        self.video_combo_box = self.window.ui.videoComboBox
        self.gif_combo_box = self.window.ui.gifComboBox
        self.gif_box = HidableGifBox(self.gif_combo_box, self.window)
        self.gif_box.set_visibility(False)
        self.start_frame_ui = FrameSelectorUI(self.window.ui.startTimeLineEdit,
                                     self.window.ui.startFrameLabel,
                                     self.window.ui.previousStartFrameButton,
                                     self.window.ui.nextStartFrameButton)
        self.end_frame_ui = FrameSelectorUI(self.window.ui.endTimeLineEdit,
                                     self.window.ui.endFrameLabel,
                                     self.window.ui.previousEndFrameButton,
                                     self.window.ui.nextEndFrameButton)

    def init_timestamps(self):
        self.timestamps = Timestamps("timestamps.json")
        self.fill_video_box()

    def fill_video_box(self):
        self.video_combo_box.clear()
        self.video_combo_box.addItem("New Video")
        self.video_combo_box.addItems(self.timestamps.videos)

    def init_frame_selectors(self):
        self.start_frame_selector = FrameSelector(cv2.VideoCapture(self.video_file), self.start_frame_ui)
        self.end_frame_selector = FrameSelector(cv2.VideoCapture(self.video_file), self.end_frame_ui)

    def connect_signals(self):
        self.timestamps.updated.connect(self.fill_video_box)
        self.video_combo_box.currentTextChanged[str].connect(lambda str: self.load_video_gifs(str))
        self.gif_combo_box.currentTextChanged[str].connect(lambda str: self.load_gif_data(str))
        self.extract_button.clicked.connect(self.launch_extraction)
        self.gif_name_edit.returnPressed.connect(self.launch_extraction)

    def load_video_gifs(self, video_name):
        self.gif_box.fill_box(video_name, self.timestamps)

    def load_gif_data(self, gif_name):
        self.count += 1
        video_name = self.video_combo_box.currentText()
        if (video_name in self.timestamps.videos) and (gif_name in self.timestamps.gifs[video_name]):
            start_timestamp = self.timestamps.timestamps_data[video_name][gif_name]["start"]
            end_timestamp = self.timestamps.timestamps_data[video_name][gif_name]["end"]
            self.gif_name_edit.setText(gif_name)
            self.video_name_edit.setText(video_name)
        else:
            start_timestamp = "00:00:00:000"
            end_timestamp = "00:00:00:000"
            self.gif_name_edit.setText("")
            self.video_name_edit.setText("")
        self.adjust_gif_name_size()
        self.start_frame_ui.time_edit.setText(start_timestamp)
        self.start_frame_selector.new_frame()
        self.end_frame_ui.time_edit.setText(end_timestamp)
        self.end_frame_selector.new_frame()

    def adjust_gif_name_size(self):
        gif_name = self.gif_name_edit.text()
        font_metrics = QFontMetrics(self.gif_name_edit.font())
        width = font_metrics.width(gif_name)
        margin = 10
        self.gif_name_edit.setFixedWidth(max(self.gif_name_edit.minimumWidth(), width + margin))
        self.window.adjustSize();

    def launch_extraction(self):
        video = cv2.VideoCapture(self.video_file)
        start_timestamp = self.start_frame_selector.ui.time_edit.text()
        end_timestamp = self.end_frame_selector.ui.time_edit.text()
        top_line_text = self.top_line_text_edit.toPlainText()
        bottom_line_text = self.bottom_line_text_edit.toPlainText()
        gif_name = self.gif_name_edit.text()
        video_name = self.video_name_edit.text()

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

        timestamps_data = self.timestamps.timestamps_data
        if video_name not in timestamps_data:
            timestamps_data[video_name] = {}
        timestamps_data[video_name][gif_name] = {"start" : start_timestamp, "end" : end_timestamp}
        self.timestamps.write_timestamps_json(timestamps_data)

        print("Gif created: {}".format(gif_name))
        print("Start timestamp = {}".format(start_timestamp))
        print("End timestamp = {}".format(end_timestamp))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()

    gif_extractor = GifExtractor('./test_video.mp4', window)

    sys.exit(app.exec_())
