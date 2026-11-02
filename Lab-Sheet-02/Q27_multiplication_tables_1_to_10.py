"""Question 27: Multiplication tables 1 to 10."""

# Independent solution for this lab-sheet question.
for n in range(1,11):
 print(f"Table of {n}")
 for i in range(1,11): print(f"{n} x {i} = {n*i}")
