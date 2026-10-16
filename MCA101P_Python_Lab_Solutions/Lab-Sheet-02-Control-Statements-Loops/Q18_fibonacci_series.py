"""Question 18: Fibonacci series."""

# Independent solution for this lab-sheet question.
n=int(input("Number of terms: ")); a,b=0,1
for _ in range(max(0,n)): print(a,end=" "); a,b=b,a+b
print()
