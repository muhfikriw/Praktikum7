file2 = str(input("Masukkan nama file (eg = D:/anyfiles.txt):  "))
try :
    while True:
        file = open(file2,"a")
        file3 = input("Masukan data yang ingin ditambahkan : ")
        file.write(file3)
        file.close()
        file4 = input("Apakah masih ada lagi? (y/n)")
        if file4 != "y" :
            break
        elif file4 == "n" :
            break
    file = open(file2, "r")
    print(file.read())
except FileNotFoundError :
    print("ada kesalahan penulisan")
