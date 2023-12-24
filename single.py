class Parent:
    def add(self, x, y):
        return self.x + self.y

class Child(Parent):
    def takevalue(self):
        self.x = int(input("Enter  x: "))  
        self.y = int(input("Enter y: "))
        return self.add(self.x, self.y) 

hi = Child()  
result = hi.takevalue()
print(hi.add(3,4))
print(result)