for i in range(2):
    for j in range(2,i,-1):
     print(end=" ")
    for k in range(67-i, 70):
      print(chr(k), end=" ")
    print()

for i in range(3):
    for j in range(i):
     print(end=" ")
    for k in range(65+i, 70):
      print(chr(k), end=" ")
    print()