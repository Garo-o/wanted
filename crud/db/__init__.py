import sqlite3
from utils import query
import bcrypt

conn = sqlite3.connect('wanted.db')
cursor = conn.cursor()

create_table = query.user_table
cursor.execute(create_table)

create_table = query.board_table
cursor.execute(create_table)

password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())

if not cursor.execute('''select * from user where email = 'admin' ''').fetchone():
    cursor.execute('''insert into user(email, roles, password) values('admin', 'ROLE_USER,ROLE_ADMIN',?)''', (password,))

conn.commit()
conn.close()
