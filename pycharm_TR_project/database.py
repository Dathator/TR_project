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
    data = (name)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users WHERE nameSurname=?""", data)
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