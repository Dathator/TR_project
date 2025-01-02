from imports import *


def insert_user(name, password):
    data = (name, password)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO users(nameSurname,password) VALUES(?,?)""", data)
    connection.commit()

def get_user(name, password):
    data = (name, password)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users WHERE nameSurname=? AND password=?""", data)
    user = cursor.fetchone()
    return user[0]