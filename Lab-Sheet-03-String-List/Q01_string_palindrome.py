"""Question 1: String palindrome."""

# Independent solution for this lab-sheet question.
s=input("String: "); t=s.replace(" ","").lower(); print("Palindrome" if t==t[::-1] else "Not palindrome")
