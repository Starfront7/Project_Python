import random 

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│    ●    │"
"│         │"
"└─────────┘"


dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

dice = []

total = 0

taruhan = int(input("Masukkan jumlah taruhan Anda: "))
num_dice = int(input("jumlah dadu yang ingin Anda lempar (1-6): "))
jumlah_bulatan = int(input("berapa total tengah dadu: "))

for die in range(num_dice):
    dice.append(random.randint(1, 6))

for die in dice:
    total += die

print("Dadu yang dilempar:")
for die in dice:
    for line in dice_art[die]:
        print(line)
print(f"Total: {total}")
if total == jumlah_bulatan:
    print("Selamat! Anda menang!")
    print(f"Uang anda bertambah menjadi {taruhan + (taruhan * len(dice))}")
else:
    print("Maaf, Anda kalah. Coba lagi!")