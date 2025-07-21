def circle():
    r=int(input("enter radius:"))
    print("area of circle",3.14*r*r)

def square():
    print("area of square",a*a)

def triangle():
    b=int(input("enter base:"))
    h=int(input("enter height:"))
    return 0.5*b*h
def rectangle():
    return a*b


while True:
    print("1.CIRCLE")
    print("2.SQUARE")
    print("3.triangle")
    print("4.rectangle")
    ch = int(input("Enter your choice: ")) 
    match ch:
        case 1:
            circle()
        case 2:
            a = int(input("Enter side of square: "))
            square(a)
        case 3:
            res = triangle()
            print("Area of triangle:", res)
        case 4:
            a = int(input("Enter length: "))
            b = int(input("Enter width: "))
            res = rectangle(a, b)
            print("Area of rectangle:", res)
        case 5:
            print("Exiting program.")
            exit(0)
        case _:
            print("Invalid choice. Please try again.")





