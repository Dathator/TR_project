from imports import *
from W_login import LogIn
from W_registration import Registration
from W_menu import StudentMenu, TeacherMenu, AdminMenu
from W_account_pref import AccountPref
from W_admin_panel import AdmPanel
from W_teacher_class_list import TeacherClassList
from W_class_notes import ClassNotes
from W_student_class_list import StudentsClassList
from W_student_notes import StudentNotes
from database import insert_user, get_current_user_by_name_password


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
            w_menu.nameLabel.setText(str(self.current_user[1]))
            w_menu.acchangeButton.clicked.connect(self.show_w_login)
            w_menu.acchangeButton.clicked.connect(w_menu.close)
            w_menu.prefButton.clicked.connect(self.show_w_account_pref)
            w_menu.prefButton.clicked.connect(w_menu.close)
            w_menu.signaturesButton.clicked.connect(self.show_w_student_class_list)
            w_menu.signaturesButton.clicked.connect(w_menu.close)
        elif self.current_user[3] == 2:
            w_menu = TeacherMenu()
            w_menu.nameLabel.setText(str(self.current_user[1]))
            w_menu.acchangeButton.clicked.connect(self.show_w_login)
            w_menu.acchangeButton.clicked.connect(w_menu.close)
            w_menu.prefButton.clicked.connect(self.show_w_account_pref)
            w_menu.prefButton.clicked.connect(w_menu.close)
            w_menu.classesButton.clicked.connect(self.show_w_teacher_class_list)
            w_menu.classesButton.clicked.connect(w_menu.close)
        elif self.current_user[3] == 3:
            w_menu = AdminMenu()
            w_menu.nameLabel.setText(str(self.current_user[1]))
            w_menu.acchangeButton.clicked.connect(self.show_w_login)
            w_menu.acchangeButton.clicked.connect(w_menu.close)
            w_menu.prefButton.clicked.connect(self.show_w_account_pref)
            w_menu.prefButton.clicked.connect(w_menu.close)
            w_menu.everyclassButton.clicked.connect(self.show_w_teacher_class_list)
            w_menu.everyclassButton.clicked.connect(w_menu.close)
            w_menu.admpanelButton.clicked.connect(self.show_w_adm_panel)
            w_menu.admpanelButton.clicked.connect(w_menu.close)
        self.setCentralWidget(w_menu)
        self.setFixedSize(500, 600)

    def show_w_account_pref(self):
        w_account_pref = AccountPref()
        w_account_pref.nameLabel.setText(str(self.current_user[1]))
        w_account_pref.acchangeButton.clicked.connect(self.show_w_login)
        w_account_pref.acchangeButton.clicked.connect(w_account_pref.close)
        w_account_pref.backtomenuButton.clicked.connect(self.show_w_menu)
        w_account_pref.backtomenuButton.clicked.connect(w_account_pref.close)
        w_account_pref.changenameButton.clicked.connect(lambda: self.change_current_user(w_account_pref.nameLabel.text()))
        self.setCentralWidget(w_account_pref)
        self.setFixedSize(500, 600)

    def change_current_user(self, new_name):
        self.current_user = (self.current_user[0], new_name, self.current_user[2], self.current_user[3])

    def show_w_adm_panel(self):
        w_adm_panel = AdmPanel()
        w_adm_panel.userLabel.setText(self.current_user[1])
        w_adm_panel.backButton.clicked.connect(self.show_w_menu)
        w_adm_panel.backButton.clicked.connect(w_adm_panel.close)
        w_adm_panel.saveButton.clicked.connect(lambda: self.change_current_user(w_adm_panel.userLabel.text()))
        self.setCentralWidget(w_adm_panel)
        self.setFixedSize(800, 580)

    def show_w_teacher_class_list(self):
        w_teacher_class_list = TeacherClassList(self)
        w_teacher_class_list.userLabel.setText(self.current_user[1])
        w_teacher_class_list.current_user = self.current_user
        w_teacher_class_list.fill_classes()
        w_teacher_class_list.backButton.clicked.connect(self.show_w_menu)
        w_teacher_class_list.backButton.clicked.connect(w_teacher_class_list.close)
        self.setCentralWidget(w_teacher_class_list)
        self.setFixedSize(800, 600)

    def show_w_class_notes(self, class_list_window, class_id):
        w_class_notes = ClassNotes(class_list_window, class_id)
        w_class_notes.backButton.clicked.connect(self.show_w_teacher_class_list)
        w_class_notes.backButton.clicked.connect(w_class_notes.close)
        self.setCentralWidget(w_class_notes)
        self.setFixedSize(1100, 700)

    def show_w_student_class_list(self):
        w_student_class_list = StudentsClassList(self)
        w_student_class_list.userLabel.setText(self.current_user[1])
        w_student_class_list.backButton.clicked.connect(self.show_w_menu)
        w_student_class_list.backButton.clicked.connect(w_student_class_list.close)
        self.setCentralWidget(w_student_class_list)
        self.setFixedSize(800, 600)

    def show_w_student_notes(self, class_id):
        w_student_notes = StudentNotes(class_id, self.current_user[0])
        w_student_notes.userLabel.setText(self.current_user[1])
        w_student_notes.backButton.clicked.connect(self.show_w_student_class_list)
        w_student_notes.backButton.clicked.connect(w_student_notes.close)
        self.setCentralWidget(w_student_notes)
        self.setFixedSize(1100, 300)
