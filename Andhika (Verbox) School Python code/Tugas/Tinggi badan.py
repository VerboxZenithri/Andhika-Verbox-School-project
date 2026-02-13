tinggi=int(input("Masukkan tinggi badan (cm): "))
if tinggi<160:
    kategori="Pendek Nyooo"
elif tinggi>=160 and tinggi<170:
    kategori="Gak Pendek Tapi Tidak Tinggi Juga"
elif tinggi>=170 and tinggi<=179:
    kategori="Tinggi"
else:
    kategori="Sangat Tinggi/Lainnya"
print(f"Kategori:{kategori}")