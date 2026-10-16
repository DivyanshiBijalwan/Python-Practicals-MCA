"""Question 19: Power set."""

# Independent solution for this lab-sheet question.
from itertools import chain,combinations
s=set(input("Items: ").split()); items=list(s); power=[set(c) for r in range(len(items)+1) for c in combinations(items,r)]; print(power)
