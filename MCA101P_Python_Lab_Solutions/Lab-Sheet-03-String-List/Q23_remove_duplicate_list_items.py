"""Question 23: Remove duplicate list items."""

# Independent solution for this lab-sheet question.
nums=input("Items separated by spaces: ").split(); out=[]
for x in nums:
 if x not in out: out.append(x)
print(out)
