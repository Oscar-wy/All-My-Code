import sqlite3 as sql

class User():
    def __init__(self):
        self.Username = ""
        self.Password = ""
        self.SessionID = ""
        self.FName = ""
        self.LName = ""
        self.Balance = 0
    
    def CreateTables():
        with sql.connect("Server.db") as db:
            cursor = db.cursor()
            sql = """
                    CREATE TABLE IF NOT EXISTS Users(
                        UserID integer,
                        Username text UNIQUE,
                        Password text,
                        Firstname varchar(20),
                        Lastname varchar(20),
                        SessionID text UNIQUE,
                        Primary key(UserID)
                    );
                  """
            cursor.execute(sql)
        with sql.connect("Server.db") as db:
            cursor = db.cursor()
            sql = """
                    CREATE TABLE IF NOT EXISTS Bank(
                        UserID integer,
                        Balance integer,
                        Loan integer,
                        Primary key(UserID)
                    )
                  """

    def UsernameExists():
        with sql.connect("Server.db") as db:
            cursor = db.cursor()
            sql = """
                    
                  """