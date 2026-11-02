from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("Welcome to Python file handling.\\nSample file.", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
