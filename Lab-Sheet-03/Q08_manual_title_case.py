"""Question 8: Manual title case."""

# Independent solution for this lab-sheet question.
s=input("Sentence: "); words=s.split(); print(" ".join(w[:1].upper()+w[1:].lower() for w in words))
