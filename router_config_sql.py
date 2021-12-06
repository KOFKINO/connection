import sqlite3

conn = sqlite3.connect('config_sql.sqlite')
cursor = conn.cursor()
cursor.execute('create table config (ip varchar(40), config varchar(99999), config_md5 varchar(999))')