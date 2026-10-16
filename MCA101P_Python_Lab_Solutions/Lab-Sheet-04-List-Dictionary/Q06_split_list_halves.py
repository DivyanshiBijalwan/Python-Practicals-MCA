"""Question 6: Split list halves."""

items = input("Enter items separated by spaces: ").split()
middle = (len(items) + 1) // 2
print("First half =", items[:middle])
print("Second half =", items[middle:])
