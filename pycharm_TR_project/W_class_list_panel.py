from imports import *


class ClassListPanel(QWidget):
    def __init__(self):
        super(ClassListPanel, self).__init__()

        loadUi("W_class_list_panel.ui", self)
        self.backButton = self.findChild(QPushButton, "backButton")
        self.userLabel = self.findChild(QLabel, "userLabel")