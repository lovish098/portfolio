import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f :
    connection.executescript(f.read())

name = "John Doe"
email = "johndoe@example.com"
mobile = "1234567890"
subject = "Hello"
message = "This is a test message"

cur = connection.cursor()
cur.execute("INSERT INTO posts(name,email,mobile,subject,message) VALUES (?,?,?,?,?)",(name,email,mobile,subject,message))

connection.commit()
connection.close()