import sqlite3

#creates tables: Users, Accessibilities, Comments
def create_tables():
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Users
    (Username VARCHAR NOT NULL,
    Password VARCHAR NOT NULL,
    FirstName VARCHAR NOT NULL,
    LastName VARCHAR NOT NULL)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Accessibilities
    (Place_ID VARCHAR NOT NULL,
    Access_Type VARCHAR NOT NULL,
    Average_Rating VARCHAR NOT NULL,
    User_Ratings VARCHAR NOT NULL,
    PRIMARY KEY (Place_ID, Access_Type))""")
    c.execute("""CREATE TABLE IF NOT EXISTS Comments
    (Place_ID VARCHAR NOT NULL,
    Access_Type VARCHAR NOT NULL,
    User VARCHAR NOT NULL,
    Comment VARCHAR NOT NULL,
    PRIMARY KEY (Place_ID, Access_Type, User))""")

#checks whether or not a username already exists in the Users table
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

#createsa new user in the Users table
def new_user(username, password, first_name, last_name):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""INSERT INTO Users VALUES (?, ?, ?, ?)""", (username, password, first_name, last_name))
    database.commit()
    database.close()

#will call the place accessibility ratings
def place_access(place_ID):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    pass

#will call the place's comments
def place_comments(place_ID):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    pass

