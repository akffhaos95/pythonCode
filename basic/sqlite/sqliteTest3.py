import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()

sql = 'SELECT * FROM STOCKS ORDER BY PRICE'
c.execute(sql)
rows = c.fetchall()

print(rows)
print(type(rows))

for i in rows:
    print(i)

c.close()
conn.close()