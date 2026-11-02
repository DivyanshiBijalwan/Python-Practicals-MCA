import csv
from pathlib import Path
p = Path("students.csv")
if not p.exists():
    with p.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows([["Roll", "Name", "Marks"], [1, "Aman", 85]])
with p.open(newline="", encoding="utf-8") as f: rows = list(csv.reader(f))
print("Data rows:", max(0, len(rows) - 1))
print("Columns:", len(rows[0]) if rows else 0)
