from pathlib import Path
import re
src, dest = Path("sample.txt"), Path("unique_words.txt")
if not src.exists(): src.write_text("Python is easy and Python is useful.", encoding="utf-8")
words = re.findall(r"\\b[\\w']+\\b", src.read_text(encoding="utf-8"))
unique = list(dict.fromkeys(w.lower() for w in words))
dest.write_text("\\n".join(unique), encoding="utf-8")
print("Unique words saved.")
