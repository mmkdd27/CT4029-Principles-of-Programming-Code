import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("SELECT * FROM employee")
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()
