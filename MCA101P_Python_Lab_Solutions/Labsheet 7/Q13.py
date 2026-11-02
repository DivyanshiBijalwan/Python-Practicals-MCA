from pathlib import Path
p = Path("numbers.txt")
if not p.exists(): p.write_text("10\\n20\\n30\\n40", encoding="utf-8")
try:
    numbers = [float(x) for x in p.read_text(encoding="utf-8").split()]
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers) if numbers else 0)
except ValueError: print("Invalid number in file.")
