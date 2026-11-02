"""Question 19: Remove tuple duplicates."""

# Independent solution for this lab-sheet question.
t=tuple(input("Items: ").split()); out=tuple(dict.fromkeys(t)); print(out)
