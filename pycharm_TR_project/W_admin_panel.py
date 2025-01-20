from imports import *
from database import get_all_users, change_user_name, change_user_password, change_user_status


class QComboBoxForAdmPAnel(QComboBox):
    def __init__(self, scrollWidget=None, *args, **kwargs):
        super(QComboBoxForAdmPAnel, self).__init__(*args, **kwargs)
        self.scrollWidget=scrollWidget
        self.setFocusPolicy(Qt.StrongFocus)

    def wheelEvent(self, *args, **kwargs):
        if self.hasFocus():
            return QComboBox.wheelEvent(self, *args, **kwargs)
        else:
            if self.scrollWidget is not None:
                return self.scrollWidget.wheelEvent(*args, **kwargs)
            else:
                return None


class AdmPanel(QWidget):
    def __init__(self):
        super(AdmPanel, self).__init__()

        loadUi("W_admin_panel.ui", self)
        self.backButton = self.findChild(QPushButton, "backButton")
        self.saveButton = self.findChild(QPushButton, "saveButton")
        self.saveButton.clicked.connect(self.update_data)

        self.users = get_all_users()
        self.usersTable = self.findChild(QTableWidget, "usersTable")
        self.usersTable_Data = []
        self.usersTable.setRowCount(len(self.users))
        self.usersTable.setColumnCount(4)
        self.usersTable.setHorizontalHeaderLabels(["ID", "Name", "Password", "Status"])
        for i in range(0, len(self.users)):
            IdItem = QTableWidgetItem(str(self.users[i][0]))
            IdItem.setFlags(IdItem.flags() ^ Qt.ItemIsEditable)
            self.usersTable.setItem(i, 0, IdItem)
            self.usersTable.setItem(i, 1, QTableWidgetItem(str(self.users[i][1])))
            self.usersTable.setItem(i, 2, QTableWidgetItem(str(self.users[i][2])))
            comboBox = QComboBoxForAdmPAnel()
            comboBox.addItems(["Alumne", "Professor", "Admin"])
            if self.users[i][3] == 1:
                comboBox.setCurrentIndex(0)
            elif self.users[i][3] == 2:
                comboBox.setCurrentIndex(1)
            elif self.users[i][3] == 3:
                comboBox.setCurrentIndex(2)
            self.usersTable.setCellWidget(i, 3, comboBox)
            comboBox.activated.connect(lambda: self.status_change_comboBox(comboBox))
            self.usersTable_Data.append([IdItem,
                                         str(self.users[i][1]),
                                         str(self.users[i][2]),
                                         self.users[i][3]])

    def status_change_comboBox(self, comboBox):
        

    def update_data(self):
        for i in range(0, len(self.users)):
            for j in range(0, 4):
                print(self.usersTable.item(i, j))
        #for i in range(0, len(self.users)):
        #    change_user_password(self.usersTable.item(i, 2).text(), self.users[i][1])
        #    new_status = self.usersTable.item(i, 3).text()
        #    if new_status == "Alumne":
        #        new_status = 1
        #    elif new_status == "Professor":
        #        new_status = 2
        #    elif new_status == "Admin":
        #        new_status = 3
        #    change_user_status(3, self.users[i][1])
        #    change_user_name(self.usersTable.item(i, 1).text(), self.users[i][1])