from pathlib import Path
a, b, c = Path("file1.txt"), Path("file2.txt"), Path("merged.txt")
if not a.exists(): a.write_text("First file content.\\n", encoding="utf-8")
if not b.exists(): b.write_text("Second file content.\\n", encoding="utf-8")
c.write_text(a.read_text(encoding="utf-8") + "\\n" + b.read_text(encoding="utf-8"), encoding="utf-8")
print("Files merged into", c)
