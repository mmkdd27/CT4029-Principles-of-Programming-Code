import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("SELECT * FROM employee WHERE role='Manager'")
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()
