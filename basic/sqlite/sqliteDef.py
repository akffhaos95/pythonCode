import sqlite3

class Database():
    def create_conn(self):
        conn = sqlite3.connect('my_books.db')
        return conn
    def create_table(self):
        conn = self.create_conn
        c = conn.cursor()
        sql = '''
            CREATE TABLE if not exists BOOKS(
            TITLE TEXT,
            PUBLISHED_DATE TEXT,
            PUBLISHER TEXT,
            PAGES INTEGER,
            RECOMMEND INTEGER
        )'''
        c.execute(sql)
        conn.commit()
        c.close()
    def insert_books(self, item):
        conn = self.create_conn
        c = conn.cursor()
        sql = 'INSERT INTO books VALUES(?,?,?,?,?)'
        c.execute(sql, item)
        conn.commit()
        c.close()
        conn.close()
    def insert_books2(self, items):
        conn = self.create_conn
        c = conn.cursor()
        sql = 'INSERT INTO books VALUES(?,?,?,?,?)'
        c.executemany(sql, items)
        conn.commit()
        c.close()
        conn.close()
    def all_books():
        conn = self.create_conn
        c = conn.cursor()
        sql = 'SELECT * FROM books'
        c.execute(sql)
        books = c.fetchall()
        c.close()
        conn.close()
        return books
    def one_book(self, title):
        conn = self.create_conn()
        c = conn.cursor()
        sql = 'SELECT * FROM books WHERE title like ?'
        title = "%" + title + "%"
        c.execute(sql, (title,))
        book = c.fetchone()
        c.close()
        conn.close()
        return book

if __name__ == '__main__':
    db = Database()
    q = '데이터 분석'
    a = db.one_book(q)
    print(a)