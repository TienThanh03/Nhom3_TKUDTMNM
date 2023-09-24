from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel, messagebox, Canvas, Scrollbar, HORIZONTAL, VERTICAL
import numpy as np
from tkinter.constants import BOTH
from numpy.linalg import inv
import menu

class Inverse:
    def back_to_menu_from_output(self):
        self.gui_inverse_output.destroy()
        menu.gui_menu.deiconify()

    def back_to_input(self):
        self.gui_inverse_output.destroy()
        self.input_matrix()

    def compute_inverse(self):
        try:
            # Chuyển đổi ma trận từ chuỗi sang số nguyên
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] = int(self.matrix[i][j])
            self.matrix = np.linalg.inv(self.matrix)
            return self.matrix
        except (TypeError, NameError, ValueError):
            pass

    def output_matrix(self):
        self.gui_inverse_input.destroy()
        self.gui_inverse_output = Toplevel()
        self.gui_inverse_output.title("Matrix Calculator")

        self.frame_inverse_output = Frame(self.gui_inverse_output, highlightbackground='black', highlightthickness=1,
                                          padx=5, pady=5)
        self.frame_inverse_output.pack(fill='both', expand=True, padx=5, pady=5)

        # Hiển thị đầu vào của người dùng
        Label(self.frame_inverse_output, text='Input:', font=('arial', 12, 'bold')).grid(row=0, column=0)
        
        # Tạo thanh cuộn dọc cho nội dung của ma trận đầu vào
        canvas_input = Canvas(self.frame_inverse_output, width=400, height=200)
        canvas_input.grid(row=1, column=0)
        v_scrollbar_input = Scrollbar(self.frame_inverse_output, orient=VERTICAL, command=canvas_input.yview)
        v_scrollbar_input.grid(row=1, column=1, sticky='ns')
        canvas_input.configure(yscrollcommand=v_scrollbar_input.set)

        frame_matrix_input = Frame(canvas_input)
        canvas_input.create_window((0, 0), window=frame_matrix_input, anchor='nw')

        for i in range(self.rows):
            for j in range(self.cols):
                Label(frame_matrix_input, text=self.matrix[i][j], font=('arial', 12, 'bold')).grid(row=i, column=j,
                                                                                           padx=5, pady=5)

        frame_matrix_input.update_idletasks()
        canvas_input.config(scrollregion=canvas_input.bbox("all"))

        # Hiển thị đầu ra
        Label(self.frame_inverse_output, text='Inverted:', font=('arial', 12, 'bold')).grid(row=0, column=self.cols + 2)

        self.frame_button = Frame(self.gui_inverse_output, bg='#F9E79F', highlightbackground='black',
                                  highlightthickness=1, padx=5, pady=5)
        self.frame_button.pack(fill='x', expand=True, padx=5, pady=5)
        Button(self.frame_button, text="Back", font=('arial', 10, 'bold'), width=11, activebackground='green',
               command=self.back_to_input).grid(row=0, column=1, sticky='e', padx=14)
        Button(self.frame_button, text="Back to Menu", font=('arial', 10, 'bold'), activebackground='green',
               command=self.back_to_menu_from_output).grid(row=0, column=0, sticky='e', padx=14)
        Button(self.frame_button, text="Exit", font=('arial', 10, 'bold'), width=11, activebackground='green',
               command=exit).grid(row=0, column=2, sticky='e', padx=14)

        inverse_matrix = self.compute_inverse()
        
        # Tạo thanh cuộn dọc cho nội dung của ma trận kết quả
        canvas_output = Canvas(self.frame_inverse_output, width=400, height=200)
        canvas_output.grid(row=1, column=self.cols + 2)
        v_scrollbar_output = Scrollbar(self.frame_inverse_output, orient=VERTICAL, command=canvas_output.yview)
        v_scrollbar_output.grid(row=1, column=self.cols + 3, sticky='ns')
        canvas_output.configure(yscrollcommand=v_scrollbar_output.set)

        frame_matrix_output = Frame(canvas_output)
        canvas_output.create_window((0, 0), window=frame_matrix_output, anchor='nw')

        for i in range(self.rows):
            for j in range(self.cols):
                Label(frame_matrix_output, text=inverse_matrix[i][j], font=('arial', 12, 'bold')).grid(row=i,
                                                                                               column=j,
                                                                                               padx=5, pady=5)

        frame_matrix_output.update_idletasks()
        canvas_output.config(scrollregion=canvas_output.bbox("all"))

        # Tạo thanh cuộn ngang cho cả hai khung ma trận đầu vào và kết quả
        h_scrollbar_input = Scrollbar(self.frame_inverse_output, orient=HORIZONTAL, command=canvas_input.xview)
        h_scrollbar_input.grid(row=2, column=0, sticky='ew')
        canvas_input.configure(xscrollcommand=h_scrollbar_input.set)
        
        h_scrollbar_output = Scrollbar(self.frame_inverse_output, orient=HORIZONTAL, command=canvas_output.xview)
        h_scrollbar_output.grid(row=2, column=self.cols + 2, sticky='ew')
        canvas_output.configure(xscrollcommand=h_scrollbar_output.set)

        self.gui_inverse_output.protocol("WM_DELETE_WINDOW", self.back_to_input)
        self.gui_inverse_output.mainloop()

    def input_matrix(self):
        self.gui_inverse_menu.destroy()
        self.gui_inverse_input = Toplevel()
        self.gui_inverse_input.title("Matrix Calculator")

        self.frame_inverse_input = Frame(self.gui_inverse_input, bg='#F9E79F', highlightbackground='black',
                                         highlightthickness=1, padx=5, pady=5)
        self.frame_inverse_input.pack(fill='both', expand=True, padx=5, pady=5)

        Label(self.frame_inverse_input, text="Matrix:", bg='#F9E79F', font=('arial', 12, 'bold')).grid(row=0, column=0)

        # Tạo ma trận các ô nhập dữ liệu
        text_var = []
        entries = []

        self.rows, self.cols = (self.m_dimensions.get(), self.m_dimensions.get())
        for i in range(self.rows):
            text_var.append([])
            entries.append([])
            for j in range(self.cols):
                if i == 0:
                    Label(self.frame_inverse_input, text=j + 1, bg='#F9E79F').grid(row=1, column=j + 1, padx=5)
                if j == 0:
                                    Label(self.frame_inverse_input, text=i + 1, bg='#F9E79F').grid(row=i + 2, column=0, padx=5)

                text_var[i].append(StringVar())
                entries[i].append(
                    Entry(self.frame_inverse_input, textvariable=text_var[i][j], width=10, font=('arial', 10, 'bold')))
                entries[i][j].grid(row=i + 2, column=j + 1)

        def get_mat():
            try:
                self.matrix = []
                for i2 in range(self.rows):
                    self.matrix.append([])
                    for j2 in range(self.cols):
                        self.matrix[i2].append(text_var[i2][j2].get())
                self.output_matrix()
            except (NameError, TypeError, ValueError):
                messagebox.showerror('Lỗi', 'Ma trận không hợp lệ')

        self.frame_button = Frame(self.gui_inverse_input, bg='#F9E79F', highlightbackground='black',
                                  highlightthickness=1, padx=5, pady=5)
        self.frame_button.pack(fill='x', expand=True, padx=5, pady=5)
        Button(self.frame_button, text="Nhập", font=('arial', 10, 'bold'), width=11, activebackground='green',
               command=get_mat).grid(row=0, column=2, sticky='e', padx=14)
        Button(self.frame_button, text="Quay lại", font=('arial', 10, 'bold'), width=11, activebackground='green',
               command=self.back_to_dimensions).grid(row=0, column=1, sticky='e', padx=14)
        Button(self.frame_button, text="Quay lại Menu", font=('arial', 10, 'bold'), activebackground='green',
               command=self.back_to_menu_from_input).grid(row=0, column=0, sticky='e', padx=14)

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
        self.rows, self.cols = None, None
        self.matrix = None

        menu.gui_menu.withdraw()
        self.gui_inverse_menu = Toplevel()
        self.gui_inverse_menu.title("Nghịch đảo")
        self.gui_inverse_menu.geometry('700x550')
        self.gui_inverse_menu.resizable(False, False)

        self.frame_inverse_menu = Frame(self.gui_inverse_menu, highlightbackground='black', padx=5, pady=5,
                                        bg='#F9E79F', highlightthickness=1)
        self.frame_inverse_menu.pack(fill='both', expand=True, padx=5, pady=5)

        Label(self.frame_inverse_menu, text='Chọn kích thước ma trận:', font=('arial', 14, 'bold'), bg='#F9E79F').pack(
            fill='both', pady=10)

        self.m_dimensions = IntVar()
        self.m_dimensions.set(2)
        OptionMenu(self.frame_inverse_menu, self.m_dimensions, *range(2, 21)).pack(fill='both', pady=10, padx=5)
        Button(self.frame_inverse_menu, text='Nhập', font=('arial', 10, 'bold'), activebackground='green', padx=10,
               pady=5, command=self.input_matrix).pack(pady=20)

        Button(self.frame_inverse_menu, text="Quay lại Menu", font=('arial', 10, 'bold'), activebackground='green',
               padx=10, pady=5, command=self.back_to_menu_from_dimension).pack()

        self.gui_inverse_menu.protocol("WM_DELETE_WINDOW",
                                       menu.gui_menu.destroy)
        self.gui_inverse_menu.mainloop()

    def back_to_menu_from_dimension(self):
        self.gui_inverse_menu.destroy()
        menu.gui_menu.deiconify()

if __name__ == "__main__":
    inverse_calculator = Inverse()

