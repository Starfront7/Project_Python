questions = ("apakah python adalah bahsa pemograman? :", 
            "dimanakah ibukota indonesia? :",
            "siapa nama presiden indonesia ke 8? :",
            "berapa jumlah pulau di indonesia? :",
            "siapa nama presiden pertama indonesia? :")

options = (("A. Ya", "B. Tidak", "C. Mungkin", "D. Tidak Tahu"),
            ("A. Jakarta", "B. Bandung", "C. Surabaya", "D. Medan"),
            ("A. Joko Widodo", "B. Prabowo", "C. Soeharto", "D. Megawati"),
            ("A. 17.508", "B. 17.509", "C. 17.510", "D. 17.511"),
            ("A. Soekarno", "B. Soeharto", "C. Joko Widodo", "D. Megawati"))

answers = ("A", "A", "B", "B", "A")
guesses = ()
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)


    question_num += 1
    guess = input("Masukkan jawaban (A, B, C, D): ").upper()
    if guess == answers[question_num - 1]:
        score += 1
        print("Benar!")
        print("=====================================")
        
    else:
        print("Salah!")
        print(f"Jawaban yang benar adalah: {answers[question_num - 1]}")
        print("=====================================")

print(f"answers: ", end="")
for answer in answers:
    print(answer, end=" ")
    
print()
print(f"Total skor anda adalah {score} dari {len(questions)}")
print(f"nilai anda adalah {score * 20} dari 100")
print(f"apakah anda lulus atau tidak? ", end="")
print("Lulus" if score * 20 >= 70 else "Tidak Lulus")
print("=====================================")











