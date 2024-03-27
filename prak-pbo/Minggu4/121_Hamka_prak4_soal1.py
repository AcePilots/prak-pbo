import math

class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    def hitungLuas(self):
        return math.pi * self.radius ** 2

def hitung_luas(objek):
    return objek.hitungLuas()

persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi: {hitung_luas(persegi)}")
print(f"Luas Lingkaran: {hitung_luas(lingkaran)}")