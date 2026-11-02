"""Question 14: Remove punctuation."""

# Independent solution for this lab-sheet question.
import string
s=input("String: "); print("".join(ch for ch in s if ch not in string.punctuation))
