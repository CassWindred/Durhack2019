import sqlite3

#creates tables: Users, Accessibilities, Comments
def create_tables():
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Users
    (Username VARCHAR PRIMARY KEY,
    Password VARCHAR NOT NULL,
    FirstName VARCHAR NOT NULL,
    LastName VARCHAR NOT NULL)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Accessibilities
    (LocationID VARCHAR NOT NULL,
    AccessType VARCHAR NOT NULL,
    User VARCHAR NOT NULL,
    ZeroStar INTEGER,
    OneStar INTEGER,
    TwoStar INTEGER,
    ThreeStar INTEGER,
    FourStar INTEGER,
    FiveStar INTEGER,
    FOREIGN KEY (User) REFERENCES Users (Username),
    PRIMARY KEY (LocationID, AccessType, User))""")
    c.execute("""CREATE TABLE IF NOT EXISTS Comments
    (LocationID VARCHAR NOT NULL,
    AccessType VARCHAR NOT NULL,
    User VARCHAR NOT NULL,
    Comment VARCHAR,
    FOREIGN KEY (LocationID, AccessType, User) REFERENCES Accessibilities (LocationID, AccessType, User),
    PRIMARY KEY (LocationID, AccessType, User))""")

#creates a new user in the Users table
def new_user(Username, Password, FirstName, LastName):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    try:
        c.execute("""INSERT INTO Users VALUES (?, ?, ?, ?)""", (Username, Password, FirstName, LastName))
    except:
        return False
    database.commit()
    database.close()

#creates a new location in the Accessibilities table
def new_location(LocationID, AccessType, User):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    try:
        c.execute("""INSERT INTO Accessibilities(LocationID, AccessType, User, ZeroStar, OneStar, TwoStar, ThreeStar, FourStar, FiveStar) VALUES (?, ?, ?, 0, 0, 0, 0, 0, 0)""", (LocationID, AccessType, User))
    except:
        return False
    database.commit()
    database.close()

#creates a new comment in the Comments table
def new_comment(LocationID, AccessType, User, Comment):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    try:
        c.execute("""INSERT INTO Comments(LocationID, AccessType, User, Comment) VALUES (?, ?, ?, ?)""", (LocationID, AccessType, User, Comment))
    except:
        return False
    database.commit()
    database.close()

#updates rating 
def add_rating(LocationID, AccessType, User, Star):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT {0} FROM Accessibilities WHERE LocationID = ? AND AccessType = ? AND User = ? """.format(Star), (LocationID, AccessType, User))
    number = c.fetchall()
    number = number[0][0] + 1
    c.execute("""UPDATE Accessibilities SET {0} = ? WHERE LocationID = ? AND AccessType = ? AND User = ? """.format(Star), (number, LocationID, AccessType, User))
    database.commit()
    database.close()

#gets rating for a location
def get_ratings(LocationID):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT AccessType, ZeroStar, OneStar, TwoStar, ThreeStar, FourStar, FiveStar FROM Accessibilities WHERE LocationID = ? """, (LocationID))
    locations = c.fetchall()
    print(locations)
    access_list = []
    for i in range(0, len(locations)):
        access_list.append({"Access Type" : None, "Average Rating" : None, "Number of Ratings" : None})
        access_list[i]["Access Type"] = locations[i][0]
        access_list[i]["Number of Ratings"] = locations[i][1] + locations[i][2] + locations[i][3] + locations[i][4] + locations[i][5] + locations[i][6]
        if access_list[i]["Number of Ratings"] == 0:
            access_list[i]["Average Rating"] = "Not yet rated"
        else:
            access_list[i]["Average Rating"] = round(((locations[i][2] * 1) + (locations[i][3] * 2) + (locations[i][4] * 3) + (locations[i][5] * 4) +
                                                (locations[i][6] * 5)) / access_list[i]["Number of Ratings"], 1)
    return access_list

# will call the place's comments
def get_comments(LocationID):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT AccessType, User, Comment FROM Comments WHERE LocationID = ? """, (LocationID))
    comments = c.fetchall()
    comments_list = []
    for i in range(0, len(comments)):
        comments_list.append({"Access Type": None, "User": None, "Comment": None})
        comments_list[i]["Access Type"] = comments[i][0]
        comments_list[i]["User"] = comments[i][1]
        comments_list[i]["Comment"] = comments[i][2]
    return comments_list

def check_if_password_is_correct(Username, Password):
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT * FROM Users WHERE Username = ? AND Password = ? """, (Username, Password))
    login = c.fetchall()
    if login == []:
        return False
    else:
        return True
