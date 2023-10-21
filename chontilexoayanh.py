import cv2
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QInputDialog, QSlider, QGridLayout
from PyQt6.QtGui import QPixmap, QImage, QImageReader
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
        self.btn_rotate_left = QPushButton("Xoay trái", self)
        self.btn_rotate_right = QPushButton("Xoay phải", self)
        self.btn_flip_upside_down = QPushButton("Úp ngược ảnh", self)
        self.btn_cartoon = QPushButton("Tạo ảnh cartoon", self)
        self.btn_rotate_custom = QPushButton("Xoay theo góc tùy chỉnh", self)

        self.btn_select_image.clicked.connect(self.open_file_dialog)
        self.btn_histogram.clicked.connect(self.plot_histogram)
        self.btn_gray.clicked.connect(self.create_gray_image)
        self.btn_flip.clicked.connect(self.create_flip_image)
        self.btn_cartoon.clicked.connect(self.create_cartoon_image)
        self.btn_rotate_custom.clicked.connect(self.rotate_custom_image)

        left_layout = QVBoxLayout()
        right_layout = QGridLayout()
        left_layout.addWidget(self.image_label)
        right_layout.addWidget(self.btn_select_image, 0, 0)
        right_layout.addWidget(self.btn_histogram, 1, 0)
        right_layout.addWidget(self.btn_gray, 2, 0)
        right_layout.addWidget(self.btn_flip, 3, 0)
        right_layout.addWidget(self.btn_rotate_left, 4, 0)
        right_layout.addWidget(self.btn_rotate_right, 5, 0)
        right_layout.addWidget(self.btn_flip_upside_down, 6, 0)
        right_layout.addWidget(self.btn_cartoon, 7, 0)
        right_layout.addWidget(self.btn_rotate_custom, 8, 0)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(right_layout)

        self.central_widget.setLayout(main_layout)

        self.filename = None
        self.count = 0
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
        chans = cv2.split(image)
        colors = ("b", "g", "r")
        plt.figure()
        plt.title("Histogram for Original Image")
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        for (chan, color) in zip(chans, colors):
            hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
            plt.plot(hist, color=color)
            plt.xlim([0, 256])
        plt.show()

    def create_gray_image(self):
        image = cv2.imread(self.filename)
        gray = cv2.cvtColor(image, cv2.ColorConversionCodes.COLOR_BGR2GRAY)
        if self.gray:
            cv2.imshow('Gray image', image)
        else:
            cv2.imshow('Gray image', gray)
        self.gray = not self.gray

    def create_flip_image(self):
        image = cv2.imread(self.filename)
        if self.flipped:
            cv2.imshow('Flip image', image)
        else:
            flipped_img = cv2.flip(image, 1)
            cv2.imshow('Flip image', flipped_img)
        self.flipped = not self.flipped

    def create_rotate_left_image(self):
        image = cv2.imread(self.filename)
        rotated_img = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow('Rotate Left image', rotated_img)

    def create_rotate_right_image(self):
        image = cv2.imread(self.filename)
        rotated_img = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotate Right image', rotated_img)

    def create_flip_upside_down_image(self):
        image = cv2.imread(self.filename)
        flipped_img = cv2.flip(image, 0)
        cv2.imshow('Flip Upside Down image', flipped_img)

    def rotate_custom_image(self):
        if not self.filename:
            return

        degree, ok = QInputDialog.getDouble(self, "Xoay ảnh theo góc", "Nhập góc xoay (độ):", value=0, min=0)
        if ok:
            image = cv2.imread(self.filename)
            height, width = image.shape[:2]
            rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
            rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
            cv2.imshow("Rotated Image", rotated_image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec())