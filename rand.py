import random 

lowest_num = 1
higest_num = 100

answer = random.randint(lowest_num, higest_num)
print("Selamat datang di permainan tebak angka!")
for i in range(3):
    guess = int(input(f"Masukkan tebakan Anda (antara {lowest_num} dan {higest_num}): "))
    if guess < answer:
        print("Tebakan Anda terlalu rendah.")
        print("====================================")
    elif guess > answer:
        print("Tebakan Anda terlalu tinggi.")
        print("====================================")
    elif guess == answer:
        print("Selamat! Tebakan Anda benar!")
        print("====================================")
        break
else:
    print("====================================")
    print("Kesempatan anda habis")
    print(f"Jawaban yang benar adalah {answer}.")
        