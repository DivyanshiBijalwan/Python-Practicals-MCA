from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("python file handling", encoding="utf-8")
print(p.read_text(encoding="utf-8").upper())
