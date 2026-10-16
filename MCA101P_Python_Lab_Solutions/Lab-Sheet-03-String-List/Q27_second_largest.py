"""Question 27: Second largest."""

# Independent solution for this lab-sheet question.
nums=sorted(set(int(x) for x in input("Integers: ").split()))
print("Second largest =",nums[-2] if len(nums)>=2 else "Not enough distinct numbers")
