from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("Original content.\\n", encoding="utf-8")
with p.open("a", encoding="utf-8") as f: f.write(input("Enter content to append: ") + "\\n")
print("Content appended.")
