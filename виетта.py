import sqlite3

class Podkl:
    def __init__(self, dbfile):
        self.connect = sqlite3.connect(dbfile)
        self.cursor = self.connect.cursor()

    def show(self):
        a = self.cursor.execute('SELECT * FROM users')
        return a.fetchall()

    def add(self, name):
        if (self.cursor.execute('SELECT * FROM users WHERE "name" = (?)', (name,))).fetchall():
            raise ValueError('Уже есть')
        else:
            self.cursor.execute('INSERT INTO users (name) values (?)', (name,))
            return self.connect.commit()

    def show_is(self, _id):
        a = self.cursor.execute('SELECT * FROM users WHERE "id" = (?)', (_id,))
        return a.fetchall()

    def delete(self, name):
        self.cursor.execute('DELETE FROM users WHERE "name" = (?)', (name,))
        return self.connect.commit()


db = Podkl('test.db')
db.add('Johan')
print(db.show())
