class Rectangle:
    pro1="sum of all angle is 360"
    pro2="each angle is 90"
    def get_info(self):
        a=int(input("Enter the length of the rectangle: "))
        b=int(input("Enter the width of the rectangle: "))
        self.len=a
        self.width=b
    def area(self):
        print(self.len*self.width)



print(Rectangle.pro1)
print(Rectangle.pro2)
a1=Rectangle()
a2=Rectangle()
a1.get_info()
a2.get_info()
a1.area()
a2.area()