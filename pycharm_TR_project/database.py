from imports import *


def insert_user(name, password):
    data = (name, password)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO users(nameSurname,password) VALUES(?,?)""", data)
    connection.commit()

def get_all_users():
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    return users

def get_current_user_by_name_password(name, password):
    data = (name, password)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users WHERE nameSurname=? AND password=?""", data)
    user = cursor.fetchone()
    user = (user[0], user[1], user[2], user[3])
    return user

def get_current_user_by_name(name):
    data = (name,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users WHERE nameSurname=?""", data)
    user = cursor.fetchone()
    user = (user[0], user[1], user[2], user[3])
    return user

def get_current_user_by_id(id):
    data = (id,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users WHERE userID=?""", data)
    user = cursor.fetchone()
    user = (user[0], user[1], user[2], user[3])
    return user

def change_user_name(new_data, user_name):
    data = (new_data, user_name)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE users SET nameSurname = ? WHERE nameSurname = ?""", data)
    connection.commit()

def change_user_password(new_data, user_name):
    data = (new_data, user_name)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE users SET password = ? WHERE nameSurname = ?""", data)
    connection.commit()

def change_user_status(new_data, user_name):
    data = (new_data, user_name)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE users SET userType = ? WHERE nameSurname = ?""", data)
    connection.commit()

def get_all_classes():
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM classes""")
    classes = cursor.fetchall()
    return classes

def get_classes_by_teacher_id(id):
    data = (id,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM classes WHERE teacherID=?""", data)
    classes = cursor.fetchall()
    return classes

def get_class_by_name(name):
    data = (name,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM classes WHERE className=?""", data)
    res = cursor.fetchone()
    res = (res[0], res[1], res[2], res[3], res[4])
    return res

def get_class_by_id(id):
    data = (id,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM classes WHERE classID=?""", data)
    res = cursor.fetchone()
    res = (res[0], res[1], res[2], res[3], res[4])
    return res

def get_classes_by_student_id(studentID):
    lines = get_lines_by_studentID(studentID)
    classes = []
    for i in lines:
        if i[1] not in classes:
            classes.append(get_class_by_id(i[1]))
    return classes

def insert_class(class_name, id):
    data = (class_name, id)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO classes(className,teacherID) VALUES(?,?)""", data)
    connection.commit()

def change_class_name(new_name, id):
    data = (new_name, id)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE classes SET className = ? WHERE classID = ?""", data)
    connection.commit()

def change_class_row_count(new_row_count, id):
    data = (new_row_count, id)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE classes SET rowCount = ? WHERE classID = ?""", data)
    connection.commit()

def change_class_column_count(new_column_count, id):
    data = (new_column_count, id)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE classes SET columnCount = ? WHERE classID = ?""", data)
    connection.commit()

def delete_class(id):
    data = (id,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM classes WHERE classID=?""", data)
    connection.commit()

def get_lines_by_studentID(studentID):
    data = (studentID,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM notesLine WHERE studentLinkID=?""", data)
    res = cursor.fetchall()
    return res

def get_line_by_studetID_and_classID(studentID, classID):
    data = (classID, studentID)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM notesLine WHERE (classLinkID, studentLinkID)=(?,?)""", data)
    res = cursor.fetchall()
    return res

def get_lines_by_class_id(class_id):
    data = (class_id,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM notesLine WHERE classLinkID=?""", data)
    res = cursor.fetchall()
    return res

def insert_line(classID, studentID):
    data = (classID, studentID)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO notesLine(classLinkID,studentLinkID) VALUES(?,?)""", data)
    connection.commit()

def delete_line(id):
    data = (id,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM notesLine WHERE lineID=?""", data)
    connection.commit()

def insert_column(name, class_id, orderNum):
    data = (class_id, name, orderNum)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO columns(classLinkID,columnName,orderNum) VALUES(?,?,?)""", data)
    connection.commit()

def get_columns_by_class_id(classID):
    data = (classID,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM columns WHERE classLinkID=?""", data)
    res = cursor.fetchall()
    return res

def change_column_order(new_orderNum, columnID):
    data = (new_orderNum, columnID)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE columns SET orderNum = ? WHERE columnID = ?""", data)
    connection.commit()

def delete_column(id):
    data = (id,)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM columns WHERE columnID=?""", data)
    connection.commit()

def insert_note(note, lineID, columnID):
    data = (lineID, note, columnID)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO notes(lineLinkID,note,columnLinkID) VALUES(?,?,?)""", data)
    connection.commit()

def get_note(lineID, columnID):
    data = (lineID, columnID)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM notes WHERE (lineLinkID, columnLinkID)=(?,?)""", data)
    res = cursor.fetchall()
    return res

def update_note(note, lineID, columnID):
    data = (note, lineID, columnID)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""UPDATE notes SET note = ? WHERE (lineLinkID, columnLinkID) = (?, ?)""", data)
    connection.commit()