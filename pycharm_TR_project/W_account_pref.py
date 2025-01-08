from imports import *
from database import get_current_user_by_name, change_user_data


class AccountPref(QWidget):
    def __init__(self):
        super(AccountPref, self).__init__()

        loadUi("W_account_pref.ui", self)
        self.nameLabel = self.findChild(QLabel, "nameLabel")
        self.acchangeButton = self.findChild(QPushButton, "acchangeButton")
        self.backtomenuButton = self.findChild(QPushButton, "backtomenuButton")
        self.chooseofchangeBox = self.findChild(QComboBox, "chooseofchangeBox")
        self.chooseofchangeBox.activated.connect(lambda: self.choose_of_change(self.chooseofchangeBox))
        self.nameFrame = self.findChild(QFrame, "nameFrame")
        self.passwordFrame = self.findChild(QFrame, "passwordFrame")
        self.passwordFrame.hide()
        self.intronLineEdit = self.findChild(QLineEdit, "intronLineEdit")
        self.intropLineEdit = self.findChild(QLineEdit, "intropLineEdit")
        self.reppLineEdit = self.findChild(QLineEdit, "reppLineEdit")
        self.nstatusLabel = self.findChild(QLabel, "nstatusLabel")
        self.pstatusLabel = self.findChild(QLabel, "pstatusLabel")
        self.changenameButton = self.findChild(QPushButton, "changenameButton")
        self.changenameButton.clicked.connect(lambda: self.changenameButton_clicked(self.intronLineEdit.text()))
        self.changepasButton = self.findChild(QPushButton, "changepasButton")
        self.changepasButton.clicked.connect(lambda: self.changepasButton_clicked)

    def choose_of_change(self, comboBox):
        if comboBox.currentIndex() == 0:
            self.nameFrame.show()
            self.passwordFrame.hide()
        else:
            self.passwordFrame.show()
            self.nameFrame.hide()

    def changenameButton_clicked(self, new_name):
        try:
            get_current_user_by_name(new_name)
        except:
            self.nstatusLabel.setText("Tot està bé.")
            change_user_data(new_name)
        else:
            self.nstatusLabel.setText("L'usuari ja existeix.")

    def changepasButton_clicked(self, new_password):
        pass