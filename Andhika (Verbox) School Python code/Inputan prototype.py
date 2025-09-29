stock=[
    {"Item":"Granat", }
]

def menu():
    while True:
        print('===Black Market===')
        print('1.Lihat stock barang-barang')
        print('2.Beli barang')
        print('3.Jual barang')
        print('4.Lihat daftar organisasi "underground"')
        print('5.keluar')
        pilihan=input('anda mau kemana? (1/2/3/4/5) pilihan di tangan anda...')

        if pilihan=="1":
            print