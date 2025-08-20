import sqlite3

# connect to your DB
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# list all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# print schema of each table
for table in tables:
    print(f"\nSchema for {table[0]}:")
    cursor.execute(f"PRAGMA table_info({table[0]});")
    for col in cursor.fetchall():
        print(col)

# sample data from each table
for table in tables:
    print(f"\nData in {table[0]}:")
    cursor.execute(f"SELECT * FROM {table[0]} LIMIT 5;")
    print(cursor.fetchall())

conn.close()
