from imports import *
from W_login import LogIn
from W_registration import Registration
from W_menu import Menu


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.show()

    def show_w_login(self):
        w_login = LogIn()
        w_login.regButton.clicked.connect(self.show_w_reg)
        w_login.regButton.clicked.connect(w_login.close)
        w_login.enterButton.clicked.connect(self.show_w_menu)
        w_login.enterButton.clicked.connect(w_login.close)
        self.setCentralWidget(w_login)

    def show_w_reg(self):
        w_reg = Registration()
        w_reg.backButton.clicked.connect(self.show_w_login)
        w_reg.backButton.clicked.connect(w_reg.close)
        self.setCentralWidget(w_reg)

    def show_w_menu(self):
        w_menu = Menu()
        w_menu.acchangeButton.clicked.connect(self.show_w_login)
        w_menu.acchangeButton.clicked.connect(w_menu.close)
        self.setCentralWidget(w_menu)