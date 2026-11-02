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

with connect_db() as con:
    con.execute("""CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY, student_id INTEGER, course_name TEXT NOT NULL
    )""")
    con.executemany(
        "INSERT OR REPLACE INTO courses VALUES (?, ?, ?)",
        [(1, 1, "Python"), (2, 2, "Database"), (3, 3, "Web Designing")]
    )
    print("Courses table created and records inserted.")
