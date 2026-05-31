weight = float(input("Enter your weight : "))
unit = input("Enter your unit (K or L): ")

if unit == "K":
    weight = weight*2.20462
    unit = "Lbs."
elif unit == "L":
    weight = weight*0.453592
    unit = "Kgs."
else:
    print(f"Invalid unit {unit}, please enter K for kilograms or L for pounds")
    
print(f"Your weight is {weight:.2f} {unit}")