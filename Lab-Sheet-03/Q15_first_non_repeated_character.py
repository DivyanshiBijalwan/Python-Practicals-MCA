"""Question 15: First non repeated character."""

# Independent solution for this lab-sheet question.
s=input("String: "); ans=next((ch for ch in s if s.count(ch)==1),None); print("First non-repeated =",ans)
