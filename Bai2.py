import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Định nghĩa các kernel
kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
kernel_sharpen_2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, 2, 8, 2, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, -1, -1, -1, -1]]) / 8.0

def open_image():
    global img
    global original_img
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img = cv2.resize(img, (500, 500))
    original_img = img.copy()
    cv2.imshow('Ảnh Gốc', original_img)

def update_sharpness_and_brightness(kernel):
    global img
    sharpness = sharpness_var.get()
    brightness = brightness_var.get()
    sharpened = cv2.filter2D(img, -1, kernel * sharpness)
    adjusted_brightness = cv2.convertScaleAbs(sharpened, alpha=brightness, beta=0)
    cv2.imshow('Ảnh Sắc nét và Độ Sáng', adjusted_brightness)

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    cv2.imwrite(file_path, adjusted_brightness)

def reset_image():
    global img
    img = original_img.copy()
    sharpness_slider.set(1.0)
    brightness_slider.set(1.0)
    cv2.imshow('Ảnh Sắc nét và Độ Sáng', img)

def equalize_histogram():
    global img
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized_img = cv2.equalizeHist(img_gray)
    colored_equalized_img = cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGR)
    cv2.imshow('Ảnh Cân bằng Histogram', colored_equalized_img)

root = tk.Tk()
root.title("Ứng dụng Xử lý Ảnh")

btn_open = tk.Button(root, text="Mở Ảnh", command=open_image)
btn_open.pack(pady=10)

sharpness_var = tk.DoubleVar()
sharpness_slider = ttk.Scale(root, from_=0.1, to=5.0, variable=sharpness_var, orient="horizontal", length=200)
sharpness_slider.pack(pady=10)
sharpness_slider.set(1.0)

brightness_var = tk.DoubleVar()
brightness_slider = ttk.Scale(root, from_=0.1, to=5.0, variable=brightness_var, orient="horizontal", length=200)
brightness_slider.pack(pady=10)
brightness_slider.set(1.0)

btn_sharpen_1 = tk.Button(root, text="Kernel 1", command=lambda: update_sharpness_and_brightness(kernel_sharpen_1))
btn_sharpen_1.pack(pady=5)

btn_sharpen_2 = tk.Button(root, text="Kernel 2", command=lambda: update_sharpness_and_brightness(kernel_sharpen_2))
btn_sharpen_2.pack(pady=5)

btn_sharpen_3 = tk.Button(root, text="Kernel 3", command=lambda: update_sharpness_and_brightness(kernel_sharpen_3))
btn_sharpen_3.pack(pady=5)

btn_reset = tk.Button(root, text="Đặt lại Ảnh", command=reset_image)
btn_reset.pack(pady=5)

btn_save = tk.Button(root, text="Lưu Ảnh", command=save_image)
btn_save.pack(pady=10)

btn_equalize = tk.Button(root, text="Cân bằng Histogram", command=equalize_histogram)
btn_equalize.pack(pady=5)

def zoom_in():
    global img
    img = cv2.resize(img, (img.shape[1] + 50, img.shape[0] + 50))
    cv2.imshow('Ảnh Sắc nét và Độ Sáng', img)

def zoom_out():
    global img
    img = cv2.resize(img, (img.shape[1] - 50, img.shape[0] - 50))
    cv2.imshow('Ảnh Sắc nét và Độ Sáng', img)

btn_zoom_in = tk.Button(root, text="Phóng to", command=zoom_in)
btn_zoom_in.pack(pady=5)

btn_zoom_out = tk.Button(root, text="Thu nhỏ", command=zoom_out)
btn_zoom_out.pack(pady=5)

root.mainloop()
