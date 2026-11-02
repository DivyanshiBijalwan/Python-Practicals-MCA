from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("First line\\nSecond line\\nLast line", encoding="utf-8")
lines = p.read_text(encoding="utf-8").splitlines()
if lines: print("First:", lines[0], "\\nLast:", lines[-1])
else: print("File is empty.")
