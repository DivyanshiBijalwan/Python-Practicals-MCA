import sqlite3
con = sqlite3.connect("student_db.db")
con.execute("DROP TABLE IF EXISTS students")
con.commit()
print("Students table dropped.")
con.close()
