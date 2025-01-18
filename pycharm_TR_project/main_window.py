from imports import *
from W_login import LogIn
from W_registration import Registration
from W_menu import StudentMenu, TeacherMenu, AdminMenu
from W_account_pref import AccountPref
from database import insert_user, get_current_user_by_name, get_current_user_by_name_password


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.current_user = None
        self.show()

    def show_w_login(self):
        if self.current_user:
            self.current_user = None
        w_login = LogIn()
        w_login.regButton.clicked.connect(self.show_w_reg)
        w_login.regButton.clicked.connect(w_login.close)
        w_login.enterButton.clicked.connect(lambda: self.enterBut_clicked(w_login))
        self.setCentralWidget(w_login)
        self.setFixedSize(500, 600)

    def enterBut_clicked(self, W_login):
        try:
            get_current_user_by_name_password(W_login.nameLineEdit.text(),
                                              W_login.passwordLineEdit.text())
        except:
            W_login.statusLabel.setText("El nom d'usuari o la contrasenya són incorrectes.")
        else:
            self.current_user = get_current_user_by_name_password(W_login.nameLineEdit.text(),
                                                                  W_login.passwordLineEdit.text())
            self.show_w_menu()
            W_login.close()

    def show_w_reg(self):
        if self.current_user:
            self.current_user = None
        w_reg = Registration()
        w_reg.backButton.clicked.connect(self.show_w_login)
        w_reg.backButton.clicked.connect(w_reg.close)
        w_reg.createButton.clicked.connect(lambda: self.createBut_clicked(w_reg))
        self.setCentralWidget(w_reg)
        self.setFixedSize(500, 600)

    def createBut_clicked(self, W_reg):
        if W_reg.check_data(W_reg.nameLineEdit.text(), W_reg.passwordLineEdit.text(), W_reg.reppasswordLineEdit.text()):
            insert_user(W_reg.nameLineEdit.text(), W_reg.passwordLineEdit.text())
            self.show_w_login()
            W_reg.close()

    def show_w_menu(self):
        w_menu = None
        if self.current_user[3] == 1:
            w_menu = StudentMenu()
            w_menu.nameLabel.setText(self.current_user[1])
            w_menu.acchangeButton.clicked.connect(self.show_w_login)
            w_menu.acchangeButton.clicked.connect(w_menu.close)
            w_menu.prefButton.clicked.connect(self.show_w_account_pref)
            w_menu.prefButton.clicked.connect(w_menu.close)
        elif self.current_user[3] == 2:
            w_menu = TeacherMenu()
            w_menu.nameLabel.setText(self.current_user[1])
            w_menu.acchangeButton.clicked.connect(self.show_w_login)
            w_menu.acchangeButton.clicked.connect(w_menu.close)
            w_menu.prefButton.clicked.connect(self.show_w_account_pref)
            w_menu.prefButton.clicked.connect(w_menu.close)
        elif self.current_user[3] == 3:
            w_menu = AdminMenu()
            w_menu.nameLabel.setText(self.current_user[1])
            w_menu.acchangeButton.clicked.connect(self.show_w_login)
            w_menu.acchangeButton.clicked.connect(w_menu.close)
            w_menu.prefButton.clicked.connect(self.show_w_account_pref)
            w_menu.prefButton.clicked.connect(w_menu.close)
        self.setCentralWidget(w_menu)
        self.setFixedSize(500, 600)

    def show_w_account_pref(self):
        w_account_pref = AccountPref()
        w_account_pref.nameLabel.setText(self.current_user[1])
        w_account_pref.acchangeButton.clicked.connect(self.show_w_login)
        w_account_pref.acchangeButton.clicked.connect(w_account_pref.close)
        w_account_pref.backtomenuButton.clicked.connect(self.show_w_menu)
        w_account_pref.backtomenuButton.clicked.connect(w_account_pref.close)
        w_account_pref.changenameButton.clicked.connect(lambda: self.change_current_user(w_account_pref.nameLabel.text()))
        self.setCentralWidget(w_account_pref)
        self.setFixedSize(500, 600)

    def change_current_user(self, new_name):
        self.current_user = (self.current_user[0], new_name, self.current_user[2], self.current_user[3])