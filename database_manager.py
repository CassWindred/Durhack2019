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

#will call the place accessibility ratings: access type = access
def place_access(place_ID):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT AccessType, Average_Rating, User_Ratings FROM Accessibilities WHERE PlaceID = ? """, (placeID))
    locations = c.fetchall()
    access_list = []
    for i in range(0, len(locations)):
        access_list.append({"Access Type" : None, "Average Rating" : None, "User Ratings" : None})
        access_list[i]["Access Type"] = locations[i][1]
        access_list[i]["Average Rating"] = locations[i][2]
        access_list[i]["User Ratings"] = locations[i][3]
    return access_list

#will call the place's comments
def place_comments(place_ID):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT AccessType, User, Comment FROM Comments WHERE PlaceID = ? """, (placeID))
    comments = c.fetchall()
    comments_list = []
    for i in range(0, len(comments)):
        access_list.append({"Access Type": None, "User": None, "Comment": None})
        access_list[i]["Access Type"] = comments[i][1]
        access_list[i]["Average Rating"] = comments[i][2]
        access_list[i]["User Ratings"] = comments[i][3]
    return comments_list

#adds a comment to the comments database
def add_comment(place_ID, Accessibility, User, comment):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""INSERT INTO Comments VALUES (?, ?, ?, ?)""", (place_ID, Accessibility, User, comment))
    database.commit()
    database.close()
