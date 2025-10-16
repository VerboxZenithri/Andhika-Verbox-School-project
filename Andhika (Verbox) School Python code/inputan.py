import os
import json
import vlc
import threading
import time
import random
from datetime import datetime

def play_music():  #Fungsi Putar Musik Di Background
    path = os.path.join(os.path.dirname(__file__), "bgm.mp3")  #Langsung Cari Lagu Di Folder Sama
    player = vlc.MediaPlayer(path)
    player.play()
    player.audio_set_volume(75)
    while True:
        state = player.get_state()
        if state == vlc.State.Ended:  #Agar NgeLoop
            player.stop()
            player.play()
            player.audio_set_volume(75)
        time.sleep(1)

music_thread = threading.Thread(target=play_music, daemon=True)
music_thread.start()

def clear():  # Fungsi clear screen
    os.system("cls" if os.name == "nt" else "clear")

def load_json(filename, default_value):  # Data stock dan organisasi di Json
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump(default_value, f, indent=4)
        return default_value
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

stock = load_json("data barang black market.json", [])  #Stock Barang
organisasi = load_json("daftar organisasi.json", [])  #Daftar Organisasi
saldo_data = load_json("uang.json",{})  #Saldo User
saldo = saldo_data["saldo"]

def tampilkan_stok():  #Menampilkan Stock Barang
    print("=== Stok Barang ===\n")
    for i, produk in enumerate(stock, start=1):
        print(f"{i}. {produk['nama']} - Stok: {produk['stok']:,} - Harga: ${produk['harga']:,}")
    print(f"\nSaldo Anda : ${saldo:,}")

def save_stock_and_saldo():
    save_json("data barang black market.json", stock)
    save_json("uang.json", {"saldo": saldo})

def riwayat_transaksi(tipe, nama_barang, jumlah, total, effect=None):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("transaksi_log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{waktu}] {tipe} {jumlah}x {nama_barang} - Total: ${total:,}\n")
        if effect:
            log.write(f"    └─ {effect}\n")

def fluktuasi_harga(produk, tipe):
    
    persen = random.randint(3, 20)  #Harga Akan Terjadi Fluktuasi Di Sekitaran 3%-20%

    if tipe == "beli":
        produk['harga'] = int(produk['harga'] * (1 + persen / 100))
        effect = f"Harga {produk['nama']} naik {persen}% jadi ${produk['harga']:,}"
    elif tipe == "jual":
        produk['harga'] = int(produk['harga'] * (1 - persen / 100))
        if produk['harga'] < 1:
            produk['harga'] = 1
        effect = f"Harga {produk['nama']} turun {persen}% jadi ${produk['harga']:,}"
    else:
        effect = ""

    return effect
#Ini Fungsi Di Atas Untuk Mengubah Harga Jadi Naik/Turun Dengan Random Tergantung Pilih Beli/Jual, Jadi Seperti Ini:
#"beli" → harga naik
#"jual" → harga turun

def beli_barang():  #Cara Kerja Beli Barang
    global saldo
    clear()
    tampilkan_stok()
    try:
        pilihan = int(input("\nPilih nomor barang yang ingin dibeli: "))
        if pilihan < 1 or pilihan > len(stock):
            raise ValueError
    except ValueError:
        print("[X] Pilihan tidak valid (-.-)!")
        input("\nTekan Enter untuk lanjut... (-_-)")
        return

    produk = stock[pilihan - 1]
    try:
        jumlah = int(input(f"Masukkan jumlah {produk['nama']} yang ingin dibeli: "))
    except ValueError:
        print("\n[X] Input jumlah tidak valid (-.-)!")
        input("\nTekan Enter untuk lanjut... (-_-)")
        return

    total = jumlah * produk['harga']
    if jumlah <= produk['stok']:
        if saldo >= total:
            produk['stok'] -= jumlah
            saldo -= total
            effect = fluktuasi_harga(produk,"beli")
            save_stock_and_saldo()
            riwayat_transaksi("beli", produk['nama'], jumlah, total, effect)
            print(f"\nAnda membeli {jumlah} {produk['nama']} seharga ${total:,}")
            print("\033[92m"+effect+"\033[0m")
            print(f"Sisa saldo Anda: ${saldo:,}")
        else:
            print("\n[X] Saldo tidak cukup (-.-)!")
    else:
        print("\n[X] Stok tidak mencukupi (-.-)!")
    input("\nTekan Enter untuk kembali ke menu... (-_-)")

def jual_barang():  #Cara Kerja Menjual Barang
    global saldo
    clear()
    tampilkan_stok()
    try:
        pilihan = int(input("\nPilih nomor barang yang ingin dijual: "))
        if pilihan < 1 or pilihan > len(stock):
            raise ValueError
    except ValueError:
        print("[X] Pilihan tidak valid (-.-)!")
        input("\nTekan Enter untuk lanjut... (-_-)")
        return

    produk = stock[pilihan - 1]
    try:
        jumlah = int(input(f"Masukkan jumlah {produk['nama']} yang ingin dijual: "))
    except ValueError:
        print("\n[X] Input jumlah tidak valid (-.-)!")
        input("\nTekan Enter untuk lanjut... (-_-)")
        return

    produk['stok'] += jumlah
    total = jumlah * (produk['harga'] // 2)
    saldo += total
    effect = fluktuasi_harga(produk,"jual")
    save_stock_and_saldo()
    riwayat_transaksi("jual", produk['nama'], jumlah, total, effect)
    print(f"\nAnda menjual {jumlah} {produk['nama']} dan mendapat ${total:,}")
    print("\033[91m"+effect+"\033[0m")
    print(f"Saldo Anda sekarang: ${saldo:,}")
    input("\nTekan Enter untuk kembali ke menu... (-_-)")

def lihat_organisasi(): #Untuk Melihat Daftar Organisasi 
    clear()
    print("=== Daftar Organisasi Underground ===\n")
    for i, org in enumerate(organisasi, start=1):
        print(f"{i}. {org}")
    input("\nTekan Enter untuk kembali ke menu... (-_-)")

def baca_log():
    if not os.path.exists("transaksi_log.txt"):
        return []
    with open("transaksi_log.txt", "r", encoding="utf-8") as f:
        return f.readlines()

def lihat_log():  #Mendefinisikan Histori Dan Cara Kerja NYa
    clear()
    print("=== Riwayat Transaksi ===")
    print("1. Lihat semua transaksi")
    print("2. Filter berdasarkan jenis transaksi (BELI / JUAL)")
    print("3. Filter berdasarkan tanggal (YYYY-MM-DD)")
    print("4. Kembali")

    pilihan = input("\nPilih opsi (1/2/3/4) 📃(-.-): ")
    logs = baca_log()

    if pilihan == "1":
        clear()
        print("=== Semua Transaksi ===\n")
        print("".join(logs) if logs else "Belum ada transaksi tercatat.")
    elif pilihan == "2":
        jenis = input("Masukkan jenis transaksi (beli/jual): ").strip().upper()
        hasil = [log for log in logs if jenis.lower() in log.lower()]
        clear()
        print(f"=== Transaksi {jenis} ===\n")
        print("".join(hasil) if hasil else f"Tidak ada transaksi {jenis.lower()} ditemukan.")
    elif pilihan == "3":
        tanggal = input("Masukkan tanggal (format: YYYY-MM-DD): ").strip()
        hasil = [log for log in logs if tanggal in log]
        clear()
        print(f"=== Transaksi tanggal {tanggal} ===\n")
        print("".join(hasil) if hasil else f"Tidak ada transaksi pada tanggal {tanggal}.")
    elif pilihan == "4":
        return
    else:
        print("[X] Pilihan tidak valid (-.-)!")

    input("\nTekan Enter untuk kembali ke menu... (-_-)")

def menu():  #Mendefinisikan Menu
    while True:
        clear()
        print("=== Black Market ===")
        print("1. Beli barang illegal")
        print("2. Jual barang illegal")
        print("3. Lihat stock barang illegal")
        print("4. Lihat daftar organisasi 'Underground' yang berkontribusi di Black Market")
        print("5. lihat riwayat transaksi barang")
        print("6. Keluar")

        pilihan = input("anda mau kemana? (1/2/3/4/5/6) pilihan di tangan anda... 🚬(-.-) :")
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
            lihat_log()
        elif pilihan == "6":
            clear()
            print("Anda keluar dari Black Market... sampai jumpa nanti (-_o)✌︎💰")
            break
        else:
            print("[X] Pilihan tidak valid (-.-)!!!")
            input("\nTekan Enter untuk lanjut... (-.-)!")

if __name__=="__main__":
    menu() #Menjalankan Fungsi Menu