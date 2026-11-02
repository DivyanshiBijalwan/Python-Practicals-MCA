# DELETE: Remove a student record by roll number.
students = [{"roll": 1, "name": "Aman", "marks": 85}, {"roll": 2, "name": "Riya", "marks": 92}]
roll = int(input("Roll number to delete: "))
old_length = len(students)
students = [s for s in students if s["roll"] != roll]
print("Record deleted." if len(students) < old_length else "Student not found.")
print("Remaining records:", students)
