import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
c = conn.cursor()
sql = '''
    CREATE TABLE BOOKS(
        BOOK_ID NUMBER NOT NULL,
        TITLE VARCHAR(50),
        PUBLISHED_DATE VARCHAR(50),
        PUBLISHER VARCHAR(50),
        PAGES NUMBER,
        RECOMMEND NUMBER,
        CONSTRAINT PK_BOOK PRIMARY KEY (BOOK_ID)
    )'''
sql2 = 'CREATE SEQUENCE BOOK_SEQ START WITH 1 INCREMENT BY 1'

item = ('데이터분석실무', '2020-04-05', '위키북스', 300, 10)
sql3 = '''INSERT INTO BOOKS VALUES(BOOK_SEQ.NEXTVAL, :1, :2, :3, :4, :5)'''

sql4 = 'select * from books where book_id = :id'
c.execute(sql4, id =1)
print(c.fetchall())
c.close()
conn.close()\

