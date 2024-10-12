import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goal Planner")
    
        form = QFormLayout()
        form.addRow(QLabel("Goal 1 "), QLineEdit())

        self.setLayout(form)
        
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    
    app.exec()

