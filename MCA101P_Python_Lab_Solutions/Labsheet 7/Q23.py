import csv
from pathlib import Path
p = Path("students.csv")
if not p.exists():
    with p.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows([["Name", "Marks", "Age"], ["Aman", 85, 20], ["Riya", 92, 21]])
totals, counts = {}, {}
with p.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        for key, value in row.items():
            try: totals[key] = totals.get(key, 0) + float(value); counts[key] = counts.get(key, 0) + 1
            except (ValueError, TypeError): pass
for key in totals: print(f"Average {key}: {totals[key] / counts[key]:.2f}")
