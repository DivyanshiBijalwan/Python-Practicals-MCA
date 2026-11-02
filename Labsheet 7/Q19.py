from pathlib import Path
import re
src, dest = Path("sample.txt"), Path("sorted_words.txt")
if not src.exists(): src.write_text("banana apple mango orange", encoding="utf-8")
words = re.findall(r"\\b[\\w']+\\b", src.read_text(encoding="utf-8"))
words.sort(key=str.lower)
dest.write_text("\\n".join(words), encoding="utf-8")
print("Sorted words saved.")
