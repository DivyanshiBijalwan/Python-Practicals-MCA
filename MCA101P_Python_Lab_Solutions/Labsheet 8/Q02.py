import sqlite3
connection = sqlite3.connect("new_database.db")
print("New database created successfully.")
connection.close()
