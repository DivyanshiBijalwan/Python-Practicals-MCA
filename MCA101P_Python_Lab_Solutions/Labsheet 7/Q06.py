from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("One\\nTwo\\nThree\\nFour\\nFive\\nSix", encoding="utf-8")
with p.open(encoding="utf-8") as f:
    for number, line in enumerate(f, 1):
        if number % 2 == 0: print(line.rstrip())
