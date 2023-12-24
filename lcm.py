#WAP to find LCM of any two number entered by user

num1=int(input("Enter the first number:"))
num2=int(input("Enter thesecond number:"))
if num1>num2:
    largest=num1
else:
    largest=num2
lcm=num1*num2
while largest<=lcm:
    if largest%num2==0 and largest%num1==0:
        print("LCM of",num1,"and",num2,"=",largest)
        break
    else:
        largest+=1    