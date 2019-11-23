import sqlite3

#creates tables: Users, Accessibilities, Comments
def create_tables():
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Accessibilities
    (Place_ID VARCHAR NOT NULL,
    Access_Type VARCHAR NOT NULL,
    0_Star INTEGER NOT NULL,
    1_Star INTEGER NOT NULL,
    2_Star INTEGER NOT NULL,
    3_Star INTEGER NOT NULL,
    4_Star INTEGER NOT NULL,
    5_Star INTEGER NOT NULL
    PRIMARY KEY (Place_ID, Access_Type))""")

#
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




