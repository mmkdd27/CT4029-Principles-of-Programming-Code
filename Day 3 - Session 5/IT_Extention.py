#is this even te intended answer ?
import sqlite3

conn = sqlite3.connect('employee1_extention.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS department (
      id INTEGER PRIMARY KEY,
      name TEXT
)""")

# Insert department data
c.execute("INSERT INTO department (name) VALUES ('Research and Development')")
c.execute("INSERT INTO department (name) VALUES ('Sabotage')")
c.execute("INSERT INTO department (name) VALUES ('Data Entry')")
c.execute("INSERT INTO department (name) VALUES ('Anthropology')")

c.execute("""CREATE TABLE IF NOT EXISTS employee(
      id INTEGER PRIMARY KEY,
      First_Name TEXT,
      Last_Name TEXT,
      Department_ID INTEGER,
      phone INTEGER,
      role TEXT,
      FOREIGN KEY (Department_ID) REFERENCES department(id)
)""")

c.execute("INSERT INTO employee VALUES(1, 'joe', 'rogan', 1, 67847563, 'janitor')")
c.execute("INSERT INTO employee VALUES(2, 'optimal', 'prime', 1, 43987357, 'Manager')")
c.execute("INSERT INTO employee VALUES(3, 'homo', 'hobo', 2, 38764523, 'saboteur')")
c.execute("INSERT INTO employee VALUES(4, 'joe', 'doe', 3, 84736389, 'data entry')")
c.execute("INSERT INTO employee VALUES(5, 'some', 'guy', 1, 87676544, 'Manager')")
c.execute("INSERT INTO employee VALUES(6, 'amazing', 'spider-man', 4, 65476532, 'Anthropologist')")

conn.commit()

c.execute("SELECT * FROM employee WHERE Department_ID = 1")
print("Employees from the IT department:")
print(c.fetchall())

c.execute("SELECT * FROM employee WHERE Department_ID = 1 AND role = 'Manager'")
print("Managers from the IT department:")
print(c.fetchall())

c.execute("DELETE FROM employee WHERE id = 2")

conn.commit()
conn.close()
