"""Question 22: Flatten nested tuple."""

# Independent solution for this lab-sheet question.
t=((1,2),(3,4),(5,)); flat=tuple(x for group in t for x in group); print(flat)
