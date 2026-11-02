from pathlib import Path
import re
p = Path("sample.txt")
if not p.exists(): p.write_text("Python is useful. Python is popular.", encoding="utf-8")
word = input("Enter word to count: ").strip()
count = len(re.findall(r"\\b" + re.escape(word) + r"\\b", p.read_text(encoding="utf-8"), re.I))
print("Occurrences:", count)
