# str=input("Enter the string:-")
# print(str)
# a=input("Enter the word to search indexing")
# print(a)

def search(a,b):
    index = ""
    for i in range(0,len(a)):
        if b == a[i]:
            index = i
    
    return index

a= input("enter the word : ") 
b = input("enter the element to search : ")
index = search(a , b)
print(index) if b in a else print("Not in the word")