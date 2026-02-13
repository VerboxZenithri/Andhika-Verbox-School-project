""" 
Petunjuk Aturan:
Aturan 1: Angka habis dibagi oleh jumlah jari pada satu tangan tanpa ibu jari (yaitu 4).
Aturan 2: Angka merupakan kelipatan dari jumlah sisi bentuk bangun datar yang terbentuk
       dari dua segitiga sama sisi yang disatukan membentuk belah ketupat.
       - Segitiga = 3 sisi.
       - Dua segitiga = 6 sisi.
       - Belah ketupat = 4 sisi.
       - Karena soal sengaja ambigu, kita harus memilih salah satu: 6 (dari "dua segitiga") atau 4 (dari "membentuk belah ketupat").
       - Asumsi yang logis untuk kelipatan adalah mengambil **jumlah sisi belah ketupat**, yaitu **4**.
       - Catatan: Jika Aturan 2 yang dimaksud adalah kelipatan 6, ganti 'kelipatan_2 = 4' menjadi 'kelipatan_2 = 6'.
"""
# Penentuan Kelipatan
kelipatan_1 = 4  # Aturan 1: Jumlah jari satu tangan tanpa ibu jari (5 - 1 = 4)
kelipatan_2 = 4  # Aturan 2: Asumsi diambil dari jumlah sisi belah ketupat (4)

#Penentuan Kata-kata (Dibuat sendiri oleh siswa)
kata_1 = "pertanyaan"  # Kata untuk Aturan 1
kata_2 = "tanya pertanyaan"  # Kata untuk Aturan 2
kata_gabungan = "pertanyaan tanya pertanyaan" # Kata gabungan untuk Keduanya (KUMANVIRUS menjadi PENYAKIT)

# Loop dari angka 1 sampai 30
for angka in range(1, 31):
    # Melakukan pengecekan
    memenuhi_aturan_1 = (angka % kelipatan_1 == 0)
    memenuhi_aturan_2 = (angka % kelipatan_2 == 0)

    # Menentukan hasil keluaran berdasarkan 3 urutan pengecekan (Aturan 1)
    # Urutan pengecekan sangat penting.

    # 1. Apakah sebuah angka merupakan hasil pertemuan dua aturan kelipatan tertentu? (memenuhi keduanya)
    if memenuhi_aturan_1 and memenuhi_aturan_2:
        # Tampilkan sebuah kata gabungan (Aturan 4.a)
        print(kata_gabungan)

    # 2. Atau hanya cocok dengan salah satu aturannya saja?
    # Pengecekan sisa kasus: (A T) XOR (T B) = (A AND NOT B) OR (NOT A AND B)
    elif memenuhi_aturan_1 and not memenuhi_aturan_2:
        # Tampilkan kata pertama (Aturan 4.b)
        print(kata_1)

    elif not memenuhi_aturan_1 and memenuhi_aturan_2:
        # Tampilkan kata kedua (Aturan 4.c)
        print(kata_2)

    # 3. Atau tidak memenuhi keduanya.
    else:
        # Tampilkan angkanya sendiri (Aturan 4.d)
        print(angka)