def cek_digit_belakang(bil1,bil2,bil3):
    if bil1%10 == bil2%10 or bil1%10 == bil3%10 or bil2%10 == bil3%10:
        return "True"
    else:
        return "False"

#testcase
bil1=input("Masukkan Bilangan 1: ")
bil2=input("Masukkan Bilangan 2: ")
bil3=input("Masukkan Bilangan 3: ")
try:
    bil1 = int(bil1)
    bil2= int(bil2)
    bil3=int(bil3)
    print(cek_digit_belakang(bil1,bil2,bil3))
except:
    print("INPUT SALAH")
