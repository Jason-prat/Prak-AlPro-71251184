s1= input("Masukkan Sisi 1: ")
s2= input("Masukkan Sisi 2: ")
s3= input("Masukkan Sisi 3: ")
try: 
    s1= int(s1)
    s2=int(s2)
    s3=int(s3)
    if s3==s2==s1:
        print("3 Sisi Sama")
    elif s3==s2 or s3==s1 or s1==s2:
        print("2 Sisi Sama")
    else:
        print("Tidak ada yang sama")
except:
    print("Input tidak valid")
