from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("First line\\nSecond line\\nThird line", encoding="utf-8")
with p.open(encoding="utf-8") as f:
    for number, line in enumerate(f, 1): print(f"Line {number}: {line.rstrip()}")
