"""Question 21: Key maximum value."""

data = {"Aman": 78, "Riya": 92, "Karan": 65}
if data:
    key = max(data, key=data.get)
    print("Key with maximum value =", key, "Value =", data[key])
