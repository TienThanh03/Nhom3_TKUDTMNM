import numpy as np
import tkinter as tk
from tkinter import Entry, Label, Button

def solve_linear_equation():
    try:
        n = int(variable_n.get())
        A_values = []
        B_values = []

        # Lấy giá trị ma trận A từ input
        for i in range(n):
            A_row = []
            for j in range(n):
                A_row.append(float(A_entries[i][j].get()))
            A_values.append(A_row)

        # Lấy giá trị ma trận B từ input
        for i in range(n):
            B_values.append(float(B_entries[i].get()))

        A = np.array(A_values)
        B = np.array(B_values)
        A_inv = np.linalg.inv(A)

        X = np.dot(A_inv, B)

        result_label.config(text=f'Nghiệm của hệ: {X}')
    except Exception as e:
        result_label.config(text=f'Lỗi: {str(e)}')

# Tạo cửa sổ tkinter
root = tk.Tk()
root.title("Giải Hệ Phương Trình Tuyến Tính")

# Nhập số biến n
n_label = Label(root, text="Nhập số biến n:")
n_label.grid(row=0, column=0)
variable_n = tk.StringVar()
n_entry = Entry(root, textvariable=variable_n)
n_entry.grid(row=0, column=1)

# Tạo widgets cho ma trận A và B dựa trên giá trị của n
A_entries = []
B_entries = []

def create_input_fields():
    global A_entries, B_entries
    n = int(variable_n.get())

    # Xóa các widgets cũ (nếu có)
    for widget in root.winfo_children():
        widget.grid_forget()

    # Tạo lại các widgets mới
    for i in range(n):
        A_row_entries = []
        for j in range(n):
            label = Label(root, text=f'A[{i + 1},{j + 1}]:')
            entry = Entry(root)
            label.grid(row=i, column=j * 2)
            entry.grid(row=i, column=j * 2 + 1)
            A_row_entries.append(entry)
        A_entries.append(A_row_entries)

    B_label = Label(root, text="Ma trận B:")
    B_label.grid(row=n, column=0)
    B_entries = [Entry(root) for _ in range(n)]
    for i in range(n):
        B_entries[i].grid(row=n, column=i * 2 + 1)

    # Tạo nút giải hệ
    solve_button = Button(root, text="Giải", command=solve_linear_equation)
    solve_button.grid(row=n + 1, columnspan=n * 2)

    # Kết quả
    global result_label
    result_label = Label(root, text="")
    result_label.grid(row=n + 2, columnspan=n * 2)

# Tạo nút để tạo các trường nhập dữ liệu A và B dựa trên n
create_fields_button = Button(root, text="Nhập Dữ Liệu", command=create_input_fields)
create_fields_button.grid(row=0, column=2)

# Khởi chạy ứng dụng
root.mainloop()
