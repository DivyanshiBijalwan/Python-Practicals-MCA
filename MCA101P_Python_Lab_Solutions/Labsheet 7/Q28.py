import csv
from pathlib import Path
p = Path("students.csv")
if not p.exists():
    with p.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows([["Name", "Marks"], ["Aman", 85], ["Riya", 92]])
with p.open(newline="", encoding="utf-8") as f: rows = list(csv.DictReader(f))
try:
    topper = max(rows, key=lambda row: float(row["Marks"]))
    print("Highest marks:", topper["Marks"], "Student:", topper["Name"])
except (ValueError, KeyError): print("No valid marks found.")
