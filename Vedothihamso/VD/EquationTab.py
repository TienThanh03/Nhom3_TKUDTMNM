import os
import PyQt6.QtWidgets
import matplotlib.colors as mcolors
import sympy
from sympy.plotting.plot import Plot
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from .Equation import Equation


class EquationTab(PyQt6.QtWidgets.QWidget):
    colors = tuple(mcolors.TABLEAU_COLORS.keys())

    def __init__(self):
        super().__init__()

        self.plot = None
        self.y_axis_range = (0, 10)  # Initial y-axis range

        # Create layout
        self.layout = PyQt6.QtWidgets.QVBoxLayout()

        # Add label
        self.label = PyQt6.QtWidgets.QLabel()
        self.layout.addWidget(self.label)

        # Add zoom in button
        self.zoom_in_button = PyQt6.QtWidgets.QPushButton("Zoom In")
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.layout.addWidget(self.zoom_in_button)

        # Add zoom out button
        self.zoom_out_button = PyQt6.QtWidgets.QPushButton("Zoom Out")
        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.layout.addWidget(self.zoom_out_button)

        # Add button
        self.button = PyQt6.QtWidgets.QPushButton("Add Equation")
        self.button.clicked.connect(self.add_equation)
        self.layout.addWidget(self.button)

        self.refresh_button = PyQt6.QtWidgets.QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.layout.addWidget(self.refresh_button)

        # Set layout
        self.setLayout(self.layout)

    def add_equation(self):
        # create equation
        equation = Equation()

        # add equation to the second to last position of the layout
        self.layout.insertWidget(self.layout.count() - 3, equation)

    def refresh(self):
        # loop over all Equation
        plot = None
        for color, equation in zip(self.colors, self.children()):
            if type(equation) != Equation:
                continue
            equation: Equation = equation
            if equation.equation_right is None:
                continue
            lhs, rhs = equation.equation_left, equation.equation_right
            intersection_points = sympy.solve(lhs - rhs, sympy.var("y"))

            for f in sympy.solve(lhs - rhs, sympy.var("y")):
                label = f'y = {f}'
                if plot is None:
                    plot = sympy.plotting.plot(f, show=False, line_color=color, ylabel="y", legend=True, label=label,
                                               ylim=self.y_axis_range)  # Set y-axis range
                else:
                    plot.extend(
                        sympy.plotting.plot(f, show=False, line_color=color, ylabel="y", legend=True, label=label,
                                           ylim=self.y_axis_range))  # Set y-axis range
        if plot is not None:
            if not os.path.exists("cache"):
                os.mkdir("cache")
            # Save the plot as an image
            image_path = os.path.join("cache", "graph.png")
            plot.save(image_path)
            self.plot = plot

            # Display the plot in the label
            pixmap = QPixmap(image_path)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def zoom_in(self):
        # Decrease the y-axis range to zoom in
        self.y_axis_range = (self.y_axis_range[0] * 0.9, self.y_axis_range[1] * 0.9)
        self.refresh()

    def zoom_out(self):
        # Increase the y-axis range to zoom out
        self.y_axis_range = (self.y_axis_range[0] * 1.1, self.y_axis_range[1] * 1.1)
        self.refresh()
