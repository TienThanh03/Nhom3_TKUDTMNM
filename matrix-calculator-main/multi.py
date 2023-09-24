from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel, messagebox
from tkinter.constants import BOTH
import numpy as np
import menu

class Multi:
    def back_to_menu_from_output(self):
        self.gui_multi_output.destroy()
        menu.gui_menu.deiconify()

    def compute_product(self):
        try:
            # convert matrix_a and matrix_b to int
            for i in range(self.rows_a):
                for j in range(self.cols_a):
                    self.matrix_a[i][j] = int(self.matrix_a[i][j])

            for i in range(self.rows_b):
                for j in range(self.cols_b):
                    self.matrix_b[i][j] = int(self.matrix_b[i][j])

            # use np.matmul to achieve product
            self.product_matrix = np.matmul(self.matrix_a, self.matrix_b)
            return self.product_matrix
        except (TypeError, Exception):
            pass

        # try:
        #     # convert product_matrix back to str
        #     list_mat = [str(i) for i in self.product_matrix]

        #     # remove square brackets
        #     for i in range(len(list_mat)):
        #         list_mat[i] = list_mat[i][1:-1]

        #     # return product_matrix as a list of strings
        #     return list_mat

        # except (NameError, TypeError, Exception):
        #     Label(self.frame_multi_output, text="Ma trận của bạn").grid(row=1, column=self.cols_b * 2 + 10)
        #     Label(self.frame_multi_output, text="Không hợp lệ!").grid(row=2, column=self.cols_b * 2 + 10)

    def output_matrix(self):
        # create output window
        self.gui_multi_input.destroy()
        self.gui_multi_output = Toplevel()
        self.gui_multi_output.title("Multiply")
        self.gui_multi_output.resizable(False, False)

        # create output frame
        self.frame_multi_output = Frame(self.gui_multi_output, highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_multi_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

         #button
        self.frame_button = Frame(self.gui_multi_output, bg='#F9E79F', highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_button.pack(fill='x', expand=True, padx=5, pady=3)
        Button(self.frame_button, text="Back", font=('arial', 10, 'bold'), width=11, activebackground='green', command=self.back_to_input).grid(row=0, column=1, sticky='e', padx=14)
        Button(self.frame_button, text="Back to Menu", font=('arial', 10, 'bold'), activebackground='green', command=self.back_to_menu_from_output).grid(row=0, column=0, sticky='e', padx=14)
        Button(self.frame_button, text="Exit", font=('arial', 10, 'bold'), width=11, activebackground='green', command=exit).grid(row=0, column=2, sticky='e', padx=14)

        # display matrix_a input
        Label(self.frame_multi_output, text='Matrix A:', font=('arial', 14, 'bold'), underline=0).grid(row=0, column=0)

        for i in range(self.rows_a):
            for j in range(self.cols_a):
                Label(self.frame_multi_output, text=self.matrix_a[i][j], font=('arial', 12, 'bold'), bd=5).grid(row=i, column=j + 1, sticky='news', padx=5, pady=5)

        # display matrix_b input
        Label(self.frame_multi_output, text='Matrix B:', font=('arial', 14, 'bold'), underline=0).grid(row=0, column=self.cols_a + 1)

        for i in range(self.rows_b):
            for j in range(self.cols_b):
                Label(self.frame_multi_output, text=self.matrix_b[i][j], font=('arial', 12, 'bold'), bd=5).grid(row=i, column=j + self.cols_a + 2)

        # display product
        Label(self.frame_multi_output, text='Product:', font=('arial', 14, 'bold'), underline=0).grid(row=self.rows_a * 2, column=0)

        # compute product
        self.product_matrix = self.compute_product()

        # display product
        for i in range(self.rows_a):
            for j in range(self.cols_b):
                Label(self.frame_multi_output, text=self.product_matrix[i][j], font=('arial', 12, 'bold'), bd=5).grid(row=i + self.rows_a * 2, column=j + 1)

        # gui stuff
        self.gui_multi_output.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_output.mainloop()

    def back_to_input(self):
        self.gui_multi_output.destroy()
        self.input_matrix()

    def input_matrix(self):
        # create input window
        self.gui_multi_menu.destroy()
        self.gui_multi_input = Toplevel()
        self.gui_multi_input.title("Multiply")
        self.gui_multi_input.resizable(False, False)

        # create input frame
        self.frame_multi_input = Frame(self.gui_multi_input, bg='#F9E79F', highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_multi_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # create matrix A entries
        Label(self.frame_multi_input, text="Matrix A:", font=('arial', 12, 'bold'), bg='#F9E79F').grid(row=0, column=0)
        # to create matrix of entry cells we need to create a 2d list of entries
        # thank god to stackoverflow peeps for that

        # empty arrays for Entry and StringVars
        text_var = []
        entries = []

        # convert rows and cols from IntVar to int
        self.rows_a, self.cols_a = (self.ma_rows.get(), self.ma_cols.get())

        # create the list of entries with corresponding text_vars
        for i in range(self.rows_a):
            # append an empty list to append to later
            text_var.append([])
            entries.append([])
            for j in range(self.cols_a):
                # for column indications
                if i == 0:
                    Label(self.frame_multi_input, text=j + 1, bg='#F9E79F').grid(row=0, column=j + 1)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list
                entries[i].append(Entry(self.frame_multi_input, textvariable=text_var[i][j], width=10, font=('arial', 10, 'bold')))

                # display entry
                entries[i][j].grid(row=i + 1, column=j + 1)

                # for row indications
                Label(self.frame_multi_input, text=i + 1, bg='#F9E79F').grid(row=i + 1, column=0, sticky='e')

        Label(self.frame_multi_input, text="Matrix B:", font=('arial', 12, 'bold'), bg='#F9E79F').grid(row=self.rows_a + 1, column=0)

        text_var_b = []
        entries_b = []

        self.rows_b, self.cols_b = (self.ma_cols.get(), self.mb_cols.get())
        for i in range(self.rows_b):
            text_var_b.append([])
            entries_b.append([])
            for j in range(self.cols_b):
                if i == 0:
                    Label(self.frame_multi_input, text=j + 1, bg='#F9E79F').grid(row=self.rows_a + 1, column=j + 1)
                text_var_b[i].append(StringVar())
                entries_b[i].append(Entry(self.frame_multi_input, textvariable=text_var_b[i][j], width=10, font=('arial', 10, 'bold')))
                entries_b[i][j].grid(row=i + self.rows_a + 2, column=j + 1)
                Label(self.frame_multi_input, text=i + 1, bg='#F9E79F').grid(row=i + self.rows_a + 2, column=0, sticky='e')

        # callback functions to get StringVars/convert them to strings
        # and store in matrices
        def get_mat_a():
            self.matrix_a = []
            for i2 in range(self.rows_a):
                self.matrix_a.append([])
                for j2 in range(self.cols_a):
                    self.matrix_a[i2].append(text_var[i2][j2].get())

        def get_mat_b():
            self.matrix_b = []
            for i3 in range(self.rows_b):
                self.matrix_b.append([])
                for j3 in range(self.cols_b):
                    self.matrix_b[i3].append(text_var_b[i3][j3].get())

        def get_mat():
            try:
                get_mat_a()
                get_mat_b()
                self.output_matrix()
            except (ValueError, Exception):
                messagebox.showerror('Error', 'Ma trận của bạn không hợp lệ')

        self.frame_button = Frame(self.gui_multi_input,  bg='#F9E79F', highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_button.pack(fill='x', expand=True, padx=5, pady=3)
        Button(self.frame_button, text="Enter", font=('arial', 10, 'bold'), width=11, activebackground='green', command=get_mat).grid(row=0, column=2, padx=14)
        Button(self.frame_button, text="Back", font=('arial', 10, 'bold'), width=11, activebackground='green', command=self.back_to_dimensions).grid(row=0, column=1, padx=14)
        Button(self.frame_button, text="Back to Menu", font=('arial', 10, 'bold'),activebackground='green', command=self.back_to_menu_from_input).grid(row=0, column=0, padx=14)

        # gui stuff
        self.gui_multi_input.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_input.mainloop()

    def back_to_menu_from_input(self):
        self.gui_multi_input.destroy()
        menu.gui_menu.deiconify()

    def back_to_dimensions(self):
        self.gui_multi_input.destroy()
        self.__init__()
    
    def __init__(self):
        def update_label(*args):
            selected_value.set(self.ma_cols.get())
        # pre-declare variables
        self.product_matrix = None
        self.matrix_a, self.matrix_b = None, None
        self.matrix = None
        self.gui_multi_input = None
        self.frame_multi_input = None
        self.rows_a, self.cols_a = None, None
        self.rows_b, self.cols_b = None, None
        self.gui_multi_output = None
        self.frame_multi_output = None

        # create sub-menu window then withdraw main menu window
        menu.gui_menu.withdraw()
        self.gui_multi_menu = Toplevel()
        self.gui_multi_menu.title("Multiply")
        self.gui_multi_menu.resizable(False, False)

        # create sub-menu frame
        self.frame_multi_menu = Frame(self.gui_multi_menu, highlightbackground='black', highlightthickness=1, bg='#F9E79F', padx=5, pady=5)
        self.frame_multi_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # inputs Label(self.frame_multi_menu, text='NOTE: Matrix A height and Matrix B length').grid(row=1, column=1,
        # column span =6) Label(self.frame_multi_menu, text='...are to be equal for multiplication').grid(row=2,
        # column=1, column span =6) A matrix

        # prompt dimensions
        Label(self.frame_multi_menu, text='Matrix A dimensions:', font=('arial', 14, 'bold'), bg='#F9E79F').grid(row=0, column=0, columnspan=3, sticky='news', pady=10)
        Label(self.frame_multi_menu, text='Matrix B dimensions:', font=('arial', 14, 'bold'), bg='#F9E79F').grid(row=2, column=0, columnspan=3, sticky='news', pady=10)

        # create var for rows
        self.ma_rows = IntVar()
        self.ma_rows.set(2)

        # drop down for rows
        OptionMenu(self.frame_multi_menu, self.ma_rows, *range(1, 5)).grid(row=1, column=0, sticky='ew', pady=10)

        # 'x'
        Label(self.frame_multi_menu, text='x', bg='#F9E79F', font=('arial', 14, 'bold')).grid(row=1, column=1)
        selected_value = StringVar()
        selected_value.set(2)
        # create var for cols
        self.ma_cols = IntVar()
        self.ma_cols.set(2)
        # self.ma_cols.trace_add("write", update_label)
        OptionMenu(self.frame_multi_menu, self.ma_cols, *range(1, 5)).grid(row=1, column=2, sticky='ew')
        self.ma_cols.trace_add("write", update_label)
        # B matrix
        self.mb_rows = IntVar()
        # self.mb_rows.set(self.ma_cols.get())
        
        label=Label(self.frame_multi_menu, textvariable=selected_value, font=('arial', 10, 'bold'), padx=5, pady=5, bg='#F9E79F').grid(row=3, column=0)
         
        
        # OptionMenu(self.frame_multi_menu, self.mb_rows, *range(2, 16)).grid(row=2, column=2)

        Label(self.frame_multi_menu, text='x', bg='#F9E79F', font=('arial', 14, 'bold')).grid(row=3, column=1)

        self.mb_cols = IntVar()
        self.mb_cols.set(2)
        OptionMenu(self.frame_multi_menu, self.mb_cols, *range(1, 5)).grid(row=3, column=2, sticky='ew')

        # in order to move to input window
        Button(self.frame_multi_menu, text='Enter', font=('arial', 10, 'bold'), activebackground='green', padx=10, pady=5, command=self.input_matrix).grid(row=4, column=0, columnspan=3, pady=10)
        Button(self.frame_multi_menu, text="Back to Menu", font=('arial', 10, 'bold'), activebackground='green', pady=10, padx=5, command=self.back_to_menu_from_dimensions).grid(row=5, column=0, columnspan=3)

        # gui stuff
        self.gui_multi_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_menu.mainloop()

    def back_to_menu_from_dimensions(self):
        self.gui_multi_menu.destroy()
        menu.gui_menu.deiconify()
