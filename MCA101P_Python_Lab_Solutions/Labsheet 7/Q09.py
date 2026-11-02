from pathlib import Path
source, target = Path("source.txt"), Path("destination.txt")
if not source.exists(): source.write_text("Example source content.", encoding="utf-8")
target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
print("File copied successfully.")
