jari = float(input("Masukan jari jari :"))
phi = float(3.14)

if (jari >= 0) :

    keliling = float(2*phi*jari)
    luas = float(phi*(pow(jari,2)))

    print("kelilingnya adalah :",keliling)
    print("Luasnya adalah :", luas)
else:
    print("Jari jari tidak boleh negatif")

