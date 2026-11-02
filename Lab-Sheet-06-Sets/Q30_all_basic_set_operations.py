"""Question 30: All basic set operations."""

# Independent solution for this lab-sheet question.
a=set(input("First set items: ").split()); b=set(input("Second set items: ").split()); print("Union:",a|b); print("Intersection:",a&b); print("A - B:",a-b); print("Symmetric difference:",a^b)
