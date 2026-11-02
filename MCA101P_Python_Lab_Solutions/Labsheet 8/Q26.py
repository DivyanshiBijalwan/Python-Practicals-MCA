import sqlite3

DB_NAME = "student_db.db"

def connect_db():
    connection = sqlite3.connect(DB_NAME)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            marks REAL
        )
    """)
    return connection

def add_sample_students(connection):
    total = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    if total == 0:
        connection.executemany(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            [(1, "Aman", 20, 85), (2, "Riya", 21, 92), (3, "Karan", 19, 78)]
        )
        connection.commit()

import csv
with connect_db() as con:
    add_sample_students(con)
    rows = con.execute("SELECT * FROM students").fetchall()
with open("students_export.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age", "marks"])
    writer.writerows(rows)
print("Data exported to students_export.csv")
