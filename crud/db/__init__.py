import sqlite3

conn = sqlite3.connect('wanted.db')
cursor = conn.cursor()

create_table = '''CREATE TABLE if not exists USER(ID INTEGER PRIMARY KEY,EMAIL TEXT NOT NULL UNIQUE,PASSWORD TEXT NOT NULL)'''
cursor.execute(create_table)

create_table = '''CREATE TABLE if not exists BOARD(ID INTEGER PRIMARY KEY,TITLE TEXT NOT NULL,CONTEXT TEXT NOT NULL,WRITER TEXT NOT NULL,REGDATE TEXT NOT NULL, FIXDATE TEXT)'''
cursor.execute(create_table)

conn.commit()
conn.close()