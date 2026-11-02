import csv
rows = [["Roll No", "Name", "Marks"], [1, "Aman", 85], [2, "Riya", 92], [3, "Karan", 78]]
with open("students.csv", "w", newline="", encoding="utf-8") as f: csv.writer(f).writerows(rows)
print("students.csv created.")
