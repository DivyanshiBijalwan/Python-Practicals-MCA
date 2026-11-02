import csv
from pathlib import Path
files = ["students1.csv", "students2.csv"]
header, combined = None, []
for filename in files:
    p = Path(filename)
    if not p.exists():
        with p.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows([["Roll", "Name", "Marks"], [1, "Sample", 80]])
    with p.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
        if rows:
            if header is None: header = rows[0]
            combined.extend(rows[1:])
with open("combined_students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if header: writer.writerow(header)
    writer.writerows(combined)
print("CSV files combined.")
