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

        kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        kernel_sharpen_2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
        kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                                    [-1, 2, 2, 2, -1],
                                    [-1, 2, 8, 2, -1],
                                    [-1, 2, 2, 2, -1],
                                    [-1, -1, -1, -1, -1]]) / 8.0

        # applying different kernels to the input image
        image = cv2.imread(file_path)
        cv2.imshow('Original', image)
        output_1 = cv2.filter2D(image, -1, kernel_sharpen_1)
        output_2 = cv2.filter2D(image, -1, kernel_sharpen_2)
        output_3 = cv2.filter2D(image, -1, kernel_sharpen_3)
        cv2.imshow('Sharpening', output_1)
        cv2.imshow('Excessive Sharpening', output_2)
        cv2.imshow('Edge Enhancement', output_3)
        cv2.waitKey(0)

        cv2.destroyAllWindows()


button = Button(window, text="Chọn ảnh", command=open_file)
button.pack(pady=10)

window.mainloop()