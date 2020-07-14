import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()

symbol = 'RHAT'
#c.execute("SELECT * FROM STOCKS WHERE symbol = '%s' "%symbol)
print(c.fetchall())

t = ('RHAT')
sql = 'SELECT * FROM STOCKS WHERE symbol = ?'
c.execute(sql,t)
print(c.fetchall())

conn.close()