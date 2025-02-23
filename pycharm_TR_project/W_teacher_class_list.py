from imports import *
from database import (get_classes_by_teacher_id, get_all_classes, get_class_by_name, get_current_user_by_id,
                      insert_class, change_class_name, delete_class)


class CreateClass(QDialog):
    def __init__(self, window):
        super(CreateClass, self).__init__()

        loadUi("D_create_class.ui", self)
        self.enterNameLineEdit = self.findChild(QLineEdit, "enterNameLineEdit")
        self.createButton = self.findChild(QPushButton, "createButton")
        self.createButton.clicked.connect(self.create_but_clicked)
        self.cancelButton = self.findChild(QPushButton, "cancelButton")
        self.cancelButton.clicked.connect(self.close)
        self.statusLabel = self.findChild(QLabel, "statusLabel")
        self.window = window

    def create_but_clicked(self):
        if self.enterNameLineEdit.text() == '':
            self.statusLabel.setText("El camp no està emplenat.")
        else:
            try:
                get_class_by_name(self.enterNameLineEdit.text())
            except:
                insert_class(self.enterNameLineEdit.text(), self.window.current_user[0])
                self.close()
            else:
                self.statusLabel.setText("Ja existeix una classe amb aquest nom.")


class RenameClass(QDialog):
    def __init__(self, id):
        super(RenameClass, self).__init__()

        loadUi("D_rename_class.ui", self)
        self.enterNameLineEdit = self.findChild(QLineEdit, "enterNameLineEdit")
        self.renameButton = self.findChild(QPushButton, "renameButton")
        self.renameButton.clicked.connect(self.rename_but_clicked)
        self.cancelButton = self.findChild(QPushButton, "cancelButton")
        self.cancelButton.clicked.connect(self.close)
        self.statusLabel = self.findChild(QLabel, "statusLabel")
        self.id = id

    def rename_but_clicked(self):
        if self.enterNameLineEdit.text() == '':
            self.statusLabel.setText("El camp no està emplenat.")
        else:
            try:
                get_class_by_name(self.enterNameLineEdit.text())
            except:
                change_class_name(self.enterNameLineEdit.text(), self.id)
                self.close()
            else:
                self.statusLabel.setText("Ja existeix una classe amb aquest nom.")


class DeleteClass(QDialog):
    def __init__(self, id):
        super(DeleteClass, self).__init__()

        loadUi("D_delete_class.ui", self)
        self.okButton = self.findChild(QPushButton, "okButton")
        self.okButton.clicked.connect(self.delete)
        self.noButton = self.findChild(QPushButton, "noButton")
        self.noButton.clicked.connect(self.close)
        self.id = id

    def delete(self):
        delete_class(self.id)
        self.close()

class TeacherClassList(QWidget):
    def __init__(self, main_window):
        super(TeacherClassList, self).__init__()
        self.main_window = main_window

        loadUi("W_teacher_class_list.ui", self)
        self.userLabel = self.findChild(QLabel, "userLabel")
        self.backButton = self.findChild(QPushButton, "backButton")
        self.createClassButton = self.findChild(QPushButton, "createClassButton")
        self.createClassButton.clicked.connect(self.create_class)
        self.current_user = None

        self.classes = []
        self.classesTable = self.findChild(QTableWidget, "classesTable")
        header = self.classesTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def fill_classes(self):
        if self.current_user[3] == 2:
            self.classes = get_classes_by_teacher_id(self.current_user[0])
        elif self.current_user[3] == 3:
            self.classes = get_all_classes()
        self.classesTable.setRowCount(len(self.classes))
        for i in range(len(self.classes)):
            IdItem = QTableWidgetItem(str(self.classes[i][0]))
            IdItem.setFlags(IdItem.flags() ^ Qt.ItemIsEditable)
            self.classesTable.setItem(i, 0, IdItem)
            name = QTableWidgetItem(str(self.classes[i][1]))
            name.setFlags(name.flags() ^ Qt.ItemIsEditable)
            self.classesTable.setItem(i, 1, name)
            teachername = QTableWidgetItem(str(get_current_user_by_id(self.classes[i][2])[1]))
            teachername.setFlags(teachername.flags() ^ Qt.ItemIsEditable)
            self.classesTable.setItem(i, 2, teachername)
            open_but = QPushButton()
            open_but.setText("Abrir")
            open_but.released.connect(lambda ID = str(self.classes[i][0]): self.open_class(ID))
            self.classesTable.setCellWidget(i, 3, open_but)
            ren_but = QPushButton()
            ren_but.setText("Canvia el nom")
            ren_but.released.connect(lambda ID = str(self.classes[i][0]): self.rename_class(ID))
            self.classesTable.setCellWidget(i, 4, ren_but)
            del_but = QPushButton()
            del_but.setText("Suprimeix")
            del_but.released.connect(lambda ID = str(self.classes[i][0]): self.delete_class(ID))
            self.classesTable.setCellWidget(i, 5, del_but)

    def create_class(self):
        dlg = CreateClass(self)
        dlg.exec()
        self.fill_classes()

    def open_class(self, class_id):
        self.main_window.show_w_class_notes(self, class_id)
        self.close()

    def rename_class(self, id):
        dlg = RenameClass(id)
        dlg.exec()
        self.fill_classes()

    def delete_class(self, id):
        dlg = DeleteClass(id)
        dlg.exec()
        self.fill_classes()