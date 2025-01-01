from imports import *


class LogIn(QWidget):
    def __init__(self):
        super(LogIn, self).__init__()
        self.setFixedSize(500, 600)

        loadUi("W_login.ui", self)
        self.regButton = self.findChild(QPushButton, "regButton")
        self.enterButton = self.findChild(QPushButton, "enterButton")