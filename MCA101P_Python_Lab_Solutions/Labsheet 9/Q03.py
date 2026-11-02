# Search for a student by name in a list.
students = [{"roll": 1, "name": "Aman", "marks": 85}, {"roll": 2, "name": "Riya", "marks": 92}]
name = input("Enter student name: ").strip().lower()
matches = [s for s in students if s["name"].lower() == name]
print(matches if matches else "Student not found.")
