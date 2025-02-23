from imports import *
from database import get_classes_by_student_id, get_current_user_by_id


class StudentsClassList(QWidget):
    def __init__(self, main_window):
        super(StudentsClassList, self).__init__()
        self.main_window = main_window

        loadUi("W_student_class_list.ui", self)
        self.backButton = self.findChild(QPushButton, "backButton")
        self.userLabel = self.findChild(QLabel, "userLabel")
        self.updateButton = self.findChild(QPushButton, "updateButton")
        self.updateButton.clicked.connect(self.fill_classes_table)

        self.classes = []
        self.classesTable = self.findChild(QTableWidget, "classesTable")
        header = self.classesTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fill_classes_table()

    def fill_classes_table(self):
        self.classes = get_classes_by_student_id(self.main_window.current_user[0])
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

    def open_class(self, id):
        self.main_window.show_w_student_notes(id)
        self.close()