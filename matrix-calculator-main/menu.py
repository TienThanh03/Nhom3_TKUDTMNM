from tkinter import Tk, Label, Button, Frame
from tkinter.constants import BOTH
import inverse
import multi
import trans
import add

gui_menu = Tk()
gui_menu.geometry('700x550')
gui_menu.title('Matrix Calculator')
frame_menu = Frame(gui_menu, highlightbackground='black', bg='#F9E79F', highlightthickness=1)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)


class Menu:
    def __init__(self):
        label = Label(frame_menu, text="Chọn Phép Toán:", bg='#F9E79F', width=50, height=3, font=('arial', 16, 'bold'))
        inv = Button(frame_menu, text="Nghịch đảo", bg='#ADFF2F', font=('arial', 14, 'bold'), activebackground='green', width=50, height=3, command=inverse.Inverse)
        ad = Button(frame_menu, text="Cộng", font=('arial', 14, 'bold'), activebackground='green', width=50, height=3, command=add.Add)
        tran = Button(frame_menu, text="Chuyển vị", bg='#ADFF2F', font=('arial', 14, 'bold'), activebackground='green', width=50, height=3, command=trans.Trans)
        mlt = Button(frame_menu, text="Nhân", font=('arial', 14, 'bold'), activebackground='green', width=50, height=3, command=multi.Multi)
        Exit = Button(frame_menu, text="Exit",bg='#ADFF2F', font=('arial', 14, 'bold'), activebackground='green', width=50, height=3, command=exit)
        
        label.pack(fill=BOTH)
        inv.pack()
        ad.pack()
        tran.pack()
        mlt.pack()
        Exit.pack()

        # def on_closing():
        #      if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #         gui_menu.destroy()
        # gui_menu.protocol("WM_DELETE_WINDOW", on_closing)

        gui_menu.mainloop()
