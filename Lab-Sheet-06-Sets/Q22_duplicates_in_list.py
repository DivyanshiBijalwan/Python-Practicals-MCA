"""Question 22: Duplicates in list."""

# Independent solution for this lab-sheet question.
items=input("Items: ").split(); seen=set(); duplicates=set()
for x in items:
 if x in seen: duplicates.add(x)
 seen.add(x)
print("Duplicates =",duplicates)
