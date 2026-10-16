"""Question 6: Character frequency."""

# Independent solution for this lab-sheet question.
s=input("String: "); freq={}
for ch in s: freq[ch]=freq.get(ch,0)+1
print(freq)
