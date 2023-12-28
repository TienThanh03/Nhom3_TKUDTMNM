from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT, BOTH
import cv2


class AdjustFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        #self.brightness_value = 0
        #self.previous_brightness_value = 0

        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image

        # self.brightness_label = Label(self, text="Brightness")
        # self.brightness_scale = Scale(self, background="LightGoldenrod4", from_=0, to_=2,troughcolor="LightGoldenrod3", length=250, resolution=0.1,
        #                               orient=HORIZONTAL)
        # self.r_label = Label(self, text="Red")
        # self.r_scale = Scale(self,background="red4", from_=-100, to_=100,troughcolor="coral1", length=250, resolution=1,
        #                      orient=HORIZONTAL)
        # self.g_label = Label(self, text="Green")
        # self.g_scale = Scale(self, background="dark green",from_=-100, to_=100,troughcolor="sea green", length=250, resolution=1,
        #                      orient=HORIZONTAL)
        # self.b_label = Label(self, text="Blue")
        # self.b_scale = Scale(self, background="midnight blue",from_=-100, to_=100,troughcolor="slate blue", length=250, resolution=1,
        #                      orient=HORIZONTAL)
        self.s_label = Label(self, font=("arial bold", 10), text="Độ bão hòa")
        self.s_scale = Scale(self, background="#ccc", from_=-100, to=100, troughcolor="#f5eaab",
                             length=250, resolution=1, orient=HORIZONTAL)
        self.v_label = Label(self, font=("arial bold", 10), text="Độ sáng")
        self.v_scale = Scale(self, background="#ccc", from_=-100, to=100, troughcolor="#f5eaab",
                             length=250, resolution=1, orient=HORIZONTAL)

        self.apply_button = Button(self, font=("arial bold", 10), text="Áp dụng", activebackground='green')
        self.preview_button = Button(self, font=("arial bold", 10), text="Xem trước", activebackground='green')
        self.cancel_button = Button(self, font=("arial bold", 10), text="Thoát", activebackground='green')

        #self.brightness_scale.set(1)

        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.preview_button.bind("<ButtonRelease>", self.show_button_release)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        # self.brightness_label.pack()
        # self.brightness_scale.pack()
        # self.r_label.pack()
        # self.r_scale.pack()
        # self.g_label.pack()
        # self.g_scale.pack()
        # self.b_label.pack()
        # self.b_scale.pack()
        # self.cancel_button.pack(side=RIGHT)
        # self.preview_button.pack(side=RIGHT)
        # self.apply_button.pack()
        self.s_label.pack(fill=BOTH)
        self.s_scale.pack(fill=BOTH)
        self.v_label.pack(fill=BOTH)
        self.v_scale.pack(fill=BOTH)
        self.cancel_button.pack(side=RIGHT, padx=10, pady=5)
        self.preview_button.pack(side=RIGHT, padx=10, pady=5)
        self.apply_button.pack(side=RIGHT, padx=10, pady=5)

    def apply_button_released(self, event):
        self.master.undo_save = self.master.processed_image
        self.master.u.append(self.master.undo_save)

        self.master.processed_image = self.processing_image
        self.close()

    # def show_button_release(self, event):
    #     self.processing_image = cv2.convertScaleAbs(self.original_image, alpha=self.brightness_scale.get())
    #     b, g, r = cv2.split(self.processing_image)
    #
    #     for b_value in b:
    #         cv2.add(b_value, self.b_scale.get(), b_value)
    #     for g_value in g:
    #         cv2.add(g_value, self.g_scale.get(), g_value)
    #     for r_value in r:
    #         cv2.add(r_value, self.r_scale.get(), r_value)
    #
    #     self.processing_image = cv2.merge((b, g, r))
    #     self.show_image(self.processing_image)

    def show_button_release(self, event):
        #self.processing_image = cv2.convertScaleAbs(self.original_image, alpha=self.brightness_scale.get())
        self.processing_image = cv2.cvtColor(self.processing_image, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(self.processing_image)

        # for h_value in h:
        #     cv2.add(h_value, self.h_scale.get(), h_value)
        for s_value in s:
            cv2.add(s_value, self.s_scale.get(), s_value)
        for v_value in v:
            cv2.add(v_value, self.v_scale.get(), v_value)

        self.processing_image = cv2.merge((h, s, v))
        self.processing_image = cv2.cvtColor(self.processing_image, cv2.COLOR_HSV2RGB)
        self.show_image(self.processing_image)

    def cancel_button_released(self, event):
        self.close()

    def show_image(self, img=None):
        self.master.image_viewer.show_image(img=img)

    def close(self):
        self.show_image()
        self.destroy()


