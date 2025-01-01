from imports import *


class Registration(QWidget):
    def __init__(self):
        super(Registration, self).__init__()
        self.setFixedSize(500, 600)

        loadUi("W_registration.ui", self)
        self.backButton = self.findChild(QPushButton, "backButton")