menu = {"popcorn": 15000,
        "ayam": 20000,
        "kentang": 25000,
        "cocacola": 10000,
        "sprit": 15000,
        "fanta": 20000,
        "coklat": 12000,
        "permen": 8000,
        "aqua": 5000}

card = []
total = 0  
    
print("Selamat datang di bioskop kami!")
print("========== Menu kami: ==========")
for key, value in menu.items():
    print(f"{key:10}: Rp{value:.2f}")
    
while True:
    food = input("masukkan yang ingin anda beli (quit/q untuk keluar): ")
    if food == "q":
        print("Terima kasih telah berbelanja di bioskop kami!")
        break
    elif menu.get(food) is not None:
        card.append(food)
        total += menu[food]
        print(f"{food} berhasil ditambahkan ke keranjang anda.")
    else:
        print("Maaf, makanan yang Anda pilih tidak tersedia.")
for food in card:
    total += menu.get(food)
    print(food, end=", ")
print(f"\nTotal harga: Rp{total:.2f}")