"""Question 20: Cartesian product."""

# Independent solution for this lab-sheet question.
a=set(input("First set items: ").split()); b=set(input("Second set items: ").split()); print({(x,y) for x in a for y in b})
