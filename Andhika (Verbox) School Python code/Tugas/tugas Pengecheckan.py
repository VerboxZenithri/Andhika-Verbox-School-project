kelipatan_1 = 4
kelipatan_2 = 6 
kata_1 = "pertanyaan"  #Kata untuk Aturan 1
kata_2 = "tanya pertanyaan"  #Kata untuk Aturan 2
kata_gabungan = "kebanyakan tanya!!!"
#Melakukan pengecekan
for angka in range(1, 91):
    memenuhi_aturan_1 = (angka % kelipatan_1 == 0)
    memenuhi_aturan_2 = (angka % kelipatan_2 == 0)
    if memenuhi_aturan_1 and memenuhi_aturan_2:
        print(kata_gabungan)
    elif memenuhi_aturan_1 and not memenuhi_aturan_2:
        print(kata_1)
    elif not memenuhi_aturan_1 and memenuhi_aturan_2:
        print(kata_2)
    else:
        print(angka)