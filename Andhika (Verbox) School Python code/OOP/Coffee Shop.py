import os
import json
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
FILE_USER=os.path.join(BASE_DIR,"data_user.json")
FILE_KOPI=os.path.join(BASE_DIR,"data_kopi.json")

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
        print(f"Nama: {self.nama}| Harga: Rp{self.harga:,}| Stok: {self.stok}")
        print(f"Detail: Rasa {self.rasa}, Tekstur {self.texture}, Warna {self.warna}, {self.kekentalan}\n")
    def to_dict(self):
        return {
            "nama":self.nama,
            "harga":self.harga,
            "rasa":self.rasa,
            "texture":self.texture,
            "warna":self.warna,
            "kekentalan":self.kekentalan,
            "stok":self.stok
        }

class User:
    def __init__(self,nama,saldo=1000000):
        self.nama=nama
        self.saldo=saldo
        self.riwayat=[]
    def tambah_saldo(self,jumlah):
        self.saldo+=jumlah
        self.riwayat.append({
            "waktu":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipe":"Top Up",
            "jumlah":jumlah,
            "saldo_akhir":self.saldo
        })
        print(f"\n[BERHASIL] Top up Rp{jumlah:,}")
        print(f"Saldo sekarang: Rp{self.saldo:,}")
    def beli(self,nama_item,harga,jumlah):
        total=harga*jumlah
        if self.saldo>=total:
            self.saldo-=total
            self.riwayat.append({
                "waktu":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "tipe":"Pembelian",
                "item":nama_item,
                "jumlah":jumlah,
                "harga":harga,
                "total":total,
                "saldo_akhir":self.saldo
            })
            return True
        return False
    def tampilkan_riwayat(self):
        print(f"\n===RIWAYAT TRANSAKSI {self.nama.upper()}===")
        if not self.riwayat:
            print("Belum ada transaksi.")
        else:
            for i,transaksi in enumerate(self.riwayat,1):
                print(f"\n{i}. [{transaksi['waktu']}]")
                if transaksi['tipe']=="Top Up":
                    print(f"   Top Up: +Rp{transaksi['jumlah']:,}")
                else:
                    print(f"   Beli: {transaksi['item']} x{transaksi['jumlah']}")
                    print(f"   Harga: Rp{transaksi['harga']:,} | Total: -Rp{transaksi['total']:,}")
                print(f"   Saldo Akhir: Rp{transaksi['saldo_akhir']:,}")
    def to_dict(self):
        return {
            "nama":self.nama,
            "saldo":self.saldo,
            "riwayat":self.riwayat
        }

def simpan_kopi(daftar_kopi):
    with open(FILE_KOPI,'w') as f:
        json.dump([kopi.to_dict() for kopi in daftar_kopi],f,indent=2)

def muat_kopi():
    if os.path.exists(FILE_KOPI):
        with open(FILE_KOPI,'r') as f:
            data=json.load(f)
            return [Coffee(**item) for item in data]
    return [
        Coffee("Cappucino",12000,"Nikmat","Sedang","Hitam Kecoklatan","Cair",50),
        Coffee("Latte Art",20000,"Manis","Halus","Coklat Keputihan","Cair",210),
        Coffee("Dirty Espresso",8000,"Pahit","Kasar","Hytam Legam","Kental",37),
        Coffee("Kopi STMJ",10000,"Nikmat","halus","Putih Kecoklatan","Kental",135),
        Coffee("Civet Coffee (luwak)",45000,"Mantab","Halus","Coklat","Kental",15),
        Coffee("Americano",9000,"Lumayan pahit","Sedang","Coklat kehitaman","Sedang",75)
    ]

def simpan_user(user):
    data_users={}
    if os.path.exists(FILE_USER):
        with open(FILE_USER,'r') as f:
            data_users=json.load(f)
    data_users[user.nama]=user.to_dict()
    with open(FILE_USER,'w') as f:
        json.dump(data_users,f,indent=2)

def muat_user(nama):
    if os.path.exists(FILE_USER):
        with open(FILE_USER,'r') as f:
            data_users=json.load(f)
            if nama in data_users:
                data=data_users[nama]
                user=User(data['nama'],data['saldo'])
                user.riwayat=data['riwayat']
                return user
    return User(nama)

def tampilkan_stock(daftar_kopi):
    print("===DAFTAR STOCK KOPI SAAT INI===")
    if not daftar_kopi:
        print("kosong melompong wok...")
    else:
        for i,kopi in enumerate(daftar_kopi,1):
            print(f"{i}.",end="")
            kopi.tampilkan_ingfo()

def beli_kopi(user,daftar_kopi):
    print(f"Saldo Anda: Rp{user.saldo:,}\n")
    tampilkan_stock(daftar_kopi)
    if not daftar_kopi:return
    try:
        pilihan=int(input("Pilih nomor kopi yang ingin dibeli:"))-1
        if 0<=pilihan<len(daftar_kopi):
            kopi_pilihan=daftar_kopi[pilihan]
            jumlah=int(input(f"Mau beli berapa {kopi_pilihan.nama}? "))
            total=kopi_pilihan.harga*jumlah
            if kopi_pilihan.stok>=jumlah:
                if user.beli(kopi_pilihan.nama,kopi_pilihan.harga,jumlah):
                    kopi_pilihan.stok-=jumlah
                    simpan_user(user)
                    simpan_kopi(daftar_kopi)
                    print(f"\n[BERHASIL] Membeli {jumlah} {kopi_pilihan.nama}")
                    print(f"Total: Rp{total:,}")
                    print(f"Saldo tersisa: Rp{user.saldo:,}")
                    print("☕ Selamat menikmati! ☕")
                else:
                    print(f"\n[X] Saldo tidak cukup! Butuh Rp{total:,}, saldo Anda Rp{user.saldo:,}")
            else:
                print("\n[X] Stock gak cukup!")
        else:
            print("[!] Nomor menu tidak ada.")
    except ValueError:
        print("[!] Masukkan angka yang valid!")

def top_up(user):
    print(f"Saldo sekarang: Rp{user.saldo:,}")
    try:
        jumlah=int(input("\nMasukkan jumlah top up: Rp"))
        if jumlah>0:
            user.tambah_saldo(jumlah)
            simpan_user(user)
        else:
            print("[!] Jumlah harus lebih dari 0!")
    except ValueError:
        print("[!] Masukkan angka yang valid!")

def menu():
    clear()
    nama_user=input("Masukkan nama Anda: ")
    user=muat_user(nama_user)
    daftar_kopi=muat_kopi()
    if os.path.exists(FILE_USER):
        with open(FILE_USER,'r') as f:
            data_users=json.load(f)
            if nama_user in data_users:
                print(f"\nSelamat datang kembali, {user.nama}!")
            else:
                print(f"\nPengguna baru terdaftar: {user.nama}!")
    else:
        print(f"\nPengguna baru terdaftar: {user.nama}!")
    input("Tekan Enter untuk lanjut...")
    while True:
        clear()
        print(f"===WELCOME TO COFFEE SHOP, {user.nama.upper()}!===")
        print(f"Saldo Anda: Rp{user.saldo:,}\n")
        print("1. Lihat stock kopi")
        print("2. Beli kopi")
        print("3. Top up saldo")
        print("4. Lihat riwayat transaksi")
        print("5. Keluar dari toko")
        pilihan=input("\nAnda mau apa? (1/2/3/4/5):")
        if pilihan=="1":
            clear()
            tampilkan_stock(daftar_kopi)
            input("Tekan Enter untuk kembali...")
        elif pilihan=="2":
            clear()
            beli_kopi(user,daftar_kopi)
            input("\nTekan Enter untuk kembali...")
        elif pilihan=="3":
            clear()
            top_up(user)
            input("\nTekan Enter untuk kembali...")
        elif pilihan=="4":
            clear()
            user.tampilkan_riwayat()
            input("\nTekan Enter untuk kembali...")
        elif pilihan=="5":
            clear()
            simpan_user(user)
            simpan_kopi(daftar_kopi)
            print(f"Makasih {user.nama} loh ya sudah berkunjung ke toko gweh! ☕✌︎")
            print(f"Saldo akhir Anda: Rp{user.saldo:,}")
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