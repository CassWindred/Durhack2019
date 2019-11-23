import sqlite3

def create_tables():
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Users
    (Username VARCHAR(20) PRIMARY KEY,
    Password BINARY(32) NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL)""")

def check_username(username):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    while True:
        c.execute("""SELECT Username FROM Users WHERE Username = ? """, (username,))
        existing_users = c.fetchall()
        if existing_users == []:
            return False
        else:
            return True
    
def new_user(username, password, first_name, last_name):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""INSERT INTO Users VALUES (?, ?, ?, ?)""", (username, password, first_name, last_name))
    database.commit()
    database.close()

def place_info(place_ID):




