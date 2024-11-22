import sqlite3
import uuid
from flask import url_for

def InitialiseTables():
    try:
        with sqlite3.connect("Data.db") as db:
            cursor = db.cursor()
            sql = """CREATE TABLE IF NOT EXISTS User(
                     UUID TEXT UNIQUE,
                     NID TEXT UNIQUE,
                     ProfilePicture TEXT,
                     FName varchar(20),
                     LName varchar(20),
                     Email TEXT UNIQUE,
                     Password TEXT,
                     SessionID TEXT UNIQUE,
                     PRIMARY KEY(UUID));
            """
            cursor.execute(sql)
            db.commit()
    except sqlite3.Error as err:
        print(err)

class User():
    def __init__(self):
        self.UUID = ""
        self.NID = ""
        self.ProfilePic = ""
        self.FName = ""
        self.LName = ""
        self.Email = ""
        self.Password = ""
        self.SessionID = ""
    def SetupTables(self):
        try:
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
        except sqlite3.Error as err:
            print(err)
    def CheckUsernameExists(self, Username):
        Values = (Username,)
        try:
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT NID FROM User
                         WHERE NID = ?
                """
                cursor.execute(sql, Values)
                result = cursor.fetchone()
                print(result)
                if Username == result:
                    return False
                return True
        except sqlite3.Error as err:
            print(err)
            return True
    def SetUser(self):
        try:
            Values = (self.UUID, self.NID, self.ProfilePic, self.FName, self.LName, self.Email, self.Password, self.SessionID)
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """INSERT INTO User(UUID, NID, ProfilePicture, FName, LName, Email, Password, SessionID)
                         Values (?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(sql, Values)
                return True
        except sqlite3.Error as err:
            print(err)
            return False
    def CreateUser(self, Username, FName, LName, Email, Password):
        try:
            if self.CheckUsernameExists(Username):
                self.UUID = str(uuid.uuid4()).replace("-","")
                self.NID = Username
                self.FName = FName
                self.LName = LName
                self.Email = Email
                self.Password = Password
                self.ProfilePic = url_for('static', filename='PFP.png')
                self.SessionID = str(uuid.uuid4()).replace("-","")
                if self.SetUser():
                    return True
                return False
        except:
            return False
    def CheckPassword(self, Username, Password):
        try:
            Values = (Username, Username)
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT Password FROM User
                         WHERE NID = ? OR Email = ?
                """
                cursor.execute(sql, Values)
                result = ""
                try:
                    result, = cursor.fetchone()
                except:
                    result = None
                if result == Password:
                    return True
                return False
        except sqlite3.Error as err:
            print(err)
            return False
    def AssignUser(self, Input):
        try:
            Values = (Input, Input, Input)
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT * FROM User
                         WHERE NID = ? OR Email = ? OR SessionID = ?
                """
                cursor.execute(sql, Values)
                result = cursor.fetchone()
                self.UUID = result[0]
                self.NID = result[1]
                self.ProfilePic = result[2]
                self.FName = result[3]
                self.LName = result[4]
                self.Email = result[5]
                self.Password = result[6]
                self.SessionID = result[7]
                return True
        except:
            return False
    def GetUserProfile(self, Username):
        try:
            Values = (Username)
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT NID, FName, LName FROM User
                         WHERE NID = ?
                """
                cursor.execute(sql, Values)
                result = cursor.fetchall()
                return result
        except sqlite3.Error as err:
            print(err)
            return None
    def Login(self, UserEmail, Password):
        if self.CheckPassword(UserEmail, Password):
            if self.AssignUser(UserEmail):
                return True
        return False
    