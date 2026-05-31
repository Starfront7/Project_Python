foods = []
prices = []
total = 0

while True:
    food = input("Enter the name of the food (or 'q' to finish): ")
    if food.lower() == "q":
        print("Makasih")
        break
    else:
        price = float(input(f"Enter the price of {food}: RP. "))
        foods.append(food)
        prices.append(price)
        total += price

print("========== Pesanan Anda ==========")

for food in foods:
    print(f"- {food} dengan harga {price:.2f}")
print(f"Total harga: RP. {total:.2f}")