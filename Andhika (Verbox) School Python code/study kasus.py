inventaris = [
    {"nama":"Laptop", "stok":5, "harga":7500000},
    {"nama":"Mouse", "stok":20, "harga":150000},
]

def tampilkan_produk():
    print("=== Daftar Produk ===")
    for produk in inventaris:
        print(f"{produk['nama']} - Stok: {produk['stok']} - Harga: {produk['harga']}")

def tambah_produk(nama, stok, harga):
    inventaris.append({"nama": nama, "stok": stok, "harga": harga})
    print(f"Produk {nama} berhasil ditambahkan!")

tampilkan_produk()
tambah_produk("Keyboard Mechanical", 10, 670000)

def cari_produk(nama):
    for produk in inventaris:
        if produk['nama'].lower() == nama.lower():
            print(f"Produk ditemukan: {produk['nama']} - Stok: {produk['stok']} - Harga: {produk['harga']}")
            return
    print("Produk tidak ditemukan!")

def hapus_produk(nama):
    for produk in inventaris:
        if produk['nama'].lower() == nama.lower():
            inventaris.remove(produk)
            print(f"Produk {nama} berhasil dihapus!")
            return
    print("Produk tidak ditemukan!")

def update_produk(nama, stok=None, harga=None):
    for produk in inventaris:
        if produk['nama'].lower() == nama.lower():
            if stok is not None:
                produk['stok'] = stok
            if harga is not None:
                produk['harga'] = harga
            print(f"Produk {nama} berhasil diupdate!")
            return
    print("Produk tidak ditemukan!")

cari_produk('Keyboard Mechanical')
tambah_produk('Laptop Fan Cooler',25,350000)
update_produk('Keyboard Mechanical',55,700000)
update_produk('Laptop',25)
update_produk('Mouse',None,125000)
tampilkan_produk()