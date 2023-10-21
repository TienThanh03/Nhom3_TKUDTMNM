import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import Label
from tkinter import Entry
from tkinter import Button

selected_image = None  # Biến lưu trữ ảnh mà người dùng đã chọn

def open_image():
    global selected_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        selected_image = cv2.imread(file_path)
        cv2.imshow("Ảnh Gốc", selected_image)

def resize_image():
    if selected_image is not None:
        fx = float(resize_fx.get())
        fy = float(resize_fy.get())
        resized_image = cv2.resize(selected_image, (0, 0), fx=fx, fy=fy)
        cv2.imshow(f"Ảnh đã điều chỉnh kích thước fx={fx}, fy={fy}", resized_image)

def rotate_image():
    if selected_image is not None:
        angle = float(rotate_angle.get())
        img = selected_image
        rotate_matrix = cv2.getRotationMatrix2D(center=(img.shape[1] / 2, img.shape[0] / 2), angle=angle, scale=1.0)
        rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(img.shape[1], img.shape[0]))
        cv2.imshow('Ảnh Quay', rotated_image)

def grayscale_image():
    if selected_image is not None:
        img = selected_image
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Ảnh Đen Trắng", img_gray)

def edge_detection():
    if selected_image is not None:
        img = selected_image
        img = cv2.resize(img, (400, 300))
        edges = cv2.Canny(image=img, threshold1=500, threshold2=700)
        cv2.imshow("Phát Hiện Biên", edges)

root = tk.Tk()
root.title("Ứng dụng Xử lý Ảnh")

open_button = Button(root, text="Mở Ảnh", command=open_image)
open_button.pack()

Label(root, text="Điều chỉnh Kích Thước Ảnh").pack()
resize_fx = Entry(root)
resize_fx.pack()
resize_fy = Entry(root)
resize_fy.pack()
resize_button = Button(root, text="Điều chỉnh Kích Thước", command=resize_image)
resize_button.pack()

Label(root, text="Quay Ảnh").pack()
rotate_angle = Entry(root)
rotate_angle.pack()
rotate_button = Button(root, text="Quay Ảnh", command=rotate_image)
rotate_button.pack()

grayscale_button = Button(root, text="Chuyển thành Ảnh Đen Trắng", command=grayscale_image)
grayscale_button.pack()

edge_button = Button(root, text="Phát Hiện Biên", command=edge_detection)
edge_button.pack()

root.mainloop()
