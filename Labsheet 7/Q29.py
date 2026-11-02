import csv
from pathlib import Path
p = Path("students.csv")
if not p.exists():
    with p.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows([["Roll", "Name", "Marks"], [1, "Aman", 85]])
name = input("Student name to search: ").strip().lower()
found = False
with p.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row.get("Name", "").lower() == name: print("Record:", row); found = True
if not found: print("Student not found.")
