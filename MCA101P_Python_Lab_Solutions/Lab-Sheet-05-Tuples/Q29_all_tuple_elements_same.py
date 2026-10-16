"""Question 29: All tuple elements same."""

# Independent solution for this lab-sheet question.
t=tuple(input("Items: ").split()); print("All same" if not t or all(x==t[0] for x in t) else "Not all same")
