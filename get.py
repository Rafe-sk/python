# class ITM:
#     count = 0
#     def getdata(self):
#         while True:
#             name = input("Enter the student's name: ")
#             age = int(input("Enter the student's age: "))
#             address = input("Enter the address: ")
#             ask = input("Do you want to add more students? (yes/no): ")
#             ITM.count += 1
#             self.displaydata(name, age, address)
#             if ask.lower() != 'yes':
#                 break

#     def displaydata(self, name, age, address):
#         print("Student Information:")
#         print(f"Name: {name}")
#         print(f"Age: {age}")
#         print(f"Address: {address}")

# obj1 = ITM()
# obj1.getdata()
# print(ITM.count)



class Testclass:
    admission=0
    btech=0
    pgdm=0
    def getdata(self):
        self.name=input("Enter your name:")
        self.age=input("Enter your age:")
        self.address=input("Enter you address:")
        Testclass.count=+1
        self.department=input("Enter department BTECH/PGDM:")
        if self.department.upper=="BTECH":
            self.department="BTECH"
            Testclass.btech=+1
        else:
            self.department="PGDM"
            Testclass.pgdm+=1

    def setdata(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)
        print("Department:",self.department)   
        

obj=Testclass()
obj.getdata()
obj.setdata()
print(Testclass.admission)
print(Testclass.btech)
print(Testclass.pgdm)