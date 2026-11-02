from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("Python\\nFile Handling\\n", encoding="utf-8")
content = p.read_text(encoding="utf-8")
print("Lines:", len(content.splitlines()))
print("Characters:", len(content))
