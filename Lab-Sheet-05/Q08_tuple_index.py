"""Question 8: Tuple index."""

# Independent solution for this lab-sheet question.
t=tuple(input("Items: ").split()); x=input("Find index of: "); print("Index =",t.index(x) if x in t else "Item not found")
