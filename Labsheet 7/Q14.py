from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("Short line.\\nThis is the longest line.\\nMedium.", encoding="utf-8")
lines = p.read_text(encoding="utf-8").splitlines()
if lines: print("Longest line:", max(lines, key=len))
else: print("File is empty.")
