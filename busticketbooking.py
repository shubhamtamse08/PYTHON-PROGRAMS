from datetime import datetime


class Bus:
    def __init__(self,bno,ac,cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno
    def get_ac(self):
        return self.ac
    def get_cap(self):
        return self.cap

    def display(self):
        print("1.Bus number:",self.bno)
        print("2.Ac:",self.ac)
        print("3.Cap:",self.cap)



BUSES=[Bus(1,True,2),Bus(2,True,10),Bus(3,True,20)]


class Booking:
    def __init__(self):
        name = input("Enter your name")
        bno = int(input("Enter your bno"))
        d = int(input("Enter  date dd-mm-yyyy"))
        date = date.time.strptime(d, "%d/%m/%Y").date()
        self.name = name
        self.bno = bno
        self.date = date

    def make_booking(self, BUSES,BOOKING):
        if(self.isavailable(BUSES,BOOKING,bno,date)):
            booked=0
            capacity=0
            for i in BUSES:
                if(i.bno==bno):
                    capacity=i.cap
            for i in BOOKING:
                if(i.bno==bno and i.date==date):
                    booked=booked+1
            return (booked,capacity)

    def display_booking_info(self):
        print("Name:",self.name)
        print("Bno:",self.bno)
        print("Date:",self.date)

print("Available buses are")
for i in BUSES:
    i.display()

BOOKING=[]
while True:
    print("press 1 to book ticket")
    print("press 2 to view booking")
    print("press 3 to exit")

    ch=int(input("enter your choice:"))
    if ch==1:
        b=Booking()
        b.make_booking(BUSES,BOOKING)
    elif ch==2:
        if(not booking):
            print("booking is full")
        else:
            for i in BOOKING:
                i.display_booking_info()
    elif ch==3:
        print("exit")
    else:
        print("invalid choice")



