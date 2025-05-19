import sqlite3
import random

def InitialiseTables():
    with sqlite3.connect("./Database.db") as db:
        cursor = db.cursor()
        sql = """
                CREATE TABLE IF NOT EXISTS Users
                (
                 NID INTEGER Primary Key AUTOINCREMENT,
                 Username TEXT,
                 FName TEXT,
                 LName TEXT,
                 Email TEXT UNIQUE,
                 Password TEXT
                )
              """
        cursor.execute(sql)

class User():
    def __init__(self):
        self.NID = None
        self.Username = ""
        self.FName = ""
        self.LName = ""
        self.Email = ""
        self.Password =  ""
    def Login(self, username, password):
        with sqlite3.connect("./Database.db") as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            sql = "SELECT * FROM Users WHERE Username = ? AND Password = ?"
            print(sql)
            cursor.execute(sql, (username, password))
            row = cursor.fetchone()
            if row:
                row = dict(row)
                self.SetData(row)
                return True
            else:
                return False
    def SetData(self, row):
        for key in row.keys():
            setattr(self, key, row[key])
    def fetchUserData(self, username):
        with sqlite3.connect("./Database.db") as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
            row = cursor.fetchone()
            if row:
                row = dict(row)
                self.SetData(row)
            return None
    def Register(self, username, password, fname, lname, email):
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                return False  # User already exists
            else:
                cursor.execute("INSERT INTO Users (Username, Password, FName, LName, Email) VALUES (?, ?, ?, ?, ?)",
                               (username, password, fname, lname, email))
                db.commit()
                return True