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

def update_sharpness_and_brightness(kernel):
    global img
    sharpness = sharpness_var.get()
    brightness = brightness_var.get()
    sharpened = cv2.filter2D(img, -1, kernel * sharpness)
    adjusted_brightness = cv2.convertScaleAbs(sharpened, alpha=brightness, beta=0)
    cv2.imshow('Sharpened and Brightened Image', adjusted_brightness
               root = tk.Tk()
root.title("Ứng dụng Tăng cường Sắc nét và Độ Sáng Ảnh")

btn_open = tk.Button(root, text="Chọn Ảnh", command=open_image)
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


window.mainloop()
