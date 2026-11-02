# CREATE: Build a list of student records.
students = []
count = int(input("How many students? "))
for _ in range(count):
    roll = int(input("Roll number: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})
print("Created records:", students)
