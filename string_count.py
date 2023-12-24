def search(a,b):
    count =0
    for i in range(0,len(a)):
        if b == a[i]:
            count = i+1
    
    return count

a= input("enter the word : ") 
b = input("enter the element to search : ")
index = search(a , b)
print(index) if b in a else print("Not in the word")