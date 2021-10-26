import sqlite3


def findById(id):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    execute = cursor.execute("select * from board where id =?", (id,)).fetchone()
    conn.close()
    return execute


def findALl():
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    execute = cursor.execute('''select * from board''').fetchall()
    conn.close()
    return execute


def findByOffsetWithLimit(offset, limit):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    execute = cursor.execute('''select * from board limit ? offset ?''', (limit, offset)).fetchall()
    conn.close()
    return execute


def permit(board):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    cursor.execute('''insert into board(title,context,writer,regdate,fixdate) values(?,?,?,datetime('now','localtime'),datetime('now','localtime'))''', (board.title,board.context,board.writer))
    conn.commit()
    conn.close()


def remove(id):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    cursor.execute('''delete from board where id = ?''', (id,))
    conn.commit()
    conn.close()


def update(board):
    conn = sqlite3.connect('wanted.db')
    cursor = conn.cursor()
    cursor.execute('''update user set title=?, context=?, fixdate=datetime('now','localtime') where id=?'''(board.title, board.context, board.id))
    conn.commit()
    conn.close()
