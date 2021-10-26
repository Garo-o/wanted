import sqlite3

def create(conn):

    cursor = conn.cursor()

    create_table = '''CREATE TABLE if not exists USER (
    ID INTEGER PRIMARY KEY,
    EMAIL TEXT NOT NULL UNIQUE,
    PASSWORD TEXT NOT NULL
    )'''
    cursor.execute(create_table)

    create_table = '''CREATE TABLE if not exists BOARD(
    ID INTEGER PRIMARY KEY,TITLE TEXT NOT NULL,
    CONTEXT TEXT NOT NULL,WRITER TEXT NOT NULL,
    REGDATE TEXT not null, 
    FIXDATE text not null
    )'''
    cursor.execute(create_table)


def drop(conn):
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE USER''')
    cursor.execute('''DROP TABLE BOARD''')


def insertUser(conn):
    cursor = conn.cursor()
    cursor.execute('''insert into user(email, password) values('hon', '123')''')
    cursor.execute('''insert into user(email, password) values('HO', '123')''')
    cursor.execute('''insert into user(email, password) values('hong', '123')''')


def selectUser(conn):
    cursor = conn.cursor()
    execute = cursor.execute('''select * from user''')
    print(execute.fetchall())


def deleteUser(conn):
    cursor = conn.cursor()
    cursor.execute('''delete from user where id=1''')

def updateUser(conn):
    cursor = conn.cursor()
    cursor.execute('''update user set email='park', password='456' where id=2''')


def allUsers(conn):
    cursor = conn.cursor()
    return cursor.execute('''select * from user''').fetchall()


def insertBoard(conn):
    cursor = conn.cursor()
    cursor.execute('''insert into board(title,context,writer,regdate,fixdate) values('1','2','3',datetime('now','localtime'),datetime('now','localtime'))''')
    cursor.execute(
        '''insert into board(title,context,writer,regdate,fixdate) values('1','2','3',datetime('now','localtime'),datetime('now','localtime'))''')
    cursor.execute(
        '''insert into board(title,context,writer,regdate,fixdate) values('1','2','3',datetime('now','localtime'),datetime('now','localtime'))''')
    cursor.execute(
        '''insert into board(title,context,writer,regdate,fixdate) values('1','2','3',datetime('now','localtime'),datetime('now','localtime'))''')
    cursor.execute(
        '''insert into board(title,context,writer,regdate,fixdate) values('1','2','3',datetime('now','localtime'),datetime('now','localtime'))''')
    cursor.execute(
        '''insert into board(title,context,writer,regdate,fixdate) values('1','2','3',datetime('now','localtime'),datetime('now','localtime'))''')
    cursor.execute(
        '''insert into board(title,context,writer,regdate,fixdate) values('1','2','3',datetime('now','localtime'),datetime('now','localtime'))''')
    cursor.execute(
        '''insert into board(title,context,writer,regdate,fixdate) values('1','2','3',datetime('now','localtime'),datetime('now','localtime'))''')



def selectBoard(conn):
    cursor = conn.cursor()
    execute = cursor.execute('''select * from board''')
    print(execute.fetchall())


def selectBoardWithOffset(conn):
    cursor = conn.cursor()
    execute = cursor.execute('''select * from board limit 1 offset 0''')
    print(execute.fetchall())



conn = sqlite3.connect('wanted.db')
create(conn)
insertUser(conn)
selectUser(conn)
deleteUser(conn)
selectUser(conn)
updateUser(conn)
selectUser(conn)

insertBoard(conn)
# selectBoard(conn)
selectBoardWithOffset(conn)

drop(conn)
conn.commit()
conn.close()
