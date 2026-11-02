# CRUD operations on a dictionary of employee data.
employees = {101: {"name": "Aman", "department": "IT", "salary": 30000}}
while True:
    print("\\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ")
    if choice == "1":
        emp_id = int(input("Employee ID: "))
        employees[emp_id] = {"name": input("Name: "), "department": input("Department: "), "salary": float(input("Salary: "))}
    elif choice == "2":
        for emp_id, data in employees.items(): print(emp_id, data)
    elif choice == "3":
        emp_id = int(input("Employee ID: "))
        if emp_id in employees: employees[emp_id]["salary"] = float(input("New salary: "))
        else: print("Employee not found.")
    elif choice == "4":
        emp_id = int(input("Employee ID: "))
        print("Deleted." if employees.pop(emp_id, None) is not None else "Employee not found.")
    elif choice == "5": break
    else: print("Invalid choice.")
