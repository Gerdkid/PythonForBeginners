import sqlite3

db = sqlite3.connect('database.db')
db.row_factory = sqlite3.Row
table = db.execute('select * from person')
for each in table:
    print(dict(each))
    print(each['lastname'])
