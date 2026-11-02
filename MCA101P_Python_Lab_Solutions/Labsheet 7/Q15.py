from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("Python is easy. Python is useful.", encoding="utf-8")
old, new = input("Word to replace: "), input("New word: ")
content = p.read_text(encoding="utf-8").replace(old, new)
p.write_text(content, encoding="utf-8")
print(content)
