unit = input("masukin tempratur (C/F) celcius or farenheit : ")
temp = float(input("enter the temparature: "))

if unit == "C": temp = round((9 * temp) / 5 + 32, 2), print(f"The temprature in farenheit is: {temp} F")
elif unit == "F":
    temp = round((5 * (temp - 32)) / 9, 2)
    print(f"The temprature in celcius is: {temp} C")
else:
    print(f"{unit} is an invalid unit of measurement")
















