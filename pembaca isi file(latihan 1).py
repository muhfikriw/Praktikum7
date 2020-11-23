file = input("Masukkan nama file (eg = d:/anyfiles.txt) =  ")
file2 = open(file,"r")
print("Isi file " , file, " adalah = ")
print(file2.read())