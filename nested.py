#nested tuple
#WAP to print the name of the topper and his/her marks in 4 subject wherein the marks
#are specified as a list in the tuple topper

number = int(input("Enter the number of students: "))
toppername=""
toppermarks=[]
for i in range (number):
    name=input(f"Enter the name of student{i+1}:")
    for i in range (4):
        marks=int(input(f"Enter the marks in {i+1} subject "))
        totalmarks=sum(marks)
        if totalmarks >sum(toppermarks):
            toppername=name
            toppermarks=marks
print(f"{name} is the topper with marks {toppermarks} in the 4 subjects")