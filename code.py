import sympy as sp
import matplotlib.pyplot as plt

# Khai báo biến ký hiệu
x = sp.symbols('x')

# Định nghĩa dãy số
n = sp.symbols('n')
sequence = 1/n

while True:
    #them 1 print
    print("Chọn tùy chọn:")
    print("1. Tính đạo hàm")
    print("2. Tính tích phân")
    print("3. Giải phương trình")
    print("4. Xác định tính hội tụ")
    print("5. Thoát")
    
    choice = input("Nhập lựa chọn của bạn: ")
    
    if choice == '1':
        expression = input("Nhập biểu thức (ví dụ: x**2 + 3*x - 1): ")
        try:
            f = sp.sympify(expression)
            derivative = sp.diff(f, x)
            print("Đạo hàm của", expression, "là:", derivative)
        except:
            print("Biểu thức không hợp lệ.")
    
    elif choice == '2':
        expression = input("Nhập biểu thức (ví dụ: x**2 + 3*x - 1): ")
        try:
            f = sp.sympify(expression)
            integral = sp.integrate(f, x)
            print("Tích phân của", expression, "là:", integral)
        except:
            print("Biểu thức không hợp lệ.")

    elif choice == '3':
        equation = input("Nhập phương trình (ví dụ: x**2 - 4 = 0): ")
        try:
            equation = sp.Eq(sp.sympify(equation), 0)
            solutions = sp.solve(equation, x)
            print("Nghiệm của phương trình là:", solutions)
        except :
            print("Phương trình không hợp lệ.")
    elif choice == '4':
        # Xác định tính hội tụ của dãy số
        limit = sp.limit(sequence, n, sp.oo)

        print("Giới hạn của dãy số là:", limit)

        # Vẽ đồ thị của dãy số
        n_values = range(1, 21)  # Dãy số từ n=1 đến n=20
        sequence_values = [sp.N(sequence.subs(n, value)) for value in n_values]

        plt.plot(n_values, sequence_values)
        plt.xlabel('n')
        plt.ylabel('Giá trị của dãy số')
        plt.title('Tính hội tụ của dãy số')
        plt.grid(True)
        plt.show()
    elif choice == '5':
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
