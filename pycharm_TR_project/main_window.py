from imports import *
from W_login import LogIn
from W_registration import Registration


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.show()

    def show_w_login(self):
        W_login = LogIn()
        W_login.regButton.clicked.connect(self.show_w_reg)
        W_login.regButton.clicked.connect(W_login.close)
        self.setCentralWidget(W_login)

    def show_w_reg(self):
        W_reg = Registration()
        W_reg.backButton.clicked.connect(self.show_w_login)
        W_reg.backButton.clicked.connect(W_reg.close)
        self.setCentralWidget(W_reg)