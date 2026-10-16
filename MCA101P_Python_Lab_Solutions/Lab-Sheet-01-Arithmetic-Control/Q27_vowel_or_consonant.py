"""Question 27: Vowel or consonant."""

# Independent solution for this lab-sheet question.
ch=input("One alphabet character: ").lower(); print("Enter one alphabet character" if len(ch)!=1 or not ch.isalpha() else "Vowel" if ch in "aeiou" else "Consonant")
