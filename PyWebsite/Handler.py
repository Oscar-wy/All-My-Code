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
                 Username TEXT UNIQUE,
                 FirstName VARCHAR(20),
                 LastName VARCHAR(20),
                 Email TEXT UNIQUE NOT NULL,
                 Password TEXT NOT NULL,
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
        self.UUID = None
        self.Username = ""
        self.Email = ""
        self.Password = ""
        self.FName = ""
        self.LName = ""
        self.Got = False
    def CheckUsernameExists(self, Username):
        with sqlite3.connect("Data.db") as db:
            cursor = db.cursor()
            Values = (Username,)
            sql = """SELECT Username FROM User
                     WHERE Username = ?;
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
                sql = """SELECT Username, FirstName, LastName, Email, Password FROM User
                        WHERE UUID = ?
                """
                result, = cursor.execute(sql, Values)
                if result:
                    self.Username = result[0]
                    self.FName = result[1]
                    self.LName = result[2]
                    self.Email = result[3]
                    self.Passsword = result[4]
                    self.Got = True
                else:
                    print("Error")
        except sqlite3.Error as err:
            print(err)

    def SetUserDB(self):
        Values = (self.UUID, self.Username, self.FName, self.LName, self.Email, self.Password)
        try:
            with sqlite3.connect("Data.db") as db:
                cursor = db.cursor()
                sql = """INSERT INTO User(UUID, Username, FirstName, LastName, Email, Password)
                        Values (?, ?, ?, ?, ?, ?)
                """
                cursor.execute(sql, Values)
                return True
        except sqlite3.Error as error:
            print("Failed to insert variables into table, ", error)
            return False
    def CreateUser(self, Username, Password, FName, LName, Email):
        if self.CheckUsernameExists(Username):
            return False
        self.UUID = str(uuid.uuid4()).replace("-","")
        self.Username = Username
        self.Passsword = Password
        self.FName = FName
        self.LName = LName
        self.Email = Email
        self.Got = True
        if self.SetUserDB():
            return True
        return False

