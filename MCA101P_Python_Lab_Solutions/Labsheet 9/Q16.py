import sqlite3

DB_NAME = "crud_students.db"

def connect_db():
    con = sqlite3.connect(DB_NAME)
    con.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, marks REAL
    )""")
    return con

def add_sample_data(con):
    if con.execute("SELECT COUNT(*) FROM students").fetchone()[0] == 0:
        con.executemany("INSERT INTO students VALUES (?, ?, ?, ?)",
                        [(1, "Aman", 20, 85), (2, "Riya", 21, 92), (3, "Karan", 19, 78)])
        con.commit()

with connect_db() as con:
    add_sample_data(con)
    roll = int(input("Roll number to delete: "))
    cursor = con.execute("DELETE FROM students WHERE id=?", (roll,))
    print("Record deleted." if cursor.rowcount else "Student not found.")
