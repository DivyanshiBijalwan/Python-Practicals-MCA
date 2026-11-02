import sqlite3
connection = None
try:
    connection = sqlite3.connect("student_db.db")
    connection.execute("SELECT * FROM table_that_does_not_exist")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")
