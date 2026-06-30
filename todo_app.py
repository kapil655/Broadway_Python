import sqlite3

# Connect to database (creates todo.db if it doesn't exist)
conn = sqlite3.connect("todo.db")

print("Database connected successfully!")


import sqlite3

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
""")

conn.commit()

print("Table created successfully!")