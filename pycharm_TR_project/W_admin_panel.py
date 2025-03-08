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
        self.usersTable = self.findChild(QTableWidget, "usersTable")
        self.usersTable.setRowCount(len(self.users))
        self.usersTable.setColumnCount(4)
        self.usersTable.setHorizontalHeaderLabels(["ID", "Nom", "Contrasenya", "Status"])
        header = self.usersTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
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

    def update_data(self):
        new_names = []
        new_passwords = []
        cur_user_id = str(get_current_user_by_name(self.userLabel.text())[0])
        for i in range(0, len(self.users)):
            new_names.append(self.usersTable.item(i, 1).text())
            change_user_name(i, str(self.users[i][1]))
            new_passwords.append(self.usersTable.item(i, 2).text())
        for i in range(0, len(new_names)):
            if new_names[i] == '':
                self.statusLabel.setText("Un dels camps no està emplenat.")
                break
            elif new_names.count(new_names[i]) > 1:
                self.statusLabel.setText("Es repeteix un dels noms.")
                break
            else:
                self.statusLabel.setText("Tot està bé.")
                change_user_name(self.usersTable.item(i, 1).text(), i)
                if cur_user_id == self.usersTable.item(i, 0).text():
                    self.userLabel.setText(self.usersTable.item(i, 1).text())
            if new_passwords[i] == '':
                self.statusLabel.setText("Un dels camps no està emplenat.")
                break
            else:
                self.statusLabel.setText("Tot està bé.")
                change_user_password(self.usersTable.item(i, 2).text(), self.users[i][1])
            new_status = self.usersTable.cellWidget(i, 3).currentIndex()
            new_status += 1
            if str(self.users[i][3]) != str(new_status):
                change_user_status(new_status, self.users[i][1])
                self.statusLabel.setText("Tot està bé.")
            self.users = get_all_users()