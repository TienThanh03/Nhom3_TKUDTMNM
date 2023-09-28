import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate():
    matrix = []
    for x in range(9):
        try:
            value = int(entry_values[x].get())
            matrix.append(value)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên.")
            return

    arr = np.array(matrix, ndmin=1)
    newarr = arr.reshape(3, 3)
    x = newarr.copy()

    for row in range(3):
        for col in range(3):
            if row != col:
                x[row][col] = newarr[col][row]

    result_text.set(f"Ma trận đã nhập:\n{newarr}\n\nMa trận sau khi chuyển đổi:\n{x}")

    # Tính tích hai ma trận
    matrix_product = np.dot(newarr, x)
    result_text.set(result_text.get() + f"\n\nTích hai ma trận:\n{matrix_product}")

root = tk.Tk()
root.title("Chuyển đổi và tính tích ma trận")

entry_values = []

for i in range(9):
    label = tk.Label(root, text=f"Nhập số thứ {i+1}:")
    label.grid(row=i, column=0, padx=5, pady=5)
    entry_value = tk.Entry(root)
    entry_value.grid(row=i, column=1, padx=5, pady=5)
    entry_values.append(entry_value)

calculate_button = tk.Button(root, text="Tính toán", command=calculate)
calculate_button.grid(row=9, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=10, columnspan=2, padx=5, pady=5)

root.mainloop()

