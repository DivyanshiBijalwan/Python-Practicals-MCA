"""Question 13: Tuple max min."""

# Independent solution for this lab-sheet question.
t=tuple(map(float,input("Numbers: ").split())); print("Maximum =",max(t),"Minimum =",min(t)) if t else print("Empty tuple")
