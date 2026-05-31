import random

options = ("Batu", "Gunting", "Kertas")
running = True

while running:
    if not input("Apakah Anda ingin bermain (y/n): ").lower().startswith("y"):
        running = False
        print("Terima kasih! Sampai jumpa lagi.")
        break 

    player = None
    computer = random.choice(options)
    
    player = input("Masukkan pilihan Anda (Batu, Gunting, Kertas): ")
    while player not in options:
        print("Pilihan tidak valid. Silakan pilih Batu, Gunting, atau Kertas.")
        player = input("Masukkan pilihan Anda (Batu, Gunting, Kertas): ")

    print(f"Pilihan Player: {player}")
    print(f"Pilihan komputer: {computer}")

    if player == computer:
        print("Hasil: Seri!")
    elif (player == "Batu" and computer == "Gunting") or \
        (player == "Gunting" and computer == "Kertas") or \
        (player == "Kertas" and computer == "Batu"):
        print("Hasil: Player menang!")
    else:
        print("Hasil: Komputer menang!")
        
    if not input("Apakah Anda ingin bermain lagi? (y/n): ").lower().startswith("y"):
        running = False
        print("Terima kasih telah bermain! Sampai jumpa lagi.")
        break