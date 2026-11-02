"""Question 21: Largest smallest list."""

# Independent solution for this lab-sheet question.
nums=[int(x) for x in input("Integers: ").split()]; print("Largest =",max(nums),"Smallest =",min(nums)) if nums else print("Empty list")
