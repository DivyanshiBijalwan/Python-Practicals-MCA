"""Question 29: Max min set."""

# Independent solution for this lab-sheet question.
s=set(map(float,input("Numbers: ").split())); print("Maximum =",max(s),"Minimum =",min(s)) if s else print("Set is empty")
