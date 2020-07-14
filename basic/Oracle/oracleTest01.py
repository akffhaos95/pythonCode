import cx_Oracle

conn = cx_Oracle.connect("hr/hr@localhost:1521/xe")
c = conn.cursor()
sql = "SELECT * FROM EMPLOYEES"

c.execute(sql)

for row in c:
    print(row)

conn.close()