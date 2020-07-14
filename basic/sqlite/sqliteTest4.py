import sqlite3, csv

conn = sqlite3.connect('example.db')
c = conn.cursor()

sql = '''
    create table if not exists suppliers(
    supplier_name varchar(20),
    invoice_number varchar(20),
    part_number varchar(20),
    cost float,
    purchase_date date)
'''

c.execute(sql)
conn.commit()

file_reader = csv.reader(open('basic/sqlite/test.csv', 'r'), delimiter=',')
header = next(file_reader, None)

data = []
for row in file_reader:
    print(row)
    data.append(row)

sql = 'insert into suppliers values(?,?,?,?,?)'
c.executemany(sql, data)

conn.commit()

c.close()
conn.close()