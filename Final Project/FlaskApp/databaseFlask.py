import sqlite3
conn = sqlite3.connect("profiles.db")
cursor = conn.cursor()
sql = "create table members(firstname text, lastname text, age int, " \
      "email text PRIMARY KEY, photo text, bio text)"
cursor.execute(sql)
conn.commit()
conn.close()

