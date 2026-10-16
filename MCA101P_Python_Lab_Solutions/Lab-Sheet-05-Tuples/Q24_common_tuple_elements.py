"""Question 24: Common tuple elements."""

# Independent solution for this lab-sheet question.
a=tuple(input("First tuple: ").split()); b=tuple(input("Second tuple: ").split()); print(tuple(x for x in a if x in b))
