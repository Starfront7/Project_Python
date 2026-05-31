modal = 0
bunga = 0
waktu = 0

while True:
    modal = float(input("Masukkan jumlah modal awal: "))
    if modal <= 0:
        print("Jumlah modal harus lebih besar dari 0. Silakan coba lagi.")
    else:
        break
        
while True:
    bunga = float(input("Masukkan suku bunga (dalam persen): "))
    if bunga <= 0:
        print("Suku bunga harus lebih besar dari 0. Silakan coba lagi.")
    else:
        break
        
while True:
    waktu = float(input("Masukkan jangka waktu (dalam tahun): "))
    if waktu <= 0:
        print("Jangka waktu harus lebih besar dari 0. Silakan coba lagi.")
    else:
        break
        

total_akhir = modal * pow((1 + bunga / 100), waktu)

bunga_majemuk = total_akhir - modal

print(f"Total uang akhir (modal + bunga): {total_akhir:.2f}")
print(f"Keuntungan dari bunga majemuk saja: {bunga_majemuk:.2f}")
