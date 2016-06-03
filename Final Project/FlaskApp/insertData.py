import sqlite3
conn = sqlite3.connect("profiles.db")
cursor = conn.cursor()
sql = "insert into members values (?, ?, ?, ?, ?, ?)"
data = ("Snow", "White", 21, "sw@disney.org", "http://www.nphinity.com/pics/sw.jpg",
        "Pursued by a jealous queen, hides with the dwarfs, the queen tries to feed Snow White a poison apple")\
    , ("Darth", "Vadar", 29, "dv@darkside.me", "http://www.nphinity.com/pics/dv.jpg",
       "Once a heroic Jedi Knight but was seduced by the dark side of the Force, became a Sith Lord, led the Empire's eradication of the Jedi Order")\
    , ("Taylor", "Swift", 25, "ts@1989.us", "http://www.nphinity.com/pics/ts.jpg",
       "American signer-songwriter, raised in Wyomissing Tennessee, signed to Big Machine Label")
cursor.executemany(sql, data)
conn.commit()
conn.close()