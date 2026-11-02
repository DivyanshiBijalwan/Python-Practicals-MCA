"""Question 20: Longest word length."""

# Independent solution for this lab-sheet question.
t=tuple(input("Words: ").split()); print(max((len(w) for w in t),default=0))
