import sqlite3

database = sqlite3.connect("database.db")
c = database.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Users
(Username VARCHAR(20) PRIMARY KEY,
Password BINARY(32) NOT NULL)""")


