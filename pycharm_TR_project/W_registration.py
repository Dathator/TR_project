from imports import *


class Registration(QWidget):
    def __init__(self):
        super(Registration, self).__init__()

        loadUi("W_registration.ui", self)
        self.createButton = self.findChild(QPushButton, "createButton")
        self.backButton = self.findChild(QPushButton, "backButton")
        self.nameLineEdit = self.findChild(QLineEdit, "nameLineEdit")
        self.passwordLineEdit = self.findChild(QLineEdit, "passwordLineEdit")
        self.reppasswordLineEdit = self.findChild(QLineEdit, "reppasswordLineEdit")
        self.statusLabel = self.findChild(QLabel, "statusLabel")

    def check_data(self, name, password, rep_password):
        if (name != "") and (password != "") and (rep_password != ""):
            if password == rep_password:
                self.statusLabel.setText("Tot està bé.")
                return True
            else:
                self.statusLabel.setText("La contrasenya s'ha repetit incorrectament.")
                return False
        else:
            self.statusLabel.setText("Un dels camps no està emplenat.")
            return False