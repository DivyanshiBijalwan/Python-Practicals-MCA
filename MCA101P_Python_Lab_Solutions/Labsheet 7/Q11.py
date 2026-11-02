from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("Python is easy. Python is powerful.", encoding="utf-8")
word = input("Enter word to search: ").strip()
if word and word.lower() in p.read_text(encoding="utf-8").lower(): print("Word found.")
else: print("Word not found.")
