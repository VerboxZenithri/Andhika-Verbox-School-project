class siswa:
    def __init__(self,nisn,nama,alamat):
        self.nisn=nisn
        self.nama=nama
        self.alamat=alamat
        
    def tujuan(self):
        print("menggapai skill diatas rata-rata")

damian=siswa("123456789","Damian","balikpapan")
print(damian.nisn)
print(damian.nama)
print(damian.alamat)
damian.tujuan()