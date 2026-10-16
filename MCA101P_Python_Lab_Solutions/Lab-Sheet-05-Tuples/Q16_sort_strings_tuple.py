"""Question 16: Sort strings tuple."""

# Independent solution for this lab-sheet question.
t=tuple(input("Words: ").split()); print(tuple(sorted(t,key=str.lower)))
