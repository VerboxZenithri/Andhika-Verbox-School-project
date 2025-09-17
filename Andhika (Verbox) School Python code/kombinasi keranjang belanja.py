belanjaan=[
    {'nama_barang':'Anggur','harga':'250K','jumlah':'20'},
    {'nama_barang':'Genitu','harga':'225K','jumlah':'23'},
    {'nama_barang':'Delima','harga':'144K','jumlah':'17'}
]
for data in belanjaan:
    print(f'Nama barang:{data['nama_barang']},Harga:{data['harga']},Jumlah barang:{data['jumlah']}')

barang_baru={'nama_barang':'Apel','harga':'100K','jumlah':'55'}
belanjaan.append(barang_baru)

print('Nama Item discan pertama:',belanjaan[0]['nama_barang'])
print('Harga Genitu:',belanjaan[1]['harga'])
print('Jumlah Apel:',belanjaan[3]['jumlah'])
print('struk belanja:',belanjaan)