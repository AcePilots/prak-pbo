batas1 = int(input("Masukan batas bawah :"))
batas2 = int(input("Masukan batas atas:"))
total = 0

print("Batas bawahnya adalah :", batas1)
print("Batas atasnya adalah :", batas2)

if (batas1 >= 0 and batas2 >= 0) :

        for i in range (batas1, batas2):
    
            if (i % 2 != 0) :
                total += 1
                print(i)
            else:
                pass
else:
    print("Batas 1 atau batas 2 tidak boleh dibawah 0")


print("Maka totalnya adalah :", total)
