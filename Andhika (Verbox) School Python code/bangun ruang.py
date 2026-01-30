import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hitung_luas():
    while True:
        clear()
        print("--- Program Hitung Luas Bangun Datar ---")
        print("1. Persegi         6. Belah Ketupat")
        print("2. Persegi Panjang 7. Layang-Layang")
        print("3. Segitiga        8. Lingkaran")
        print("4. Trapesium       9. Segi Lima")
        print("5. Jajar Genjang   10. Segi Enam")
        print("             0. end")
        print("---------------------------------------")
        print("\nuntuk keluar pilih 0")
        pilihan = input("Pilih bangun datar (1-10): ")

        # 1. Persegi
        if pilihan=='1':
            clear()
            sisi=float(input("Masukkan sisi: "))
            if sisi>0: # Periksa data (Langkah 3)
                luas=sisi*sisi
                print(f"Luas Persegi: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Sisi harus lebih besar dari nol.")

        # 2. Persegi Panjang
        elif pilihan=='2':
            clear()
            p=float(input("Masukkan panjang: "))
            l=float(input("Masukkan lebar: "))
            if p>0 and l>0:
                luas=p*l
                print(f"Luas Persegi Panjang: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Nilai harus lebih besar dari nol.")

        # 3. Segitiga
        elif pilihan=='3':
            clear()
            alas=float(input("Masukkan alas: "))
            tinggi=float(input("Masukkan tinggi: "))
            if alas>0 and tinggi>0:
                luas=0.5*alas*tinggi
                print(f"Luas Segitiga: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Nilai harus lebih besar dari nol.")

        # 4. Trapesium
        elif pilihan=='4':
            clear()
            a=float(input("Masukkan sisi sejajar atas: "))
            b=float(input("Masukkan sisi sejajar bawah: "))
            t=float(input("Masukkan tinggi: "))
            if a>0 and b>0 and t>0:
                luas=0.5*(a+b)*t
                print(f"Luas Trapesium: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Nilai harus lebih besar dari nol.")

        # 5. Jajar Genjreng
        elif pilihan=='5':
            clear()
            alas=float(input("Masukkan alas: "))
            tinggi=float(input("Masukkan tinggi: "))
            if alas>0 and tinggi>0:
                luas=alas*tinggi
                print(f"Luas Jajar Genjang: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Nilai harus lebih besar dari nol.")

        # 6. Belah Ketupat
        elif pilihan=='6':
            clear()
            d1=float(input("Masukkan diagonal 1: "))
            d2=float(input("Masukkan diagonal 2: "))
            if d1>0 and d2>0:
                luas=0.5*d1*d2
                print(f"Luas Belah Ketupat: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Nilai harus lebih besar dari nol.")

        # 7. Layang-Layang
        elif pilihan=='7':
            clear()
            d1=float(input("Masukkan diagonal 1: "))
            d2=float(input("Masukkan diagonal 2: "))
            if d1>0 and d2>0:
                luas=0.5*d1*d2
                print(f"Luas Layang-Layang: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Nilai harus lebih besar dari nol.")

        # 8. Lingkaran
        elif pilihan=='8':
            clear()
            r=float(input("Masukkan jari-jari: "))
            if r>0:
                luas=3.14*r*r
                print(f"Luas Lingkaran: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Jari-jari harus lebih besar dari nol.")

        # 9. Segi Lima (Beraturan)
        elif pilihan=='9':
            clear()
            s=float(input("Masukkan panjang sisi: "))
            if s>0:
                # Rumus: (1/4) * sqrt(5(5+2sqrt(5))) * s^2
                luas=1.720*s*s
                print(f"Luas Segi Lima Beraturan: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Sisi harus lebih besar dari nol.")

        # 10. Segi Enam (Beraturan)
        elif pilihan=='10':
            clear()
            s=float(input("Masukkan panjang sisi: "))
            if s>0:
                # Rumus: (3*sqrt(3)/2) * s^2
                luas=2.598*s*s
                print(f"Luas Segi Enam Beraturan: {luas}")
                input("\nenter untuk ke menu")
            else:
                print("Gagal: Sisi harus lebih besar dari nol.")
        elif pilihan=='0':
            clear()
            break

        else:
            clear()
            print("Pilihan tidak tersedia.")
            input("enter untuk mencoba ulang")


# Menjalankan fungsi
hitung_luas()