import csv
from pathlib import Path
src, dest = Path("students.csv"), Path("students_copy.csv")
if not src.exists():
    with src.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows([["Roll", "Name"], [1, "Aman"]])
with src.open(newline="", encoding="utf-8") as f: rows = list(csv.reader(f))
with dest.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows(rows)
print("CSV copied.")
