"""Question 24: Reverse list no builtin."""

# Independent solution for this lab-sheet question.
items=input("Items separated by spaces: ").split(); out=[]
for x in items: out.insert(0,x)
print(out)
