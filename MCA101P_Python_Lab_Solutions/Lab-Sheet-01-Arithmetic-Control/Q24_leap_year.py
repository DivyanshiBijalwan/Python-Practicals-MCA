"""Question 24: Leap year."""

# Independent solution for this lab-sheet question.
y=int(input("Year: ")); print("Leap year" if y%400==0 or (y%4==0 and y%100!=0) else "Not a leap year")
