import sqlite3

db = sqlite3.connect('database.db')
db.execute('drop table if exists person')
db.execute('create table person (firstname text, lastname text, age int)')
