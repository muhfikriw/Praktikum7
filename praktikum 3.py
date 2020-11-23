try:
    file = open("D:/data.txt" , "r")
    sum = 0
    for data in file:
        sum += int(data)
    print(sum)
except:
  print("data file tidak semuanya integer")
  print("bisa juga")
  print("nama/ direktori file salah")