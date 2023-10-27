import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("UPDATE employee SET role='technician' WHERE role='Manager'")
conn.commit()
conn.close()
