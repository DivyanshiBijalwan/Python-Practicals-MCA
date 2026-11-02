"""Question 29: List difference."""

# Independent solution for this lab-sheet question.
a=input("First list: ").split(); b=input("Second list: ").split(); print([x for x in a if x not in b])
