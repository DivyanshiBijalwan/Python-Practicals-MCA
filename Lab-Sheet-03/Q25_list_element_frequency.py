"""Question 25: List element frequency."""

# Independent solution for this lab-sheet question.
items=input("Items separated by spaces: ").split(); freq={}
for x in items: freq[x]=freq.get(x,0)+1
print(freq)
