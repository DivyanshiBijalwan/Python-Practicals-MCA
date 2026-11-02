from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("Python makes file handling simple.", encoding="utf-8")
print("Number of words:", len(p.read_text(encoding="utf-8").split()))
