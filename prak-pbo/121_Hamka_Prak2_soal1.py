class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self._nim = nim
        self._nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self._nim

    def set_nim(self, new_nim):
        self._nim = new_nim

    def get_nama(self):
        return self._nama

    def set_nama(self, new_nama):
        self._nama = new_nama

    def get_info(self):
        return f"NIM: {self._nim}\nNama: {self._nama}\nAngkatan: {self.angkatan}"

    def cek_status(self):
        return "Status orang ini adalah : Mahasiswa Aktif" if self.isMahasiswa else "Status orang ini adalah : Bukan Mahasiswa"

    def kasta(self):
        return "Mahasiswa ini seorang : Senior" if self.angkatan >= 2022 else "Mahasiswa ini seorang : Junior"

    def ceklulus(self):
        return "Mahasiswa ini sudah Lulus" if self.angkatan >= 2019 else "Mahasiswa ini Belum Lulus"

# Inisiasi objek
mhs1 = Mahasiswa("122140122", "Hamka", 2022)
print(f"Informasi Mahasiswa:\n{mhs1.get_info()}")
print(f"Status: {mhs1.cek_status()}")
print(f"Kasta: {mhs1.kasta()}")
print(f"Kelulusan: {mhs1.ceklulus()}\n")

mhs1.set_nama("Hamka Putra Andiyan")
mhs1.set_nim("122140121")

print("Setelah perubahan")
print(f"Informasi Mahasiswa:\n{mhs1.get_info()}")
print("=============================================")

mhs2 = Mahasiswa("119140121","Takanashi Rikka", 2019, isMahasiswa= False)
print(f"Informasi Mahasiswa:\n{mhs2.get_info()}")
print(f"Status: {mhs2.cek_status()}")
print(f"Kasta: {mhs2.kasta()}")
print(f"Kelulusan: {mhs2.ceklulus()}\n")

mhs2.set_nama("Rikka the half eyed wicked witch")
mhs2.set_nim("119140121")

print("Setelah perubahan")
print(f"Informasi Mahasiswa:\n{mhs2.get_info()}")