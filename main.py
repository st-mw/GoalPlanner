import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from goal import Goal
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Goal Planner")
        
        container = QWidget()
        self.setCentralWidget(container)
        self.layout = QVBoxLayout()
        container.setLayout(self.layout)
        
        self.new_goal_button = QPushButton("Make a new goal!")
        self.layout.addWidget(self.new_goal_button)

        self.new_goal_button.clicked.connect(self.add_new_goal)

    def add_new_goal(self):
        self.layout.addWidget(QLabel("Goal Title: "))
        self.entry_box = QLineEdit()
        self.layout.addWidget(self.entry_box)

        self.calendar = QCalendarWidget()
        self.date_button = QPushButton("Select date")

        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.date_button)

        self.date_button.clicked.connect(self.date_selected)
        
        print("Goal added.")

    def date_selected(self):
        new_goal = Goal()
        new_goal.end_date = self.calendar.selectedDate()
        new_goal.title = self.entry_box.text()
        print(new_goal.end_date)
        print(new_goal.title)

        
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    
    app.exec()
