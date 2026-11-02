"""Question 15: Subset check."""

# Independent solution for this lab-sheet question.
a=set(input("First set items: ").split()); b=set(input("Second set items: ").split()); print("First is subset of second" if a<=b else "Not a subset")
