"""Question 5: Remove using remove."""

# Independent solution for this lab-sheet question.
s={1,2,3}; x=int(input("Item to remove: "));
if x in s: s.remove(x); print(s)
else: print("Item not found")
