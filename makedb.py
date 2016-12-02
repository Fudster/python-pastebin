import sqlite3

conn = sqlite3.connect('paste.db')
print("Connected to database")
cursor = conn.cursor()
cursor.execute("CREATE TABLE pastes(id TEXT unique, content TEXT, password TEXT);")
print("Inserted table to database")
conn.commit
conn.close()
print("Saved database")
