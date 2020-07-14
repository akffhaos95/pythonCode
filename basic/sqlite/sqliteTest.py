import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("create table if not exists stocks (data text, trans text, symbol text, qty real, price real)")

c.execute("insert into stocks values('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

conn.commit()
conn.close()