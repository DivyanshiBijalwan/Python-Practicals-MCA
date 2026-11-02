import sqlite3
# Connect to SQLite and create a students table.
connection = sqlite3.connect("crud_students.db")
connection.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks REAL)")
connection.commit()
print("Database connected and students table created.")
connection.close()
