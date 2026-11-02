from pathlib import Path
# File-based CRUD: add, view, modify and delete student records.
path = Path("student_records.txt")
if not path.exists(): path.write_text("1,Aman,85\\n2,Riya,92\\n", encoding="utf-8")

def read_records():
    return [line.split(",", 2) for line in path.read_text(encoding="utf-8").splitlines() if len(line.split(",", 2)) == 3]

while True:
    print("\\n1.Add 2.View 3.Modify 4.Delete 5.Exit")
    choice = input("Choose: ")
    records = read_records()
    if choice == "1":
        records.append([input("Roll: "), input("Name: "), input("Marks: ")])
    elif choice == "2":
        for record in records: print(record)
        continue
    elif choice in ("3", "4"):
        roll = input("Roll number: ")
        if choice == "3":
            for record in records:
                if record[0] == roll:
                    record[1], record[2] = input("New name: "), input("New marks: ")
                    break
            else: print("Record not found.")
        else: records = [r for r in records if r[0] != roll]
    elif choice == "5": break
    else:
        print("Invalid choice.")
        continue
    path.write_text("".join(",".join(r) + "\\n" for r in records), encoding="utf-8")
    print("File updated.")
