from imports import *


class Menu(QWidget):
    def __init__(self):
        super(Menu, self).__init__()
        self.setFixedSize(600, 600)

        loadUi("W_menu.ui", self)
        self.acchangeButton = self.findChild(QPushButton, "acchangeButton")