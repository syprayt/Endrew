import sqlite3
connection = sqlite3.connect("itstep_database.sl3", 5)
cur = connection.cursor()
#cur.execute("CREATE TABLE first_table (name TEXT);")
#cur.execute("INSERT INTO first_table (name, age) VALUES ('Andrey', '22');")
#cur.execute("DELETE first_table (name) VALUES ('Age');")
cur.execute("SELECT INTO first_table (name) VALUES ('Nick');")
connection.commit()
connection.close()