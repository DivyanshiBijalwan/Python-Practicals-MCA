"""Question 19: Most repeated word."""

# Independent solution for this lab-sheet question.
from collections import Counter
import re
words=re.findall(r"\b\w+\b",input("Sentence: ").lower()); counts=Counter(words); print(counts.most_common(1)[0] if counts else "No words")
