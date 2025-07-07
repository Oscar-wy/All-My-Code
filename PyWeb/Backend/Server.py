import sqlite3
import random
import hashlib
import os
import secrets

def hashSaltText(text):
    salt = os.urandom(16)

    salted_password = salt + text.encode()

    hash_digest = hashlib.sha256(salted_password).hexdigest()
    return salt.hex(), hash_digest

def verifySaltText(text, salt):
    input_hash = hashlib.sha256(salt + text.encode()).hexdigest()
    return input_hash

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
                 Password TEXT,
                 Salt TEXT,
                 SessionID TEXT
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
        self.SessionID = ""

    def getSalt(self, username):
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            sql = "SELECT Salt FROM Users WHERE Username = ?"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            if result:
                result = result[0]
            return result
    def Login(self, username, password):
        salt = self.getSalt(username)
        salt = bytes.fromhex(salt)
        password = verifySaltText(password, salt)
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
    def fetchUserData(self, sessionID):
        with sqlite3.connect("./Database.db") as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Users WHERE SessionID = ?", (sessionID,))
            row = cursor.fetchone()
            if row:
                row = dict(row)
                self.SetData(row)
            return None
    def Register(self, username, password, fname, lname, email):
        salt, password = hashSaltText(password)
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                return False  # User already exists
            else:
                cursor.execute("INSERT INTO Users (Username, FName, LName, Email, Password, Salt, SessionID) VALUES (?, ?, ?, ?, ?, ?, ?)",
                               (username, fname, lname, email, password, salt, self.createSessionID()))
                db.commit()
                return True
    def createSessionID(self):
        return secrets.token_hex(32)