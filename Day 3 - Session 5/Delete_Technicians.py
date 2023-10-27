import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("DELETE FROM employee WHERE role='technician'")
conn.commit()
conn.close()
