import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()

sql = """CREATE TABLE IF NOT EXISTS employee( 
      id INTEGER PRIMARY KEY,
      First_Name TEXT,
      Last_Name TEXT,
      Department TEXT,
      phone INTEGER,
      role TEXT
)"""

sql1 = "INSERT INTO employee VALUES(1, 'joe', 'roagen', 'research and development', 67847563, 'janitor')"
#who would make a better janitor ?
sql2 = "INSERT INTO employee VALUES(2, 'optimal', 'prime', 'research and development', 43987357, 'Manager')"
#optimal prime,a liked manger in the department,some employees complain about the random motor smell he has
sql3 = "INSERT INTO employee VALUES(3, 'homo', 'hobo', 'sabotage', 38764523, 'saboteur')"
#homo hobo ,a queer homeless person who specializes in commercial sabotage
sql4 = "INSERT INTO employee VALUES(4, 'joe', 'doe', 'data entry', 84736389, 'data entry')"
#defenitly not a russian spy
sql5 = "INSERT INTO employee VALUES(5, 'some', 'guy', 'research and development', 87676544, 'Manager')"
sql6 = "INSERT INTO employee VALUES(6, 'amazing', 'spiderman', 'anthropology', 65476532, 'Anthropologist')"



c.execute(sql)
c.execute(sql1)
c.execute(sql2)
c.execute(sql3)
c.execute(sql4)
c.execute(sql5)
c.execute(sql6)

conn.commit()
conn.close()
