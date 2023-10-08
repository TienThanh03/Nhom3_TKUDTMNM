import sys
import sympy as sp
import matplotlib.pyplot as plt
from PyQt6 import QtWidgets, QtGui

class MathOperationsApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Khai báo biến ký hiệu
        self.x = sp.symbols('x')

        # Định nghĩa dãy số
        self.n = sp.symbols('n')
        self.sequence = 1 / self.n

        # Tạo các thành phần giao diện
        self.init_ui()

    def init_ui(self):
        # Tạo nhãn
        self.label = QtWidgets.QLabel("Chọn tùy chọn:")

        # Tạo ô nhập
        self.input_field = QtWidgets.QLineEdit()

        # Tạo nút chức năng
        self.derivative_button = QtWidgets.QPushButton("Tính đạo hàm")
        self.integral_button = QtWidgets.QPushButton("Tính tích phân")
        self.equation_button = QtWidgets.QPushButton("Giải phương trình")
        self.convergence_button = QtWidgets.QPushButton("Xác định tính hội tụ")
        self.exit_button = QtWidgets.QPushButton("Thoát")

        # Tạo khu vực vẽ biểu đồ
        self.plot_widget = QtWidgets.QLabel()

        # Thiết lập layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.derivative_button)
        layout.addWidget(self.integral_button)
        layout.addWidget(self.equation_button)
        layout.addWidget(self.convergence_button)
        layout.addWidget(self.exit_button)
        layout.addWidget(self.plot_widget)

        # Kết nối nút với các hàm chức năng
        self.derivative_button.clicked.connect(self.calculate_derivative)
        self.integral_button.clicked.connect(self.calculate_integral)
        self.equation_button.clicked.connect(self.solve_equation)
        self.convergence_button.clicked.connect(self.check_convergence)
        self.exit_button.clicked.connect(self.close_app)

        self.setLayout(layout)

    def calculate_derivative(self):
        expression = self.input_field.text()
        try:
            f = sp.sympify(expression)
            derivative = sp.diff(f, self.x)
            self.show_result(f"Đạo hàm của {expression} là: {derivative}")
        except:
            self.show_result("Biểu thức không hợp lệ.")

    def calculate_integral(self):
        expression = self.input_field.text()
        try:
            f = sp.sympify(expression)
            integral = sp.integrate(f, self.x)
            self.show_result(f"Tích phân của {expression} là: {integral}")
        except:
            self.show_result("Biểu thức không hợp lệ.")

    def solve_equation(self):
        equation = self.input_field.text()
        try:
            equation = sp.Eq(sp.sympify(equation), 0)
            solutions = sp.solve(equation, self.x)
            self.show_result(f"Nghiệm của phương trình là: {solutions}")
        except:
            self.show_result("Phương trình không hợp lệ.")

    def check_convergence(self):
        # Nhập giới hạn từ người dùng
        limit_point_str, ok = QtWidgets.QInputDialog.getText(self, "Nhập giới hạn", "Nhập giá trị giới hạn:")

        if ok:
            try:
                # Chuyển đổi giá trị nhập vào thành giá trị số
                limit_point = float(limit_point_str)

                # Tính giới hạn số học
                limit = sp.limit(self.sequence, self.n, limit_point)
                self.show_result(f"Giới hạn của dãy số khi n tiến tới {limit_point} là: {limit}")

                # Tạo và hiển thị biểu đồ của dãy số
                n_values = range(1, 21)
                sequence_values = [sp.N(self.sequence.subs(self.n, value)) for value in n_values]
                plt.figure()
                plt.plot(n_values, sequence_values)
                plt.xlabel('n')
                plt.ylabel('Giá trị của dãy số')
                plt.title(f'Tính hội tụ của dãy số khi n tiến tới {limit_point}')
                plt.grid(True)
                plt.savefig('sequence_plot.png')
                plt.close()

                # Hiển thị biểu đồ trong giao diện
                pixmap = QtGui.QPixmap('sequence_plot.png')
                self.plot_widget.setPixmap(pixmap)

            except ValueError:
                self.show_result("Giá trị giới hạn không hợp lệ.")

    def show_result(self, result):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText(result)
        msg_box.setWindowTitle("Kết quả")
        msg_box.exec()

    def close_app(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MathOperationsApp()
    window.setWindowTitle("Các Phép Tính Toán")
    window.show()
    sys.exit(app.exec())
