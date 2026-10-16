"""Question 30: Dictionary character frequency."""

text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)
