# UPDATE: Change a student's marks using roll number.
students = [{"roll": 1, "name": "Aman", "marks": 85}, {"roll": 2, "name": "Riya", "marks": 92}]
roll = int(input("Roll number: "))
marks = float(input("New marks: "))
for student in students:
    if student["roll"] == roll:
        student["marks"] = marks
        print("Updated:", student)
        break
else:
    print("Student not found.")
