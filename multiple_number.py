# WAP to print index a which particular value exist if the value exist at multiple location
#  in the list then print all the indices also count the number of times that value is repeated 
# in the list 

number_of_elements=int(input("Enter number of elements:- "))
list=[]
count=0
for i in range(number_of_elements):
    elements=int(input("Enter element:-"))
    list.append(elements)
print(list)
b=int(input("Enter element to search for:-"))
for i in range(number_of_elements):
    if list[i]==b:
        count+=1
        print("Position(Index):-",i)
print("Repeated time(Count):-",count)