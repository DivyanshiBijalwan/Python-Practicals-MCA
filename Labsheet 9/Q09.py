from pathlib import Path
# Save student data in a text file and read it back.
path = Path("students.txt")
data = input("Enter student details: ")
with path.open("w", encoding="utf-8") as file:
    file.write(data + "\\n")
with path.open("r", encoding="utf-8") as file:
    print("Saved data:", file.read())
