import os

# Fungsi untuk membersihkan layar terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Coffee:
    def __init__(self,nama,harga,rasa,texture,warna,kekentalan,stok):
        self.nama=nama
        self.harga=harga
        self.rasa=rasa
        self.texture=texture
        self.warna=warna
        self.kekentalan=kekentalan
        self.stok=stok
    def tampilkan_ingfo(self):
        print(f"Nama: {self.nama}| Harga: Rp{self.harga}| Stok: {self.stok}")
        print(f"Detail: Rasa {self.rasa}, Tekstur {self.texture}, Warna {self.warna}, {self.kekentalan}\n")

daftar_kopi = [
    Coffee("Cappucino",12000,"Nikmat","Sedang","Hitam Kecoklatan","Cair", 50),
    Coffee("Latte Art",20000,"Manis","Halus","Coklat Keputihan","Cair",210),
    Coffee("Dirty Espresso",8000,"Pahit","Kasar","Hytam Legam","Kental",37),
    Coffee("Kopi STMJ",10000,"Nikmat","halus","Putih Kecoklatan","Kental",135),
    Coffee("Civet Coffee (luwak)",45000,"Mantab","Halus","Coklat","Kental",15),
    Coffee("Americano",9000,"Lumayan pahit","Sedang","Coklat kehitaman","Sedang",75)
]

def tampilkan_stock():
    print("===DAFTAR STOCK KOPI SAAT INI===")
    if not daftar_kopi:
        print("kosong melompong wok...")
    else:
        for i, kopi in enumerate(daftar_kopi,1):
            print(f"{i}.",end="")
            kopi.tampilkan_ingfo()

def beli_kopi():
    tampilkan_stock()
    if not daftar_kopi:return
    try:
        pilihan=int(input("Pilih nomor kopi yang ingin dibeli:"))- 1
        if 0<=pilihan<len(daftar_kopi):
            jumlah = int(input(f"Mau beli berapa {daftar_kopi[pilihan].nama}? "))
            if daftar_kopi[pilihan].stok>=jumlah:
                daftar_kopi[pilihan].stok-=jumlah
                print(f"\n[BERHASIL] Membeli {jumlah} {daftar_kopi[pilihan].nama}")
                print("☕ Selamat menikmati! ☕")
            else:
                print("\n[X] Stock gakcukup!")
        else:
            print("[!] Nomor menu tidak ada.")
    except ValueError:
        print("[!] Masukkan angka yang valid!")

def menu():
    while True:
        clear()
        print("===WELCOME TO COFFEE SHOP===")
        print("1. Lihat stock kopi")
        print("2. Beli kopi")
        print("3. Keluar dari toko")
        
        pilihan=input("\nAnda mau apa? (1/2/3):")
        
        if pilihan=="1":
            clear()
            tampilkan_stock()
            input("Tekan Enter untuk kembali...")
        elif pilihan=="2":
            clear()
            beli_kopi()
            input("\nTekan Enter untuk kembali...")
        elif pilihan=="3":
            clear()
            print("Makasih loh ya sudah berkunjung ke toko gweh! ☕✌︎")
            break
        else:
            print("[X] Pilihan tidak valid!")
            input("\nTekan Enter untuk mencoba lagi...")
menu()

'''
class coffee:
    def __init__(self,nama,harga,rasa,texture,warna,kekentalan,stock):
        self.harga=int(harga)
        self.rasa=rasa
        self.texture=texture
        self.warna=warna
        self.kekentalan=kekentalan
        self.stock=int(stock)
        self.nama=nama

    def ingfo(self):
        print(f"\n>MENU: {self.nama}")
        print(f"  Rasa:{self.rasa}|Karakteristik:{self.texture},{self.kekentalan}")
        print(f"  Harga:Rp{self.harga}|Stok yang ada:{self.stok}")

    def pesenwoy(self,tersedianya):
        if self.stok>=tersedianya:
            self.stok-=tersedianya
            print(f"---[Berhasil Pesan{tersedianya}{self.nama}]---")
            print("Selamat menikmati!")
        else:
            print(f"---[hehey! ternyata {self.nama} gak cukup! :v]---")

daftar_kopi = [
    coffee("Cappucino",10000,"nikmat","sedang","hitam ke-coklatan","cair",50),
    coffee("Latte Art",20000,"manis","halus","coklat dan putih","cair",210),
    coffee("Dirty Expresso",8000,"pahit","kasar","hytam legam","kental",37)
]

print("===SISTEM INPUT GUDANG KOPI===")

while True:
    nama=input("\nNama Kopi (ketik 'stop' untuk selesai): ")
    if nama.lower()=="stop":
        break
    harga=input("Harga (misal 15000):...")
    rasa=input("Rasa:...")
    texture=input("Texture:...")
    warna=input("Warna:...")
    kekentalan=input("Kekentalan:...")
    stok=input("Jumlah Stok Awal:...")
    kopi_baru=coffee(nama,harga,rasa,texture,warna,kekentalan,stok)
    daftar_kopi.append(kopi_baru)

print("\n"+"="*30)
print("Menu yang ada")
for index, kopi in enumerate(daftar_kopi):
    print(f"{index+1}.{kopi.nama}")

if daftar_kopi:
    pilihan=int(input("\nPilih no kopi yang diinginkan: ")) - 1
    if 0 <=pilihan<len(daftar_kopi):
        menu_pilihan=daftar_kopi[pilihan]
        menu_pilihan.tampilkan_info()
        jumlah_beli=int(input(f"Mau beli berapa{menu_pilihan.nama}?"))
        menu_pilihan.pesan(jumlah_beli)
''' #sebelumnya-model kedua

'''
cappucino=coffee("12k","nikmat","sedang","hitam ke-coklatan", "cair")
latte_art=coffee("20K","manis","halus","coklat dan putih","cair")
dirty_expresso=coffee("8K","pahit","kasar","hytam legam","kental")

print (latte_art.harga)
print(latte_art.rasa)
print(latte_art.warna)
latte_art.aspek()

print(dirty_expresso.harga)
print(dirty_expresso.texture)
print(dirty_expresso.kekentalan)
dirty_expresso.aspek()
''' #sebelumnya-model pertama