import sqlite3

db = sqlite3.connect('database.db')
db.execute('update person set firstname="Josh" where lastname="gerding"')
db.commit()
