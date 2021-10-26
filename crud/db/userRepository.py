import sqlite3

def findById(id):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    execute = cursor.execute("select * from user where id =?", (id,)).fetchone()
    conn.close()
    return execute


def findByEmail(email):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    execute = cursor.execute("select * from user where email =?", (email,)).fetchone()
    conn.close()
    return execute


def findALl():
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    execute = cursor.execute('''select * from user''').fetchall()
    conn.close()
    return execute


def permit(user):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    cursor.execute('''insert into user(email, password) values(?, ?)''', (user.email, user.password))
    conn.commit()
    conn.close()


def remove(id):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    cursor.execute('''delete from user where id = ?''', (id,))
    conn.commit()
    conn.close()


def update(user):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    cursor.execute('''update user set password=? where id=?'''(user.password, user.id))
    conn.commit()
    conn.close()

