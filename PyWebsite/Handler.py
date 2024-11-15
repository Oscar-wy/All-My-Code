import sqlite3
from datetime import date, timedelta
from calendar import monthrange
import uuid

def Initialise():
    # Creating tables if they dont exist
    with sqlite3.connect("Data.db") as db:
        cursor = db.cursor()
        # Creating User table
        sql = """CREATE TABLE IF NOT EXISTS User(
                 UUID TEXT UNIQUE,
                 NID TEXT UNIQUE,
                 Username TEXT,
                 FirstName VARCHAR(20),
                 LastName VARCHAR(20),
                 Email TEXT UNIQUE NOT NULL,
                 Password TEXT NOT NULL,
                 SessionID Text UNIQUE,
                 PRIMARY KEY(UUID));
              """
        cursor.execute(sql)

class Encryption:
    def LowEncrypt(Data, Type):
        if Type.lower() == "e":
            pass
        else:
            pass
    def HighEncrypt(Data, Type):
        if Type.lower() == "e":
            pass
        else:
            pass

class User:
    def __init__(self):
        self.UUID = ""
        self.NID = ""
        self.Username = ""
        self.Email = ""
        self.Password = ""
        self.FName = ""
        self.LName = ""
        self.SessionID = ""
        self.Got = False
    def CheckPassword(self, Username, Password):
        try:
            Values = (Username,)
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT Password FROM User
                         WHERE NID = ?
                """
                cursor.execute(sql, Values)
                result = cursor.fetchone()
                if Password == result:
                    return True
                return False
        except sqlite3.Error as err:
            print(err)
            return False
    def Login(self, Username, Password):
        try:
            if self.CheckPassword(Username, Password):
                self.GetUser()
                if self.Got:
                    return True
                return False
            return False
        except:
            print("Error")
            return False
    def CheckNIDExists(self, Username):
        with sqlite3.connect("Data.db") as db:
            cursor = db.cursor()
            Values = (Username,)
            sql = """SELECT NID FROM User
                     WHERE NID = ?;
                  """
            cursor.execute(sql, Values)
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
            
    def GetUser(self, UUID):
        Values = (UUID,)
        try:
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """SELECT NID, Username, FirstName, LastName, Email, SessionID FROM User
                        WHERE UUID = ?
                """
                result, = cursor.execute(sql, Values)
                if result:
                    self.NID = result[0]
                    self.Username = result[1]
                    self.FName = result[2]
                    self.LName = result[3]
                    self.Email = result[4]
                    self.SessionID = result[5]
                    self.Got = True
                else:
                    print("Error")
        except sqlite3.Error as err:
            print(err)
    def SetUserDB(self):
        Values = (self.UUID, self.Username, self.Username, self.FName, self.LName, self.Email, self.Password, self.SessionID,)
        try:
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """INSERT INTO User(UUID, NID, Username, FirstName, LastName, Email, Password, SessionID)
                        Values (?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(sql, Values)
                return True
        except sqlite3.Error as error:
            print("Failed to insert variables into table, ", error)
            return False
    def CreateUser(self, Username, Password, FName, LName, Email):
        if self.CheckNIDExists(Username):
            return False
        self.UUID = str(uuid.uuid4()).replace("-","")
        self.Username = Username
        self.NID = Username
        self.Passsword = Password
        self.FName = FName
        self.LName = LName
        self.Email = Email
        self.SessionID = str(uuid.uuid4).replace("-","")
        self.Got = True
        if self.SetUserDB():
            return True
        return False

