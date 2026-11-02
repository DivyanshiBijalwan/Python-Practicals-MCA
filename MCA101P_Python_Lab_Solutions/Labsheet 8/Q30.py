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

def add_student(con):
    values = (int(input("ID: ")), input("Name: "), int(input("Age: ")), float(input("Marks: ")))
    con.execute("INSERT INTO students VALUES (?, ?, ?, ?)", values)
    con.commit()
    print("Student added.")

def view_students(con):
    for row in con.execute("SELECT * FROM students"): print(row)

def update_student(con):
    sid, marks = int(input("ID to update: ")), float(input("New marks: "))
    cur = con.execute("UPDATE students SET marks=? WHERE id=?", (marks, sid))
    con.commit()
    print("Updated." if cur.rowcount else "Student not found.")

def delete_student(con):
    sid = int(input("ID to delete: "))
    cur = con.execute("DELETE FROM students WHERE id=?", (sid,))
    con.commit()
    print("Deleted." if cur.rowcount else "Student not found.")

with connect_db() as con:
    while True:
        print("\\n1.Add 2.View 3.Update 4.Delete 5.Exit")
        choice = input("Choose: ")
        try:
            if choice == "1": add_student(con)
            elif choice == "2": view_students(con)
            elif choice == "3": update_student(con)
            elif choice == "4": delete_student(con)
            elif choice == "5": break
            else: print("Invalid choice.")
        except (ValueError, sqlite3.Error) as error:
            print("Error:", error)
