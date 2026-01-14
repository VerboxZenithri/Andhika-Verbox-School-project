class buah:
    def __init__(self, harga, warna, rasa, bentuk):
        self.harga=harga
        self.warna=warna
        self.rasa=rasa
        self.bentuk=bentuk

    def function(self):
        print("dimakan")

semangka=buah("13500","hijau","manis","bulat")

print(semangka.harga)
print(semangka.warna)
print(semangka.rasa)
print(semangka.bentuk)
semangka.function()