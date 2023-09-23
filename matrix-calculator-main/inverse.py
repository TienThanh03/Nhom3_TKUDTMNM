from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel
from tkinter.constants import BOTH
from numpy.linalg import inv
import menu

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Inverse:
    def back_to_menu_from_output(self):
        self.gui_inverse_output.destroy()
        menu.gui_menu.deiconify() # đưa cửa sổ bị ẩn hoặc thu nhỏ hiển thị trở lại

    def compute_inverse(self):
        # convert matrix of strings to integers
        try:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] = int(self.matrix[i][j])

        except (NameError, TypeError, Exception):
            # Label(self.frame_inverse_output, text="Invalid input(s)").grid(row=1, column=2)
            pass

        try:
            # invert matrix then convert back to string
            self.matrix = inv(self.matrix)
            list_mat = [str(i) for i in self.matrix]

            # remove square brackets
            for i in range(len(list_mat)):
                list_mat[i] = list_mat[i][1:-1]
            return list_mat

        except (TypeError, Exception):
            pass
            # Label(self.frame_inverse_output, text="Ma trận của bạn", font=('arial', 12, 'bold'), bg='red').grid(row=1, column=self.cols * 2 + 1)
            # Label(self.frame_inverse_output, text="Không hợp lệ!", font=('arial', 12, 'bold'), bg='red').grid(row=2, column=self.cols * 2 + 1)

    def output_matrix(self):
        # create window
        self.gui_inverse_input.destroy()
        self.gui_inverse_output = Toplevel() # tạo ra một cửa sổ mới
        self.gui_inverse_output.title("Matrix Calculator")

        self.frame_inverse_output = Frame(self.gui_inverse_output, highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_inverse_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # display user input
        Label(self.frame_inverse_output, text='Input:', font=('arial', 12, 'bold'), underline=0).grid(row=0, column=0)
        for i in range(self.rows):
            for j in range(self.cols):
                Label(self.frame_inverse_output, text=self.matrix[i][j], font=('arial', 12, 'bold'), bd=5).grid(row=i, column=j + 1, sticky='news', padx=5, pady=5)

        # display output
        Label(self.frame_inverse_output, text='Inverted:', font=('arial', 12, 'bold'), underline=0).grid(row=0, column=self.cols + 2)

        inverse_matrix = self.compute_inverse()
        for i in range(self.rows):
            Label(self.frame_inverse_output, text=inverse_matrix[i], font=('arial', 12, 'bold'), bd=5).grid(row=i, column=self.cols + 3, sticky='news', padx=5, pady=5)

        self.frame_button = Frame(self.gui_inverse_output, bg='#F9E79F', highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_button.pack(fill='x', expand=True, padx=5, pady=5)
        Button(self.frame_button, text="Back", font=('arial', 10, 'bold'), width=11, activebackground='green', command=self.back_to_input).grid(row=0, column=1, sticky='e', padx=14)
        Button(self.frame_button, text="Back to Menu", font=('arial', 10, 'bold'), activebackground='green', command=self.back_to_menu_from_output).grid(row=0, column=0, sticky='e', padx=14)
        Button(self.frame_button, text="Exit", font=('arial', 10, 'bold'), width=11, activebackground='green', command=exit).grid(row=0, column=2, sticky='e', padx=14)

        self.gui_inverse_output.protocol("WM_DELETE_WINDOW", self.back_to_input)
        self.gui_inverse_output.mainloop()

    def back_to_input(self):
        self.gui_inverse_output.destroy()
        self.input_matrix()

    def input_matrix(self):
        self.gui_inverse_menu.destroy()
        self.gui_inverse_input = Toplevel()
        self.gui_inverse_input.title("Matrix Calculator")

        self.frame_inverse_input = Frame(self.gui_inverse_input, bg='#F9E79F', highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_inverse_input.pack(fill=BOTH, expand=True, padx=5)

        Label(self.frame_inverse_input, text="Matrix:", bg='#F9E79F', font=('arial', 12, 'bold')).grid(row=0, column=0, sticky='news')

        # to create matrix of entry cells we need to create a 2d list of entries
        # thank god to stackoverflow peeps for that

        # empty arrays for Entry and StringVars
        text_var = []
        entries = []

        self.rows, self.cols = (self.m_dimensions.get(), self.m_dimensions.get())
        for i in range(self.rows):
            # append an empty list to arrays to append to later
            text_var.append([])
            entries.append([])
            for j in range(self.cols):
                # for column indications
                if i == 1:
                    Label(self.frame_inverse_input, text=j + 1, bg='#F9E79F').grid(row=0, column=j + 1)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list
                entries[i].append(Entry(self.frame_inverse_input, textvariable=text_var[i][j], width=10, font=('arial', 10, 'bold')))

                # display entry
                entries[i][j].grid(row=i + 1, column=j + 1)

                # for row indications
                Label(self.frame_inverse_input, text=i + 1, bg='#F9E79F').grid(row=i + 1, column=0, sticky='e')

        # callback function to get StringVars/convert them to strings
        # and store in matrix[]
        def get_mat():
            try:
                self.matrix = []
                for i2 in range(self.rows):
                    self.matrix.append([])
                    for j2 in range(self.cols):
                        self.matrix[i2].append(text_var[i2][j2].get())
                self.output_matrix()

            except (ValueError, Exception):
                Label(self.frame_inverse_output, text="Ma trận của bạn").grid(row=1, column=self.cols * 2 + 1)
                Label(self.frame_inverse_output, text="không hợp lệ!").grid(row=2, column=self.cols * 2 + 1)  
        
        self.frame_button = Frame(self.gui_inverse_input, bg='#F9E79F', highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_button.pack(fill='x', expand=True, padx=5, pady=5)
        Button(self.frame_button, text="Enter", font=('arial', 10, 'bold'), width=11, activebackground='green', command=get_mat).grid(row=0, column=2, sticky='e', padx=14)
        Button(self.frame_button, text="Back", font=('arial', 10, 'bold'), width=11, activebackground='green', command=self.back_to_dimensions).grid(row=0, column=1, sticky='e', padx=14)
        Button(self.frame_button, text="Back to Menu", font=('arial', 10, 'bold'), activebackground='green', command=self.back_to_menu_from_input).grid(row=0, column=0, sticky='e', padx=14)

        self.gui_inverse_input.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_inverse_input.mainloop()

    def back_to_dimensions(self):
        self.gui_inverse_input.destroy()
        self.__init__()

    def back_to_menu_from_input(self):
        self.gui_inverse_input.destroy()
        menu.gui_menu.deiconify()

    def __init__(self):
        self.gui_inverse_input, self.gui_inverse_output = None, None
        self.frame_inverse_output, self.frame_inverse_input = None, None
        self.frame_inverse_menu = None
        self.inverse_matrix = []
        self.rows, self.cols = None, None
        self.matrix = None

        menu.gui_menu.withdraw() # loại bỏ cửa sổ menu
        self.gui_inverse_menu = Toplevel()
        self.gui_inverse_menu.title("Inverse")
        self.gui_inverse_menu.geometry('400x300')
        self.gui_inverse_menu.resizable(False, False)

        self.frame_inverse_menu = Frame(self.gui_inverse_menu, highlightbackground='black', padx=5, pady=5, bg='#F9E79F', highlightthickness=1)
        self.frame_inverse_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_inverse_menu, text='Enter matrix dimensions:', font=('arial', 14, 'bold'), bg='#F9E79F').pack(fill=BOTH, pady=10)

        # enter matrix dimensions
        self.m_dimensions = IntVar()
        self.m_dimensions.set(2)
        OptionMenu(self.frame_inverse_menu, self.m_dimensions, *range(2, 5)).pack(fill=BOTH, pady=10, padx=5)
        Button(self.frame_inverse_menu, text='Enter', font=('arial', 10, 'bold'), activebackground='green', padx=10, pady=5, command=self.input_matrix).pack(pady=20)

        #BACK TO MENU
        Button(self.frame_inverse_menu, text="Back to Menu", font=('arial', 10, 'bold'), activebackground='green', padx=10, pady=5, command=self.back_to_menu_from_dimension).pack()

        self.gui_inverse_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy) # xóa cửa sổ và thuộc tính của cửa sổ menu
        self.gui_inverse_menu.mainloop()

    def back_to_menu_from_dimension(self):
        self.gui_inverse_menu.destroy()
        menu.gui_menu.deiconify()
