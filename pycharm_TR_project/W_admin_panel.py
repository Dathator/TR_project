from imports import *
from database import get_all_users


class AdmPanel(QWidget):
    def __init__(self):
        super(AdmPanel, self).__init__()

        loadUi("W_admin_panel.ui", self)
        self.backButton = self.findChild(QPushButton, "backButton")

        self.users = get_all_users()
        self.usersTable = self.findChild(QTableWidget, "usersTable")
        self.usersTable.setRowCount(len(self.users))
        self.usersTable.setColumnCount(4)
        self.usersTable.setHorizontalHeaderLabels(["ID", "Name", "Password", "Status"])
        for i in range(0, len(self.users)):
            self.usersTable.setItem(i, 0, QTableWidgetItem(str(self.users[i][0])))
            self.usersTable.setItem(i, 1, QTableWidgetItem(str(self.users[i][1])))
            self.usersTable.setItem(i, 2, QTableWidgetItem(str(self.users[i][2])))
            self.usersTable.setItem(i, 3, QTableWidgetItem(str(self.users[i][3])))