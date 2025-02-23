from imports import *
from database import get_columns_by_class_id, get_note, get_line_by_studetID_and_classID, get_current_user_by_id


class StudentNotes(QWidget):
    def __init__(self, class_id, cur_userID):
        super(StudentNotes, self).__init__()
        self.class_id = class_id
        self.cur_userID = cur_userID

        loadUi("W_student_notes.ui", self)
        self.userLabel = self.findChild(QLabel, "userLabel")
        self.backButton = self.findChild(QPushButton, "backButton")
        self.updateButton = self.findChild(QPushButton, "updateButton")
        self.updateButton.clicked.connect(self.fill_table)

        self.columns = []
        self.notesTable = self.findChild(QTableWidget, "notesTable")
        header = self.notesTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fill_table()

    def fill_table(self):
        self.columns = get_columns_by_class_id(self.class_id)
        self.notesTable.setRowCount(1)
        self.notesTable.setColumnCount(len(self.columns) + 1)
        lineID = get_line_by_studetID_and_classID(self.cur_userID, self.class_id)[0][0]
        name = QTableWidgetItem(str(get_current_user_by_id(self.cur_userID)[1]))
        name.setFlags(name.flags() ^ Qt.ItemIsEditable)
        self.notesTable.setItem(0, 0, name)
        for i in range(1, len(self.columns) + 1):
            self.notesTable.setHorizontalHeaderItem(i, QTableWidgetItem(str(self.columns[i - 1][2])))
        for i in range(1, len(self.columns) + 1):
            self.notesTable.setItem(0, i, QTableWidgetItem(str(get_note(lineID, self.columns[i - 1][0])[0][2])))