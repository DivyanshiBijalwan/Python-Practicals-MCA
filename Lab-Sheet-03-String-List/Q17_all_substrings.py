"""Question 17: All substrings."""

# Independent solution for this lab-sheet question.
s=input("String: ")
for i in range(len(s)):
 for j in range(i+1,len(s)+1): print(s[i:j])
