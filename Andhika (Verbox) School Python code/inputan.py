import os

# Data awal stock
stock = [
    {"nama": "Barreta", "stok": 120, "harga": 935000},
    {"nama": "AK-47", "stok": 55, "harga": 4500000},
    {"nama": "BMG-50", "stok": 12, "harga": 97500000},
    {"nama": "Glock", "stok": 352, "harga": 480000},
    {"nama": "Illegal M4", "stok": 5, "harga": 12000000},
    {"nama": "RPG-7", "stok": 5, "harga": 129950000},
    {"nama": "HE Granade", "stok": 43, "harga": 2000000},
    {"nama": "Desert Eagle", "stok": 8, "harga": 15000000},
    {"nama": "Uzi", "stok": 60, "harga": 2500000},
    {"nama": "FN SCAR", "stok": 10, "harga": 12000000},
    {"nama": "M16A4", "stok": 22, "harga": 7000000},
    {"nama": "Dragunov SVD", "stok": 4, "harga": 22000000},
    {"nama": "MP5", "stok": 30, "harga": 3000000},
    {"nama": "C4 Explosive", "stok": 6, "harga": 45000000},
    {"nama": "Molotov", "stok": 200, "harga": 150000},
    {"nama": "Claymore Mine", "stok": 12, "harga": 18000000},
    {"nama": "Smoke Grenade", "stok": 120, "harga": 125000},
    {"nama": "Flashbang", "stok": 90, "harga": 250000},
    {"nama": "Kevlar Vest", "stok": 45, "harga": 900000},
    {"nama": "Tactical Helmet", "stok": 40, "harga": 650000},
    {"nama": "Night Vision Goggles", "stok": 7, "harga": 35000000},
    {"nama": "Tactical Shield", "stok": 5, "harga": 5000000},
    {"nama": "EMP Device", "stok": 2, "harga": 85500000},
    {"nama": "Signal Jammer", "stok": 8, "harga": 22000000},
    {"nama": "Hacking Laptop", "stok": 15, "harga": 12500000},
    {"nama": "Spy Drone", "stok": 9, "harga": 9500000},
    {"nama": "Silencer (Universal)", "stok": 50, "harga": 650000},
    {"nama": "Tactical Boots", "stok": 75, "harga": 250000},
    {"nama": "Survival Kit", "stok": 120, "harga": 175000},
    {"nama": "Combat Knife", "stok": 140, "harga": 120000},
    {"nama": "Tracking Beacon", "stok": 20, "harga": 4500000},
]

organisasi = ["Shadow Clan","Black Lotus","Ghost Syndicate","Slum Snake","NetBurners","D.E.V. Clan","The Convenant","The Dark Army","NWO","BitRunners","NiteSec"]

saldo = 195250000  # saldo User

# Fungsi clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_stok():
    print("=== Stok Barang ===\n")
    for i, produk in enumerate(stock, start=1):
        print(f"{i}. {produk['nama']} - Stok: {produk['stok']} - Harga: {produk['harga']}")
    print(f"\nSaldo Anda : ${saldo}")

def beli_barang():
    global saldo
    clear()
    tampilkan_stok()
    pilihan = int(input("\nPilih nomor barang yang ingin dibeli: "))
    if pilihan < 1 or pilihan > len(stock):
        print("[X] Pilihan tidak valid (-.-)!")
        input("\nTekan Enter untuk lanjut... (-_-)")
        return

    produk = stock[pilihan - 1]
    jumlah = int(input(f"Masukkan jumlah {produk['nama']} yang ingin dibeli: "))

    total = jumlah * produk['harga']
    if jumlah <= produk['stok']:
        if saldo >= total:
            produk['stok'] -= jumlah
            saldo -= total
            print(f"\nAnda membeli {jumlah} {produk['nama']} seharga {total}")
            print(f"\nSisa Saldo Anda : ${saldo}")
        else:
            print("\n[X] Saldo tidak cukup (-.-)!")
    else:
        print("\n[X] Stok tidak mencukupi (-.-)!")
    input("\nTekan Enter untuk kembali ke menu... (-_-)")

def jual_barang():
    global saldo
    clear()
    tampilkan_stok()
    pilihan = int(input("\nPilih nomor barang yang ingin dijual: "))
    if pilihan < 1 or pilihan > len(stock):
        print("[X] Pilihan tidak valid (-.-)!")
        input("\nTekan Enter untuk lanjut... (-.-)")
        return

    produk = stock[pilihan - 1]
    jumlah = int(input(f"Masukkan jumlah {produk['nama']} yang ingin dijual: "))

    produk['stok'] += jumlah
    total = jumlah * (produk['harga'] // 2)
    saldo += total
    print(f"\n$ Anda menjual {jumlah} {produk['nama']} dan mendapat {total}")
    print(f"\nTotal Saldo Anda : ${saldo}")
    input("\nTekan Enter untuk kembali ke menu... (-_-)")

def lihat_organisasi():
    clear()
    print("=== Daftar Organisasi Underground ===\n")
    for i, org in enumerate(organisasi, start=1):
        print(f"{i}. {org}")
    input("\nTekan Enter untuk kembali ke menu... (-_-)")

def menu():
    while True:
        clear()
        print("=== Black Market ===")
        print("1. Beli barang")
        print("2. Jual barang")
        print("3. Lihat stock barang")
        print("4. Lihat daftar organisasi 'Underground' yang berkontribusi di Black Market")
        print("5. Keluar")

        pilihan = input("anda mau kemana? (1/2/3/4/5) pilihan di tangan anda... 🚬(-.-) :")

        if pilihan == "1":
            beli_barang()
        elif pilihan == "2":
            jual_barang()
        elif pilihan == "3":
            clear()
            tampilkan_stok()
            input("\nTekan Enter untuk kembali ke menu... (-_-)")
        elif pilihan == "4":
            lihat_organisasi()
        elif pilihan == "5":
            clear()
            print("Anda keluar dari Black Market... sampai jumpa nanti (-_o)💰")
            break
        else:
            print("[X] Pilihan tidak valid (-.-)!!!")
            input("\nTekan Enter untuk lanjut... (-.-)!")

if __name__=="__main__":
    menu()