#WAP to remove all duplicated from a list
number=[10,20,30,40,50,60,70,80,90,100,1001,10]
p=len(number)
a=[]
for i in range(p):
    if number[i] not in a:
        a.append(number[i])
    else:
        continue
print(a)