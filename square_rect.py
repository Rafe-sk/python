class Shape:
    def area(self, shape, length, width):
        if shape == "square":
            return length * length
        elif shape == "rectangle":
            return length * width
        else:
            return "Invalid shape"

class Area(Shape):
    def takevalue(self):
        self.shape = input("square or rectangle:- ").lower()
        if self.shape == "square":
            self.length = float(input("Enter length:- "))
            return self.area(self.shape, self.length, 0)
        elif self.shape == "rectangle":
            self.length = float(input("Enter length:- "))
            self.width = float(input("Enter width:- "))
            return self.area(self.shape, self.length, self.width)
        else:
            print("Invalid Input")

hi = Area()
a = hi.takevalue()
print("AREA:", a)