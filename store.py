#wap  that has a class store which keeps a record of code and price of each product display
# a menu of all products to the user  and prompt them to enter the quantity of each item required
# and finally geenrate a bill and display total amount
# class Store:
#     def Menu(self):
#         self.product_list={'A':{'Name':'Apple','code':'A001','price':'100/Kg'},
#                            'B':{'Name':'Baigan','code':'B001','price':'30/Kg'},
#                            'C':{'Name':'Shampoo','code':'S001','price':'50'}}

#     def cart(self)    
class Store:
    __itemCode=0
    __price=0
    __total=0
    product=[]
    quantity=[]
    price=[]
    def init(self):
        print("Welcome to ABC Store!")
        while True:
            a=int(input("Select a product:\n1.Soap\n2.Toothbrush\n3.Toothpaste\n4.Comb\n5.Book\n"))
            c=("Soap","Toothbrush","Toothpaste","Comb","Book")
            if a==1:
                self.__itemCode=1
                self.__price=50
            elif a==2:
                self.__itemCode=2
                self.__price=100
            elif a==3:
                self.__itemCode=3
                self.__price=200
            elif a==4:
                self.__itemCode=4
                self.__price=150
            elif a==5:
                self.__itemCode=5
                self.__price=500
            print("Product:",c[a-1],"\nPrice:",self.__price)
            self.product.append(c[a-1])
            self.price.append(self.__price)
            b=int(input("Enter the quantity: "))
            self.quantity.append(b)
            self._total=self.total+self._price*b
            print("Total:",self.__total)
            d=input("Do you want to add more items?(y/n): ")
            if d.lower()=="n":
                break
        print("\t\tBill\n\nProduct\t\tPrice\t\tQuantity")
        for i in range(len(self.product)):
            print(self.product[i],"\t\t",self.price[i],"\t",self.quantity[i],"")
        print("Total:",self.__total)
obj=Store()