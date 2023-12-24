class Shape:
    def area(self,x):
        return x**2

class Area(Shape):
    def takevalue(self):
        x = int(input("Enter  x: "))
        return self.area(x) 

hi = Area()  
result = hi.takevalue()  
print("Area of square:",result)