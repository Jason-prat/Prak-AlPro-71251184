suhu=input("Masukkan Suhu Anda: ")
try:
    suhu = int(suhu)
    if suhu>=38:
        print("Anda Demam")
    else:
        print("Anda Tidak Demam")
except:
    print("Anda salah memasukkan input suhu")
