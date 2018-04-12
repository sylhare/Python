# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 19:46:10 2016

@author: sylhare
"""

import sqlite3


class DBManager(object):
    """ DBManager """
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, arg):
        """

        :param arg:
        :return:
        """
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def __del__(self):
        self.conn.close()


conn = sqlite3.connect(':memory:')  # Creation of a temporary database
conn = sqlite3.connect('my_db.sql')  # Creation of a database

# Example and creation of a database
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")
conn.commit()

# ==============================================================================
# #Deleting a table from the database
# cursor = c.cursor()
# cursor.execute("""
# DROP TABLE users
# """)
# conn.commit()
# print("database suppressed")
# ==============================================================================

# Insert Data into the table
cursor.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("John", 15))
conn.commit()

# Inserting data with a python dictionary in the table
data = {"name": "Sam", "age": 16}
cursor.execute("""
INSERT INTO users(name, age) VALUES(:name, :age)""", data)
conn.commit()

# Get the ID of the newly inserted row
id_db = cursor.lastrowid
print('last row id: %d' % id_db)

# With executemany, you can launch multiple queries and insert multiple rows
users = [("Steve", 42), ("John", 67)]
cursor.executemany("""
INSERT INTO users(name, age) VALUES(?, ?)""", users)
conn.commit()

# With fetchone, you can reach the first line only of the query
cursor.execute("""SELECT name, age FROM users""")
user1 = cursor.fetchone()
print(user1)

# Performing a specific research
id_db = 2
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id_db,))
response = cursor.fetchone()

# With fetchall() get all of the data from your query
cursor.execute("""SELECT id, name, age FROM users""")
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

# Cursor work as an interator here calling fetchall() automatically
cursor.execute("""SELECT id, name, age FROM users""")
for row in cursor:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

# To modify the input or a row
cursor.execute("""UPDATE users SET age = ? WHERE id = 2""", (31,))

# To comeback to the last commit
conn.rollback()

# Handling errors
try:
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTERGER
)
""")
    conn.commit()
except sqlite3.OperationalError:
    print('Error the table is already existing')
except Exception as e:
    print("Unknown error")
    conn.rollback()
    # raise e
finally:
    conn.close()

# ==============================================================================
# #Errors that can be trapped
# Error
# DatabaseError
# DataError
# IntegrityError
# InternalError
# NotSupportedError
# OperationalError
# ProgrammingError
# InterfaceError
# Warning
# ==============================================================================

# Closing the connexion with the db at the end
conn.close()

if __name__ == "__main__":
    pass