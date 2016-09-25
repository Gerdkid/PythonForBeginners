import sqlite3

db = sqlite3.connect('database.db')
db.execute('delete from person where lastname="gerding"')
db.commit()
