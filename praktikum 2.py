try:
    file = open("D:/data.txt","r")
    bil1 = int(file.readline())
    bil2 = int(file.readline())
    hasil = bil1/bil2
    print(bil1 , "dibagi" , bil2 , " : " , hasil)
except:
    print("File tidak ditemukan")
    print("Atau")
    print("Tidak boleh pembagian dengan nol!")