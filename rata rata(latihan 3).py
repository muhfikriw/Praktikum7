print("+"*25)
print("PROGRAM HITUNG RATA RATA")
print("+"*25)

x = 0
sum = 0
while True:
    try:
        aku = int(input("Masukkan bilangan bulat  =  "))
        x += 1
        sum += aku
        kamu = input("Ada Lagi (y/n)?          =  ")
        if kamu == "n":
            rumus = sum/x
            print("Rata-ratanya adalah      = ", rumus)
            break
        elif kamu != "y" :
            break
    except ValueError:
        print("bukan bil bulat")