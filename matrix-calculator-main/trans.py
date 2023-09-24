from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel, messagebox, Canvas, Scrollbar
from tkinter.constants import BOTH, VERTICAL, HORIZONTAL
import numpy as np
import menu

class Trans:
    def back_to_menu_from_output(self):
        self.gui_trans_output.destroy()
        menu.gui_menu.deiconify()

    def compute_transpose(self):
        try:
            for i in range(self.rows_get):
                for j in range(self.cols_get):
                    self.matrix[i][j] = int(self.matrix[i][j])
            self.trans_matrix = np.transpose(self.matrix)
            return self.trans_matrix
        except:
            pass

    def output_matrix(self):
        self.gui_trans_input.destroy()
        self.gui_trans_output = Toplevel()
        self.gui_trans_output.title("Chuyển vị")
        self.gui_trans_output.resizable(False, False)

        self.frame_trans_output = Frame(self.gui_trans_output, highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_trans_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # button
        self.frame_button = Frame(self.gui_trans_output, bg='#F9E79F', highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_button.pack(fill='x', expand=True, padx=5, pady=3)
        Button(self.frame_button, text="Back", font=('arial', 10, 'bold'), width=11, activebackground='green', command=self.back_to_input).grid(row=0, column=1, sticky='e', padx=14)
        Button(self.frame_button, text="Back to Menu", font=('arial', 10, 'bold'), activebackground='green', command=self.back_to_menu_from_output).grid(row=0, column=0, sticky='e', padx=14)
        Button(self.frame_button, text="Exit", font=('arial', 10, 'bold'), width=11, activebackground='green', command=exit).grid(row=0, column=2, sticky='e', padx=14)

        Label(self.frame_trans_output, text='Ma trận đã nhập:', font=('arial', 14, 'bold'), underline=0).grid(row=0, column=0, sticky='W')

        ############
        canvas_input = Canvas(self.frame_trans_output, width=700, height=200)
        canvas_input.grid(row=1, column=0, padx=5, pady=5, columnspan=self.cols_get + 1)
        v_scrollbar_input = Scrollbar(self.frame_trans_output, orient=VERTICAL, command=canvas_input.yview)
        v_scrollbar_input.grid(row=1, column=self.cols_get + 2, sticky='ns')
        h_scrollbar_input = Scrollbar(self.frame_trans_output, orient=HORIZONTAL, command=canvas_input.xview)
        h_scrollbar_input.grid(row=self.rows_get + 1, column=0, sticky='ew')
        canvas_input.configure(yscrollcommand=v_scrollbar_input.set, xscrollcommand=h_scrollbar_input.set)

        frame_matrix_input = Frame(canvas_input)
        canvas_input.create_window((0, 0), window=frame_matrix_input, anchor='nw')

        for i in range(self.rows_get):
            for j in range(self.cols_get):
                Label(frame_matrix_input, text=self.matrix[i][j], font=('arial', 12, 'bold'), bd=5).grid(row=i, column=j, padx=5, pady=5, sticky='news')

        frame_matrix_input.update_idletasks()
        canvas_input.config(scrollregion=canvas_input.bbox("all"))

        Label(self.frame_trans_output, text='Ma trận cần tìm:', font=('arial', 14, 'bold'), underline=0).grid(row=self.rows_get + 6, column=0, sticky='W')

        self.transposed_matrix = self.compute_transpose()

        ################
        canvas_output = Canvas(self.frame_trans_output, width=400, height=200)
        canvas_output.grid(row=self.rows_get + 3, column=0, padx=5, pady=5, columnspan=self.cols_get + 1)
        v_scrollbar_output = Scrollbar(self.frame_trans_output, orient=VERTICAL, command=canvas_output.yview)
        v_scrollbar_output.grid(row=self.rows_get + 3, column=self.cols_get + 2, sticky='ns')
        h_scrollbar_output = Scrollbar(self.frame_trans_output, orient=HORIZONTAL, command=canvas_output.xview)
        h_scrollbar_output.grid(row=self.rows_get + 2, column=0, sticky='ew')
        canvas_output.configure(yscrollcommand=v_scrollbar_output.set, xscrollcommand=h_scrollbar_output.set)

        frame_matrix_output = Frame(canvas_output)
        canvas_output.create_window((0, 0), window=frame_matrix_output, anchor='nw')

        for i in range(self.cols_get):
            for j in range(self.rows_get):
                Label(frame_matrix_output, text=self.transposed_matrix[i][j], font=('arial', 12, 'bold'), bd=5).grid(row=i, column=j, padx=5, pady=5, sticky='news')

        frame_matrix_output.update_idletasks()
        canvas_output.config(scrollregion=canvas_output.bbox("all"))

        self.gui_trans_output.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_trans_output.mainloop()

    def back_to_input(self):
        self.gui_trans_output.destroy()
        self.input_matrix()

    def input_matrix(self):
        self.gui_trans_menu.destroy()
        self.gui_trans_input = Toplevel()
        self.gui_trans_input.title("Chuyển vị")
        self.gui_trans_input.resizable(False, False)

        self.frame_trans_input = Frame(self.gui_trans_input, highlightbackground='black', highlightthickness=1, bg='#F9E79F', padx=5, pady=5)
        self.frame_trans_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_trans_input, text="Ma trận:", font=('arial', 12, 'bold'), bg='#F9E79F').grid(row=0, column=0)

        # empty arrays for Entry and StringVars
        text_var = []
        entries = []

        self.rows_get, self.cols_get = (self.rows.get(), self.cols.get())
        for i in range(self.rows_get):
            # append an empty list to arrays to append to later
            text_var.append([])
            entries.append([])
            for j in range(self.cols_get):
                # for column indications
                if i == 0:
                    Label(self.frame_trans_input, text=j + 1, bg='#F9E79F').grid(row=0, column=j + 1)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list5
                entries[i].append(Entry(self.frame_trans_input, textvariable=text_var[i][j], width=10, font=('arial', 10, 'bold')))

                # display entry
                entries[i][j].grid(row=i + 1, column=j + 1)

                # for row indications
                Label(self.frame_trans_input, text=i + 1, bg='#F9E79F').grid(row=i + 1, column=0, sticky='e')

        def get_mat():
            try:
                self.matrix = []
                for i2 in range(self.rows_get):
                    self.matrix.append([])
                    for j2 in range(self.cols_get):
                        self.matrix[i2].append(text_var[i2][j2].get())
                self.output_matrix()
            except (ValueError, Exception):
                messagebox.showerror('Error', 'Ma trận không hợp lệ')

        self.frame_button = Frame(self.gui_trans_input, bg='#F9E79F', highlightbackground='black', highlightthickness=1, padx=5, pady=5)
        self.frame_button.pack(fill='x', expand=True, padx=5, pady=3)
        Button(self.frame_button, text="Nhập", font=('arial', 10, 'bold'), width=11, activebackground='green', command=get_mat).grid(row=0, column=2, padx=14)
        Button(self.frame_button, text="Quay lại", font=('arial', 10, 'bold'), width=11, activebackground='green', command=self.back_to_dimensions).grid(row=0, column=1, padx=14)
        Button(self.frame_button, text="Quay lại Menu", font=('arial', 10, 'bold'), activebackground='green', command=self.back_to_menu_from_input).grid(row=0, column=0, padx=14)

        self.gui_trans_input.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_trans_input.mainloop()

    def back_to_dimensions(self):
        self.gui_trans_input.destroy()
        self.__init__()

    def back_to_menu_from_input(self):
        self.gui_trans_input.destroy()
        menu.gui_menu.deiconify()

    def __init__(self):
        self.gui_trans_input = None
        self.frame_trans_input = None
        self.gui_trans_output = None
        self.frame_trans_output = None
        self.transposed_matrix = None
        self.matrix = None
        self.rows_get, self.cols_get = None, None

        menu.gui_menu.withdraw()
        self.gui_trans_menu = Toplevel()
        self.gui_trans_menu.title("Chuyển vị")
        self.gui_trans_menu.geometry('270x500')
        self.gui_trans_menu.resizable(False, False)

        self.frame_trans_menu = Frame(self.gui_trans_menu, highlightbackground='black', highlightthickness=1, bg='#F9E79F', padx=5, pady=5)
        self.frame_trans_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_trans_menu, text='Nhập kích thước ma trận:', font=('arial', 14, 'bold'), bg='#F9E79F').grid(row=0, column=0, columnspan=3, sticky='news', pady=10)

        # Nhập kích thước ma trận:
        self.rows = IntVar()
        self.rows.set(2)
        OptionMenu(self.frame_trans_menu, self.rows, *range(1, 21)).grid(row=1, column=0, sticky='ew')

        Label(self.frame_trans_menu, text='x', bg='#F9E79F', font=('arial', 14, 'bold')).grid(row=1, column=1)

        self.cols = IntVar()
        self.cols.set(2)
        OptionMenu(self.frame_trans_menu, self.cols, *range(1, 21)).grid(row=1, column=2, sticky='ew')
        Button(self.frame_trans_menu, text='Nhập', font=('arial', 10, 'bold'), activebackground='green', padx=10, pady=5, command=self.input_matrix).grid(row=2, column=0, columnspan=3, pady=10)
        # QUAY LẠI MENU
        Button(self.frame_trans_menu, text="Quay lại Menu", font=('arial', 10, 'bold'), activebackground='green', padx=10, pady=5, command=self.back_to_menu_from_dimensions).grid(row=3, column=0, columnspan=3)

        self.gui_trans_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_trans_menu.mainloop()

    def back_to_menu_from_dimensions(self):
        self.gui_trans_menu.destroy()
        menu.gui_menu.deiconify()

if __name__ == "__main__":
    trans_calculator = Trans()

