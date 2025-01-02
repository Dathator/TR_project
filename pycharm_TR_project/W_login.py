from imports import *


class LogIn(QWidget):
    def __init__(self):
        super(LogIn, self).__init__()

        loadUi("W_login.ui", self)
        self.nameLineEdit = self.findChild(QLineEdit, "nameLineEdit")
        self.passwordLineEdit = self.findChild(QLineEdit, "passwordLineEdit")
        self.regButton = self.findChild(QPushButton, "regButton")
        self.enterButton = self.findChild(QPushButton, "enterButton")
        self.statusLabel = self.findChild(QLabel, "statusLabel")
