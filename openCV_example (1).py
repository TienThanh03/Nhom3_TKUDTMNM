# lựa chọn ảnh trước khi tạo các ảnh mới
# khuyến nghị lựa chọn ảnh có kích thước nhỏ hơn 700x700

import cv2
import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QFileDialog
from PyQt6.QtGui import QImage, QPixmap, QImageReader
from PyQt6.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image App")
        self.setGeometry(0, 0, 2160, 720)

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_select_image = QPushButton("Chọn hình ảnh", self)
        self.btn_histogram = QPushButton("Histogram", self)
        self.btn_gray = QPushButton("Tạo ảnh xám", self)
        self.btn_flip = QPushButton("Lật ảnh", self)
        self.btn_rotate = QPushButton("Xoay ảnh")
        self.btn_cartoon = QPushButton("Tạo ảnh cartoon", self)

        self.btn_select_image.clicked.connect(self.open_file_dialog)
        self.btn_histogram.clicked.connect(self.plot_histogram)
        self.btn_gray.clicked.connect(self.create_gray_image)
        self.btn_flip.clicked.connect(self.create_flip_image)
        self.btn_rotate.clicked.connect(self.create_rotate_image)
        self.btn_cartoon.clicked.connect(self.create_cartoon_image)

        left_layout = QVBoxLayout()
        right_layout = QGridLayout()
        left_layout.addWidget(self.image_label)
        right_layout.addWidget(self.btn_select_image)
        right_layout.addWidget(self.btn_histogram)
        right_layout.addWidget(self.btn_gray)
        right_layout.addWidget(self.btn_flip)
        right_layout.addWidget(self.btn_rotate)
        right_layout.addWidget(self.btn_cartoon)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)


        self.central_widget.setLayout(main_layout)

        self.filename = None
        self.count = 0
        self.rotate = False
        self.flipped = False
        self.gray = False

    def open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'C:\images')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                for filename in filenames:
                    self.filename = str(Path(filename))
                    self.image_label.setPixmap(QPixmap(filename))

    def plot_histogram(self):
        image = cv2.imread(self.filename)
        # Chia hình ảnh thành các kênh tương ứng, sau đó khởi tạo
        # Tuple tên kênh cùng với hình để vẽ đồ thị
        chans = cv2.split(image)
        colors = ("b", "g", "r")
        plt.figure()
        plt.title("Histogram for Original Image")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        # Vòng lặp các kênh hình ảnh
        for (chan, color) in zip(chans, colors):
            # Tạo biểu đồ cho kênh hiện tại và vẽ sơ đồ đó
            hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
            plt.plot(hist, color=color)
            plt.xlim([0, 256])
        # Hiển thị biểu đồ
        plt.show()

    def create_gray_image(self):
        image = cv2.imread(self.filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if self.gray:
            cv2.imshow('Gray image', image)
        else:
            # Hiển thị ảnh xám
            cv2.imshow('Gray image', gray)
        self.gray = not self.gray
    
    def create_flip_image(self):
        image = cv2.imread(self.filename)
        if self.flipped:
            cv2.imshow('Flip image', image)
        else:
            # Lật ảnh theo chiều Y
            flipped_img = cv2.flip(image, 1)
            cv2.imshow('Flip image', flipped_img)
        self.flipped = not self.flipped
    
    def create_rotate_image(self):
        image = cv2.imread(self.filename)
        rotated_img = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotate image', rotated_img)
    
    def create_cartoon_image(self):
        image = cv2.imread(self.filename, cv2.IMREAD_UNCHANGED) # trả về ảnh bao gồm cả kênh alpha (có độ trong suốt)
        cv2.imshow("test",image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurImage = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(blurImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask = edges)
        # Hiển thị ảnh cartoon
        cv2.imshow("Cartoon image", cartoon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec())