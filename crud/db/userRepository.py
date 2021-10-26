import sqlite3
from utils import query

db = 'wanted.db'

def findById(id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    execute = cursor.execute(query.select_user_by_id, (id,)).fetchone()
    conn.close()
    return execute


def findByEmail(email):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    execute = cursor.execute(query.select_user_by_email, (email,)).fetchone()
    conn.close()
    return execute


def findALl():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    execute = cursor.execute(query.select_user_all).fetchall()
    conn.close()
    return execute


def permit(user):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    roles = ",".join(user.roles)
    cursor.execute(query.insert_user, (user.email, roles, user.password))
    conn.commit()
    conn.close()


def remove(id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query.delete_user_by_id, (id,))
    conn.commit()
    conn.close()


def update(user):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query.update_user, (user.password, user.id))
    conn.commit()
    conn.close()

