"""Question 5: Remove duplicate characters."""

# Independent solution for this lab-sheet question.
s=input("String: "); out=""
for ch in s:
 if ch not in out: out+=ch
print(out)
