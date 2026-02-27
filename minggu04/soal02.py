bilangan = input("Masukkan Bilangan: ")
try:
    bilangan = int(bilangan)
    demo = "Positif" if bilangan>0 else "Negatif" if bilangan<0 else "Nol"
    print(demo)
except:
    print("Salah Input")
