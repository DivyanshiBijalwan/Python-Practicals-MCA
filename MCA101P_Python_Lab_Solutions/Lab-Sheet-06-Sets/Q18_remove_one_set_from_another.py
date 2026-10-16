"""Question 18: Remove one set from another."""

# Independent solution for this lab-sheet question.
a=set(input("Main set items: ").split()); b=set(input("Items to remove: ").split()); a.difference_update(b); print(a)
