from imports import *


class StudentMenu(QWidget):
    def __init__(self):
        super(StudentMenu, self).__init__()

        loadUi("W_menu_student.ui", self)
        self.nameLabel = self.findChild(QLabel, "nameLabel")
        self.acchangeButton = self.findChild(QPushButton, "acchangeButton")
        self.prefButton = self.findChild(QPushButton, "prefButton")


class TeacherMenu(QWidget):
    def __init__(self):
        super(TeacherMenu, self).__init__()

        loadUi("W_menu_teacher.ui", self)
        self.nameLabel = self.findChild(QLabel, "nameLabel")
        self.acchangeButton = self.findChild(QPushButton, "acchangeButton")
        self.prefButton = self.findChild(QPushButton, "prefButton")
        self.classesButton = self.findChild(QPushButton, "classesButton")


class AdminMenu(QWidget):
    def __init__(self):
        super(AdminMenu, self).__init__()

        loadUi("W_menu_admin.ui", self)
        self.nameLabel = self.findChild(QLabel, "nameLabel")
        self.acchangeButton = self.findChild(QPushButton, "acchangeButton")
        self.prefButton = self.findChild(QPushButton, "prefButton")
        self.admpanelButton = self.findChild(QPushButton, "admpanelButton")