my2DList=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(my2DList[2])#print the list at the particular index number
print(my2DList[2][0])#print particular list element

myList=[[1,2,3,'a'],[5,6,7,'cat'],[9,10,4.5,12],['beta',14,15,16]]#can have different data type
print(myList)

myLst=[[1,2,3,'a'],[5,6,7,'cat','sparshva'],[9,10,4.5,12],['beta',14,15,16]]#can have diifferent length
print(myLst)
print(len(my2DList[2]))

subL=['p','q','r','s']#list can have sublist and in sublist we can have sublist
myLs=[[1,2,3,'a'],[5,6,7,'cat','sparshva'],[9,10,4.5,12],['beta',14,15,subL]]
print(myLs[3][3])
print(myLs[3][3][3])#print list ka sublist ke sublist ka one element