from imports import *
from database import (get_current_user_by_id, get_class_by_id, get_lines_by_class_id, get_all_users, insert_line,
                      change_class_row_count, change_class_column_count, delete_line, insert_column,
                      get_columns_by_class_id, change_column_order, delete_column, insert_note, update_note,
                      get_note)


class AddStudent(QDialog):
    def __init__(self, class_notes_window):
        super(AddStudent, self).__init__()
        self.class_notes_window = class_notes_window

        loadUi("D_add_student.ui", self)
        self.addButton = self.findChild(QPushButton, "addButton")
        self.addButton.clicked.connect(self.add_students)
        self.cancelButton = self.findChild(QPushButton, "cancelButton")
        self.cancelButton.clicked.connect(self.close)

        self.students = []
        self.studentsTable = self.findChild(QTableWidget, "studentsTable")
        header = self.studentsTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fill_students()

    def fill_students(self):
        entered_students_id = []
        for i in range(len(self.class_notes_window.lines)):
            entered_students_id.append(str(self.class_notes_window.lines[i][2]))
        self.students = get_all_users()
        n = 0
        for i in range(len(self.students)):
            i -= n
            if str(self.students[i][0]) in entered_students_id:
                n += 1
                del self.students[i]
        self.studentsTable.setRowCount(len(self.students))
        for i in range(len(self.students)):
            name = QTableWidgetItem(str(self.students[i][1]))
            name.setFlags(name.flags() ^ Qt.ItemIsEditable)
            self.studentsTable.setItem(i, 0, name)
            self.studentsTable.setCellWidget(i, 1, QCheckBox())

    def add_students(self):
        n = 0
        for i in range(len(self.students)):
            if self.studentsTable.cellWidget(i, 1).isChecked() is True:
                insert_line(self.class_notes_window.class_id, self.students[i][0])
                n += 1
        n += self.class_notes_window.cur_class[3]
        change_class_row_count(n, self.class_notes_window.cur_class[0])
        self.class_notes_window.cur_class = get_class_by_id(self.class_notes_window.class_id)
        self.close()


class DeleteStudent(QDialog):
    def __init__(self, class_notes_window):
        super(DeleteStudent, self).__init__()
        self.class_notes_window = class_notes_window

        loadUi("D_delete_student.ui", self)
        self.delButton = self.findChild(QPushButton, "delButton")
        self.delButton.clicked.connect(self.del_students)
        self.cancelButton = self.findChild(QPushButton, "cancelButton")
        self.cancelButton.clicked.connect(self.close)

        self.studentsTable = self.findChild(QTableWidget, "studentsTable")
        header = self.studentsTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fill_students()

    def fill_students(self):
        self.studentsTable.setRowCount(len(self.class_notes_window.lines))
        for i in range(len(self.class_notes_window.lines)):
            name = QTableWidgetItem(get_current_user_by_id(str(self.class_notes_window.lines[i][2]))[1])
            name.setFlags(name.flags() ^ Qt.ItemIsEditable)
            self.studentsTable.setItem(i, 0, name)
            self.studentsTable.setCellWidget(i, 1, QCheckBox())

    def del_students(self):
        n = self.class_notes_window.cur_class[3]
        for i in range(len(self.class_notes_window.lines)):
            if self.studentsTable.cellWidget(i, 1).isChecked() is True:
                delete_line(self.class_notes_window.lines[i][0])
                n -= 1
        change_class_row_count(n, self.class_notes_window.cur_class[0])
        self.class_notes_window.cur_class = get_class_by_id(self.class_notes_window.class_id)
        self.close()


class AddColumn(QDialog):
    def __init__(self, class_notes_window):
        super(AddColumn, self).__init__()
        self.class_notes_window = class_notes_window

        loadUi("D_add_column.ui", self)
        self.cancelButton = self.findChild(QPushButton, "cancelButton")
        self.cancelButton.clicked.connect(self.close)
        self.createButton = self.findChild(QPushButton, "createButton")
        self.createButton.clicked.connect(self.create_column)
        self.enterNameLineEdit = self.findChild(QLineEdit, "enterNameLineEdit")

    def create_column(self):
        insert_column(self.enterNameLineEdit.text(), self.class_notes_window.class_id,
                      self.class_notes_window.cur_class[4] + 1)
        change_class_column_count(self.class_notes_window.cur_class[4] + 1, self.class_notes_window.class_id)
        self.class_notes_window.cur_class = get_class_by_id(self.class_notes_window.class_id)
        self.close()


class DeleteColumn(QDialog):
    def __init__(self, class_notes_window):
        super(DeleteColumn, self).__init__()
        self.class_notes_window = class_notes_window

        loadUi("D_delete_columns.ui", self)
        self.delButton = self.findChild(QPushButton, "delButton")
        self.delButton.clicked.connect(self.del_columns)
        self.cancelButton = self.findChild(QPushButton, "cancelButton")
        self.cancelButton.clicked.connect(self.close)

        self.columnsTable = self.findChild(QTableWidget, "columnsTable")
        header = self.columnsTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fill_columns()

    def fill_columns(self):
        self.columnsTable.setRowCount(len(self.class_notes_window.columns))
        for i in range(len(self.class_notes_window.columns)):
            self.columnsTable.setItem(i, 0, QTableWidgetItem(str(self.class_notes_window.columns[i][2])))
            self.columnsTable.setItem(i, 1, QTableWidgetItem(str(self.class_notes_window.columns[i][3])))
            self.columnsTable.setCellWidget(i, 2, QCheckBox())

    def del_columns(self):
        n = self.class_notes_window.cur_class[4]
        for i in range(len(self.class_notes_window.columns)):
            if self.columnsTable.cellWidget(i, 2).isChecked() is True:
                delete_column(self.class_notes_window.columns[i][0])
                n -= 1
        self.class_notes_window.columns = get_columns_by_class_id(self.class_notes_window.class_id)
        for i in range(len(self.class_notes_window.columns)):
            if i != (len(self.class_notes_window.columns) - 1):
                if self.class_notes_window.columns[i][3] != self.class_notes_window.columns[i + 1][3] - 1:
                    change_column_order(self.class_notes_window.columns[i][3] + 1, self.class_notes_window.columns[i + 1][0])
                    self.class_notes_window.columns = get_columns_by_class_id(self.class_notes_window.class_id)
            else:
                if self.class_notes_window.columns[i][3] != (len(self.class_notes_window.columns) + 1):
                    change_column_order(len(self.class_notes_window.columns[i][3]) + 1, self.class_notes_window.columns[i][0])
        self.class_notes_window.columns = get_columns_by_class_id(self.class_notes_window.class_id)
        change_class_column_count(n, self.class_notes_window.cur_class[0])
        self.class_notes_window.cur_class = get_class_by_id(self.class_notes_window.class_id)
        self.close()


class ClassNotes(QWidget):
    def __init__(self, class_list, class_id):
        super(ClassNotes, self).__init__()
        self.class_list = class_list
        self.class_id = class_id
        self.cur_class = get_class_by_id(self.class_id)

        loadUi("W_class_notes.ui", self)
        self.userLabel = self.findChild(QLabel, "userLabel")
        self.userLabel.setText(self.class_list.current_user[1])
        self.backButton = self.findChild(QPushButton, "backButton")
        self.addStudentButton = self.findChild(QPushButton, "addStudentButton")
        self.addStudentButton.clicked.connect(self.add_students)
        self.deleteStudentButton = self.findChild(QPushButton, "deleteStudentButton")
        self.deleteStudentButton.clicked.connect(self.delete_students)
        self.addColumnButton = self.findChild(QPushButton, "addColumnButton")
        self.addColumnButton.clicked.connect(self.add_column)
        self.deleteColumnButton = self.findChild(QPushButton, "deleteColumnButton")
        self.deleteColumnButton.clicked.connect(self.delete_column)
        self.saveButton = self.findChild(QPushButton, "saveButton")
        self.saveButton.clicked.connect(self.save_notes)
        self.statusLabel = self.findChild(QLabel, "statusLabel")

        self.lines = []
        self.columns = []
        self.notesTable = self.findChild(QTableWidget, "notesTable")
        header = self.notesTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fill_notes()

    def fill_notes(self):
        self.lines = get_lines_by_class_id(self.class_id)
        self.columns = get_columns_by_class_id(self.class_id)
        self.notesTable.setRowCount(self.cur_class[3])
        self.notesTable.setColumnCount(self.cur_class[4])
        header = self.notesTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        for i in range(len(self.lines)):
            name = QTableWidgetItem(str(get_current_user_by_id(self.lines[i][2])[1]))
            name.setFlags(name.flags() ^ Qt.ItemIsEditable)
            self.notesTable.setItem(i, 0, name)
        for i in range(1, len(self.columns) + 1):
            self.notesTable.setHorizontalHeaderItem(i, QTableWidgetItem(str(self.columns[i - 1][2])))
        for i in range(len(self.lines)):
            for j in range(1, len(self.columns) + 1):
                try:
                    self.notesTable.setItem(i, j, QTableWidgetItem(str(get_note(self.lines[i][0],
                                                                                self.columns[j][0])[0][2])))
                except:
                    self.notesTable.setItem(i, j, QTableWidgetItem(str(0)))


    def save_notes(self):
        flag = False
        for i in range(len(self.lines)):
            for j in range(1 ,len(self.columns) + 1):
                if self.notesTable.item(i, j) is None:
                    note = 0
                else:
                    note = self.notesTable.item(i, j).text()
                try:
                    note = int(note)
                except:
                    self.statusLabel.setText("El valor introduït no és un número!")
                    flag = True
                    break
            if flag:
                break
        if not flag:
            for i in range(len(self.lines)):
                for j in range(1 ,len(self.columns) + 1):
                    if self.notesTable.item(i, j) is None:
                        note = 0
                    else:
                        note = self.notesTable.item(i, j).text()
                    if not get_note(self.lines[i][0], self.columns[j - 1][0]):
                        insert_note(note, self.lines[i][0], self.columns[j - 1][0])
                    else:
                        update_note(note, self.lines[i][0], self.columns[j - 1][0])
                    self.statusLabel.setText("Tot està bé!")

    def add_students(self):
        dlg = AddStudent(self)
        dlg.exec()
        self.fill_notes()

    def delete_students(self):
        dlg = DeleteStudent(self)
        dlg.exec()
        self.fill_notes()

    def add_column(self):
        dlg = AddColumn(self)
        dlg.exec()
        self.fill_notes()

    def delete_column(self):
        dlg = DeleteColumn(self)
        dlg.exec()
        self.fill_notes()