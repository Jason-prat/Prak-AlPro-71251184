a=input("Masukkan Nilai pertama: ")
b=input("Masukkan Nilai kedua: ")
c=input("Masukkan Nilai ketiga: ")
try:
    a = int(a)
    b = int(b)
    c = int(c)
    if a>b and a>c:
        print("Nilai Terbesar: ", a)
    elif b>a and b>c:
        print("Nilai Terbesar: ", b)
    elif c>a and c>b:
        print("Nilai Terbesar: ", c)
    elif c==a==b:
        print("Nilai ketiganya sama: ", a)
    elif c==a:
        print("Nilai pertama dan ketiga sama: ", c)
    elif c==b:
        print("Nilai Kedua dan Ketiga sama: ", b)
    elif a==b:
        print("Nilai pertama dan kedua sama: ", a)

except:
    print("Ada input nilai pertama atau kedua atau ketiga yang salah")
