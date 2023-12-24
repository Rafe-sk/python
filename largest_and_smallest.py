#WAP to find largest and smallest element in a list
mylist=[]
times=int(input("enter the number of element in the list: "))
i=1
for i in range(i,times+1):
    print("enter the",i,"element: ")
    mylist.append(int(input()))
    
print(mylist)

max=mylist[0]
for num in mylist:
     if num > max:
      max=num
min=mylist[0]
for num in mylist:
    if num <min:
     min=num
print("The smallest item in the list is",min)
print ("The largest in the list is",max)