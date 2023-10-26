from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

window = Tk()
window.title("Chọn ảnh")
window.geometry("400x400")
img = None

def open_file():
    global img
    file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.jpg *.png *.gif")])
    print(file_path)
    if file_path:
        img = cv2.imread(file_path)
        show_image(img)

def show_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

def save_blurred_image():
    global img
    blurred = cv2.GaussianBlur(img, (11, 11), 0)
    show_image(blurred)
    cv2.imwrite("blurred_image.jpg", blurred)

def sharpen_image():
    global img
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    sharpened = cv2.filter2D(img, -1, kernel)
    show_image(sharpened)
    cv2.imwrite("sharpened_image.jpg", sharpened)

def crop_image():
    global img
    roi = cv2.selectROI(img)
    x, y, w, h = roi
    cropped_image = img[y:y + h, x:x + w]
    show_image(cropped_image)

label = Label(window)
label.pack()

button = Button(window, text="Chọn ảnh", command=open_file)
button.pack(pady=10)

button_blur = Button(window, text="Làm mờ ảnh", command=save_blurred_image)
button_blur.pack(pady=10)

button_sharpen = Button(window, text="Làm nét ảnh", command=sharpen_image)
button_sharpen.pack(pady=10)

button_crop = Button(window, text="Cắt ảnh", command=crop_image)
button_crop.pack(pady=10)

window.mainloop()
