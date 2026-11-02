import csv
from pathlib import Path
p = Path("students.csv")
if not p.exists():
    with p.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerow(["Roll", "Name", "Marks"])
record = [input("Roll: "), input("Name: "), input("Marks: ")]
with p.open("a", newline="", encoding="utf-8") as f: csv.writer(f).writerow(record)
print("Record appended.")
