from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

window = Tk()
window.title("Chọn ảnh")
window.geometry("300x200")
img = None


def open_file():
    global img
    file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.jpg *.png *.gif")])
    print(file_path)
    if file_path:
        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)
        label = Label(window, image=img)
        label.pack()

        img = cv2.imread(file_path)
        roi = cv2.selectROI(img)
        x, y, w, h = roi
        blurred = cv2.GaussianBlur(img[y:y + h, x:x + w], (11, 11), 0)
        img[y:y + h, x:x + w] = blurred
        cv2.imshow('Blurred Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


button = Button(window, text="Chọn ảnh", command=open_file)
button.pack(pady=10)

window.mainloop()