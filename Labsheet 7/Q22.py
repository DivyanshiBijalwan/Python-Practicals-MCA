import csv
from pathlib import Path
p = Path("students.csv")
if not p.exists():
    with p.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows([["Roll", "Name", "Marks"], [1, "Aman", 85]])
with p.open(newline="", encoding="utf-8") as f:
    for row in csv.reader(f): print(row)
