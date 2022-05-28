import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

#c.execute("""CREATE TABLE places (         place text                     )""")
c.execute("INSERT INTO places VALUES ('ica')")

#c.execute("SELECT* FROM places WHERE place
#print(c.fetchall())
conn.commit()

conn.close()
