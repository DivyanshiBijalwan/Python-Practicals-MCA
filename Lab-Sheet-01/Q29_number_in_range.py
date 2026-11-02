"""Question 29: Number in range."""

# Independent solution for this lab-sheet question.
n=float(input("Number: ")); a=float(input("Range start: ")); b=float(input("Range end: ")); a,b=min(a,b),max(a,b); print("In range" if a<=n<=b else "Out of range")
