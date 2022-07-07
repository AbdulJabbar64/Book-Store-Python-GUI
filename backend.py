import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer )")
        self.conn.commit()


    def add(self, title, year, author, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()
        # conn.close()

    def view(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        # conn.close()
        return rows

    def search(self, title="", year="", author="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        # conn.close()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        # conn.close()

    def update(self, id, title, year, author, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?  WHERE id=?",(title, author, year, isbn, id))
        self.conn.commit()
        # conn.close()

# connect()
# add("abc",2020,"xyz",123)
# add("xyz",1999,"abc",9087)
# print(view())
# print(search(author="abc"))
# delete(2)
# update(2,"qwe",2432,"nklda",536)
# print(view())
