import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('your_database.db')

# Set row_factory to sqlite3.Row so we can work with dictionary-like rows
conn.row_factory = sqlite3.Row

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS persons (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL
)
''')

# Insert values into the persons table
cursor.execute('''
INSERT INTO persons (Name, Email)
VALUES (?, ?)
''', ('John Doe', 'john.doe@example.com'))

cursor.execute('''
INSERT INTO persons (Name, Email)
VALUES (?, ?)
''', ('Jane Smith', 'jane.smith@example.com'))

cursor.execute('''
INSERT INTO persons (Name, Email)
VALUES (?, ?)
''', ('Alice Brown', 'alice.brown@example.com'))

# Commit the changes to the database
conn.commit()

# Optionally, fetch and print the results to confirm the insertions
cursor.execute('SELECT * FROM persons')
rows = cursor.fetchall()

# Print the rows, which are already dictionaries
for row in rows:
    print(dict(row))  # Directly print the row as a dictionary

# Close the connection to the database
conn.close()
