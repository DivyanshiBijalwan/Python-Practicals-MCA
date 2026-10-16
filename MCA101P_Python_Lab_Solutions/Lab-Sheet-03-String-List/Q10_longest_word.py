"""Question 10: Longest word."""

# Independent solution for this lab-sheet question.
words=input("Sentence: ").split(); print("Longest word =",max(words,key=len) if words else "No words")
