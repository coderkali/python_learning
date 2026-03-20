a = 34

match a:
    case 34:
        print("a is 34")
    case 35:
        print("a is 35")
    case _:
        print("a is not 34 or 35")


b = int(input("Enter a number: "))

match b:
    case b if b>0:
        print("b is positive")
    case b if b<0:
        print("b is negative")  
    case b if b==0:
        print("b is zero")
    case _:
        print("b is not a number")