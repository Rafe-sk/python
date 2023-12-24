str1=input("Enter the String 1:-")
str2=input("Enter the String 2:-")
first=str1.split(" ")
second=str2.split(" ")
common=[]
for i in first:
    for j in second:
        if i==j:
            common+=[j]

print(common)