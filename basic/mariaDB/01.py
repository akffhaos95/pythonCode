import pymysql

# conn = pymysql.connect(host="localhost", 
#         user="root", 
#         password="qwer1234", 
#         db="test",
#         charset="utf8",
#         cursorclass=pymysql.cursors.DictCursor
# )
# c = conn.cursor()

class Database():
    def create_conn(self):
        conn = pymysql.connect(
            host="localhost", 
            user="root", 
            password="qwer1234", 
            db="test",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    def create_table(self):
        conn = self.create_conn()
        c = conn.cursor()
        sql = '''
            CREATE TABLE if not exists BOOKS(
            BOOK_ID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
            TITLE TEXT,
            PUBLISHED_DATE TEXT,
            PUBLISHER TEXT,
            PAGES INTEGER,
            RECOMMEND INTEGER
            )DEFAULT CHARSET=utf8
        '''
        c.execute(sql)
        conn.commit()
        c.close()
    def select_all_books(self):
        conn = self.create_conn()
        c = conn.cursor()
        sql = 'SELECT * FROM BOOKS'
        c.execute(sql)
        books = c.fetchall()
        c.close()
        conn.close()
        return books
    def select_one_book(self, id):
        conn = self.create_conn()
        c = conn.cursor()
        sql = 'SELECT * FROM BOOKS WHERE BOOK_ID = %s'
        c.execute(sql, id)
        book = c.fetchone()
        c.close()
        conn.close()
        return book   
    def insert_books(self, item):
        conn = self.create_conn()
        c = conn.cursor()
        sql = 'INSERT INTO BOOKS (TITLE, PUBLISHED_DATE, PUBLISHER, PAGES, RECOMMEND) VALUES(%s,%s,%s,%s,%s)'
        c.execute(sql, item)
        conn.commit()
        c.close()
        conn.close()
    def update_book(self, name):
        conn = self.create_conn()
        c = conn.cursor()
        sql = 'UPDATE BOOKS SET TITLE = %s WHERE BOOK_ID = %s'
        c.execute(sql, name)
        conn.commit()
        c.close()
        conn.close()
    def delete_book(self, id):
        conn = self.create_conn()
        c = conn.cursor()
        sql = 'DELETE FROM BOOKS WHERE BOOK_ID = %s'
        c.executemany(sql, str(id))
        conn.commit()
        c.close()
        conn.close()
if __name__ == '__main__':
    db = Database()
    while True:
        num = int(input('''
            1. 테이블 생성
            2. 전체 데이터 가져오기
            3. 한 건의 데이터 가져오기
            4. 조건에 따라 데이터 가져오기
            5. 데이터 수정하기(제목 수정)
            6. 데이터 삭제하기
            7. 데이터 삽입하기
            8. 종료
            >>>>>
        '''))
        if num == 1:
            #1. 테이블 생성
            db.create_table()
        elif num == 2:
            a = db.select_all_books()
            print(a)
        elif num == 3:
            #3. 한 건의 데이터 가져오기
            a = db.select_all_books()
            print(a)
        elif num == 4:
            #4. 조건에 따라 데이터 가져오기
            id = input("검색할 책의 아이디 : ")
            a = db.select_one_book(id)
            print(a)
        elif num == 5:
            #5. 데이터 수정하기(제목 수정)
            id = input("수정할 책의 아이디 : ")
            name = input("수정할 책의 바꿀 제목 : ")
            db.update_book([name, id])
        elif num == 6:
            #6. 데이터 삭제하기
            id = input("삭제할 책의 아이디 : ")
            db.delete_book(id)
        elif num == 7:
            #7. 데이터 삽입하기    
            name = ['데이터분석','2020-03-02','위키',300,10]
            db.insert_books(name)
        elif num == 8:
            quit()


    