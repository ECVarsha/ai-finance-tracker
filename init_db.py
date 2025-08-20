import sqlite3

# Connect (creates user.db if not exists)
conn = sqlite3.connect("user.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Create expenses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    note TEXT,
    date TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("✅ Database initialized successfully.")
