from imports import *
from database import get_all_users, get_current_user_by_name, change_user_name, change_user_password, change_user_status


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
        self.userLabel = self.findChild(QLabel, "userLabel")
        self.statusLabel = self.findChild(QLabel, "statusLabel")

        self.users = get_all_users()
        self.names = []
        for name in self.users:
            self.names.append(str(name[1]))
        self.names_copy = self.names.copy()
        self.usersTable = self.findChild(QTableWidget, "usersTable")
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
            comboBox.addItems(["Alumne", "Professor"])
            if self.users[i][3] == 1:
                comboBox.setCurrentIndex(0)
            elif self.users[i][3] == 2:
                comboBox.setCurrentIndex(1)
            elif self.users[i][3] == 3:
                comboBox.addItem("Admin")
                comboBox.setCurrentIndex(2)
                comboBox.setEnabled(False)
            self.usersTable.setCellWidget(i, 3, comboBox)
            comboBox.activated.connect(lambda: self.status_change_comboBox(comboBox))

    def status_change_comboBox(self, comboBox):
        pass

    def update_data(self):
        for i in range(0, len(self.users)):
            if self.usersTable.item(i, 1).text() != '' and self.usersTable.item(i, 2).text() != '':
                if str(self.users[i][2]) != self.usersTable.item(i, 2).text():
                    change_user_password(self.usersTable.item(i, 2).text(), self.users[i][1])
                    self.statusLabel.setText("Tot està bé.")
                new_status = self.usersTable.cellWidget(i, 3).currentIndex()
                new_status += 1
                if self.users[i][3] != new_status:
                    change_user_status(new_status, self.users[i][1])
                    self.statusLabel.setText("Tot està bé.")
                if str(self.users[i][1]) != self.usersTable.item(i, 1).text():
                    self.names_copy[i] = self.usersTable.item(i, 1).text()
                    if self.names_copy.count(self.usersTable.item(i, 1).text()) > 1:
                        self.names_copy = self.names.copy()
                        self.statusLabel.setText("Es repeteix un dels noms.")
                    else:
                        self.names = self.names_copy.copy()
                        self.userLabel.setText(self.usersTable.item(i, 1).text())
                        change_user_name(self.usersTable.item(i, 1).text(), str(self.users[i][1]))
                        self.statusLabel.setText("Tot està bé.")
            else:
                self.statusLabel.setText("Un dels camps no està emplenat.")
                break