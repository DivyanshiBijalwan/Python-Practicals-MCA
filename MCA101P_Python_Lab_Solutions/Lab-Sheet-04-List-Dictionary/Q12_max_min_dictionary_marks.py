"""Question 12: Max min dictionary marks."""

marks = {"Aman": 78, "Riya": 92, "Karan": 65}
if marks:
    highest = max(marks, key=marks.get)
    lowest = min(marks, key=marks.get)
    print("Highest marks:", highest, marks[highest])
    print("Lowest marks:", lowest, marks[lowest])
