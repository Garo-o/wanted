import sqlite3
from utils import query

db = 'wanted.db'


def findById(id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    execute = cursor.execute(query.select_board_by_id, (id,)).fetchone()
    conn.close()
    return execute


def findALl():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    execute = cursor.execute(query.select_board_all).fetchall()
    conn.close()
    return execute


def findByOffsetWithLimit(offset, limit):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    execute = cursor.execute(query.select_board_offset, (limit, offset)).fetchall()
    conn.close()
    return execute


def permit(board):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query.insert_board, (board.title,board.context,board.writer))
    id = cursor.lastrowid
    conn.commit()
    conn.close()
    return id


def remove(id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query.delete_board_by_id, (id,))
    conn.commit()
    conn.close()


def update(board):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query.update_board, (board.title, board.context, board.hit, board.id))
    conn.commit()
    conn.close()
