from imports import *


def insert_user(name, password):
    data = (name, password)
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO users (name&surname, password, usertype) VALUES (?, ?, ?)""", data)
    connection.commit()

def get_user(id):
    connection = connect("TR_users.db")
    cursor = connection.cursor()
    user = cursor.execute("""""", id)
    user.fetchall()
    return user