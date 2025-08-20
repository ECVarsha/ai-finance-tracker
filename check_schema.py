import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(expenses)")
print(cursor.fetchall())

conn.close()
