"""Question 11: Anagram check."""

# Independent solution for this lab-sheet question.
a=sorted(input("First string: ").replace(" ","").lower()); b=sorted(input("Second string: ").replace(" ","").lower()); print("Anagrams" if a==b else "Not anagrams")
