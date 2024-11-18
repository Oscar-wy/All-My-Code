import sqlite3
import uuid

def InitialiseTables():
    try:
        with sqlite3.connect("Data.db") as db:
            cursor = db.cursor()
            sql = """CREATE TABLE IF NOT EXISTS User(
                     UUID TEXT UNIQUE
                     NID TEXT UNIQUE
                     FName varchar(20)
                     LName varchar(20)
                     Email TEXT UNIQUE
                     Password TEXT UNIQUE
                     PRIMARY KEY(UUID))
            """
            cursor.execute(sql)
            db.commit()
    except sqlite3.Error as err:
        print(err)

class User():
    def __init__(self):
        self.UUID = ""
        self.NID = ""
        self.FName = ""
        self.LName = ""
        self.Email = ""
        self.Password = ""
        self.SessionID = ""
        self.Got = False
    def CheckUsernameExists(self, Username):
        Values = (Username,)
        try:
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT Password FROM User
                         WHERE NID = ?
                """
                cursor.execute(sql, Values)
                result = cursor.fetchone()
                if Username == result:
                    return False
                return True
        except sqlite3.Error as err:
            print(err)
            return True
    def SetUser(self):
    def CreateUser(self, Username, FName, LName, Email, Password):
        try:
            if self.CheckUsernameExists(Username):
                self.UUID = str(uuid.uuid4).replace("-","")
                self.NID = Username
                self.FName = FName
                self.LName = LName
                self.Email = Email
                self.Password = Password
                self.SessionID = str(uuid.uuid4).replace("-","")
                if self.SetUser():
                    return True
                return False
        except:
            return False
    