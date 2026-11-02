from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("First\\n\\nSecond\\n   \\nThird", encoding="utf-8")
lines = [line for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
p.write_text("\\n".join(lines) + ("\\n" if lines else ""), encoding="utf-8")
print("Blank lines removed.")
