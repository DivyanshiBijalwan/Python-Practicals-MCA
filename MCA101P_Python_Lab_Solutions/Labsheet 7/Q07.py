from pathlib import Path
print("Enter lines; type END to finish.")
with Path("multiple_lines.txt").open("w", encoding="utf-8") as f:
    while True:
        line = input()
        if line.upper() == "END": break
        f.write(line + "\\n")
print("Lines saved.")
