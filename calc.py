while True: 
    operator = input("enter an operator(1, 2, 3, 4, 5): ")
    if operator == "5":
        print("Mkasih silahkan kembali")
        break
    if operator in ["1", "2", "3", "4"]:
        num1 = float(input("masukin angka pertama: "))
        num2 = float(input("masukin angka kedua: "))
        if operator == "1":
            print("hasilnya adalah: ", num1 + num2 )
        elif operator == "2":
            print("hasilnya adalah: ", num1 - num2 )
        elif operator == "3":
            if num1 == 0 or num2 == 0:
                print("error: pembagian dengan nol tidak diperbolehkan")
            else: 
                print("hasilnya adalah: ", num1 / num2 )
        elif operator == "4":
            print("hasilnya adalah: ", num1 * num2 )
    else: 
        print(f"{operator} operator tidak di temukan, silahkan pilih 1-5 ")