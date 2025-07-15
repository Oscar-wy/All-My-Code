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
                CREATE TABLE IF NOT EXISTS Users (
                    NID INTEGER Primary Key AUTOINCREMENT,
                    Username TEXT,
                    FName TEXT,
                    LName TEXT,
                    Email TEXT UNIQUE,
                    Password TEXT,
                    Salt TEXT,
                    SessionID TEXT
                );
              """
        cursor.execute(sql)
        sql = """
                CREATE TABLE IF NOT EXISTS UserRelations (
                    RequesterID INTEGER,
                    AddresseeID INTEGER,
                    Status TEXT CHECK(Status IN ('Pending', 'Accepted')),
                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (RequesterID, AddresseeID),
                    FOREIGN KEY (RequesterID) REFERENCES Users(NID),
                    FOREIGN KEY (AddresseeID) REFERENCES Users(NID)
                );
              """
        cursor.execute(sql)
        sql = """
                CREATE TABLE IF NOT EXISTS Blocks (
                    BlockerID INTEGER,
                    BlockedID INTEGER,
                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (BlockerID, BlockedID),
                    FOREIGN KEY (BlockerID) REFERENCES Users(NID),
                    FOREIGN KEY (BlockedID) REFERENCES Users(NID)
                );
              """
        cursor.execute(sql)
        sql = """
                CREATE TABLE IF NOT EXISTS Messages (
                );
              """

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
        if not salt:
            print("Login Error", salt)
            return False
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
    def getProfileFromNID(self, NID):
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Username, FName, LName FROM USERS WHERE NID = ?", (NID,))
            user = cursor.fetchone()
            if user:
                return user
            else:
                return "No User Found"
    def getUserRelations(self, selectUserNid):
        with sqlite3.connect("./Database.db") as db:
            cursor =  db.cursor()
            values = (self.NID, selectUserNid, selectUserNid, self.NID)
            sql = """
                    SELECT RequesterID, AddresseeID, Status FROM UserRelations
                    WHERE (RequesterID = ? AND AddresseeID = ?)
                    OR (RequesterID = ? AND AddresseeID = ?)
                  """
            cursor.execute(sql, values)
            relation = cursor.fetchone()
            print(relation)
            if not relation:
                return ("Not Friends", None) 
            requester, addressee, status = relation
            if status == "Accepted":
                return ("Friends", None)
            elif status == "Pending":
                if requester == self.NID:
                    return ("Requested", requester)
                else:
                    return ("Request Received", requester)
                
    def sendRequest(self, targetNID):
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            values = (self.NID, targetNID, targetNID, self.NID)
            sql = """
                    SELECT * FROM UserRelations
                    WHERE (RequesterID = ? AND AddresseeID = ?)
                    OR (RequesterID = ? AND AddresseeID = ?)
                  """
            cursor.execute(sql, values)
            relation = cursor.fetchone()
            if relation:
                return "Friend request already exists or you are already friends.", 400
            values = (self.NID, targetNID)
            sql = """
                    INSERT INTO UserRelations (RequesterID, AddresseeID, Status) 
                    VALUES (?, ?, 'Pending')
                  """
            cursor.execute(sql, values)
            db.commit()

    def cancelRequest(self, targetNID):
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            values = (self.NID, targetNID)
            sql = """
                    DELETE FROM UserRelations
                    WHERE RequesterID = ? AND AddresseeID = ? AND Status = 'Pending'
                  """
            cursor.execute(sql, values)
            db.commit()

    def acceptRequest(self, requesterNID):
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            values = (requesterNID, self.NID)
            sql = """
                    UPDATE UserRelations
                    SET Status = 'Accepted'
                    WHERE RequesterID = ? AND AddresseeID = ? AND Status = 'Pending'
                  """
            cursor.execute(sql, values)
            db.commit()

    def declineRequest(self, requesterNID):
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            values = (requesterNID, self.NID)
            sql = """
                    DELETE FROM UserRelations
                    WHERE RequesterID = ? AND AddresseeID = ? AND Status = 'Pending'
                  """
            cursor.execute(sql, values)
            db.commit()

    def unfriend(self, targetNID):
        with sqlite3.connect("./Database.db") as db:
            cursor = db.cursor()
            values = (self.NID, targetNID, targetNID, self.NID)
            sql = """
                    DELETE FROM UserRelations
                    WHERE ((RequesterID = ? AND AddresseeID = ?) OR (RequesterID = ? AND AddresseeID = ?))
                    AND Status = 'Accepted'
                  """
            cursor.execute(sql, values)
            db.commit()