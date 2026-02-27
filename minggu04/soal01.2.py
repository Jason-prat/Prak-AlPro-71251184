bilangan=input("Masukkan Suatu Bilangan: ")
try:
    bilangan = int(bilangan)
    if bilangan>0:
        print("Bilangan Positif")
    elif bilangan<0:
        print("Bilangan Negatif")
    elif bilangan ==0:
        print("Bilangan Nol")
except:
    print("Anda salah memasukkan input bilangan")
