Menu_Kantin = ["Cihu", "Batagor", "Kentang", "Es teh", "Jajan"]
for food in Menu_Kantin:
    print("==[Kantin]==")
    print(food)
Action = input("Istirahat makan apa aja? \n (Sebutkan nama makanan) : ")
while True:
    Pesanan = []
    for Queue in Pesanan:
        print(">[Pesanan]<")
        print(Queue)
    match Action:
        case "Cihu":
            Pesanan.append(Menu_Kantin[0])
        case "Batagor":
            Pesanan.append(Menu_Kantin[1])
        case "Kentang":
            Pesanan.append(Menu_Kantin[2])
        case "Es teh":
            Pesanan.append(Menu_Kantin[3])
        case "Jajan":
            Pesanan.append(Menu_Kantin[4])