

user_table = '''CREATE TABLE if not exists USER(ID INTEGER PRIMARY KEY,EMAIL TEXT NOT NULL UNIQUE,ROLES TEXT,PASSWORD TEXT NOT NULL)'''
board_table = '''CREATE TABLE if not exists BOARD(ID INTEGER PRIMARY KEY,TITLE TEXT NOT NULL,CONTEXT TEXT NOT NULL,WRITER TEXT NOT NULL,REGDATE TEXT NOT NULL, hit integer)'''

select_user_by_id = '''select * from user where id =?'''
select_user_by_email = '''select * from user where email =?'''
select_user_all = '''select * from user'''

insert_user = '''insert into user(email, roles ,password) values(?, ?, ?)'''

delete_user_by_id = '''delete from user where id = ?'''

update_user = '''update user set password=? where id=?'''




select_board_by_id = '''select * from board where id =?'''
select_board_all = '''select * from board'''
select_board_offset = '''select *  from board order by regdate desc limit ? offset ?'''

insert_board = '''insert into board(title,context,writer,regdate,hit) values(?,?,?,datetime('now','localtime'),0)'''

delete_board_by_id = '''delete from board where id = ?'''

update_board = '''update board set title=?, context=?,hit=? where id=?'''
