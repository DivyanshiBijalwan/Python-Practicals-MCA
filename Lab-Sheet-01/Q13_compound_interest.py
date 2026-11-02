"""Question 13: Compound interest."""

# Independent solution for this lab-sheet question.
p=float(input("Principal: ")); r=float(input("Annual rate (%): ")); t=float(input("Years: ")); amount=p*(1+r/100)**t; print("Compound interest =",amount-p,"Total amount =",amount)
