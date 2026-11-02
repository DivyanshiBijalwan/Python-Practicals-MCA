"""Question 30: Separate even odd."""

# Independent solution for this lab-sheet question.
nums=[int(x) for x in input("Integers: ").split()]; print("Even =",[x for x in nums if x%2==0]); print("Odd =",[x for x in nums if x%2!=0])
