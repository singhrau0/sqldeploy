import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

connection = sqlite3.connect(currentdirectory + "\ims.db")
cn = connection.cursor()
import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()



# Create Product table
cursor.execute('''
    INSERT INTO CUSTOMER VALUES(2,'XYZ','HYD','XYZ@GMAIL.COM')
    
''')

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
