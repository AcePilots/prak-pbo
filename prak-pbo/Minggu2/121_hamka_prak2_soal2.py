def checkvisa(func):
    def checker(obj1, obj2):
        if obj2 >= 2024:
            print("Visa valid dan di izinkan masuk")
        else:
            print("Visa kadaluarsa segera deportasi")
        func(obj1, obj2)

    return checker

def keterangan(func):
    def kets (obj1, obj2):
        print("Nama pemohon :", obj1)
        print("Tahun Visa pemohon :", obj2)
        func(obj1, obj2)
    
    return kets

@keterangan
@checkvisa
class PaperPlease:
    def __init__(self, nama, visa):
        self.nama = nama
        self.visa = visa

    def __del__(self):
        print("Data telah di proses. Menutup program....")
        print("=========================================")


turis1 = PaperPlease("Hamka", 2024)
turis2 = PaperPlease("Rikka", 2019) 

del turis1,turis2
