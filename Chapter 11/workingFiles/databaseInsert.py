import sqlite3

db = sqlite3.connect('database.db')
db.execute('insert into person (firstname, lastname, age) values ("joshua", "gerding", 21)')
db.commit()
