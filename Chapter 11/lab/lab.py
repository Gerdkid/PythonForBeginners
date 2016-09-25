import sqlite3


class LogDatabase:
    def __init__(self, name):
        self.databaseName = name
        db = sqlite3.connect(self.databaseName)
        db.execute('create table LogMessages (message text)')
        db.commit()
        db.close()

    def read(self):
        db = sqlite3.connect(self.databaseName)
        table = db.execute('select * from LogMessages')
        for each in table:
            print(each)
        db.close()

    def write(self, message):
        db = sqlite3.connect(self.databaseName)
        db.execute('insert into LogMessages (message) values (?)', (message,))
        db.commit()
        db.close()

log = LogDatabase('mydb.db')
log.write('Testing')
log.write('Test')
log.read()
