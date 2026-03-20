def smartDivision(func):
    def inner(a,b):
        if b == 0:
            print("How come divide with zero")
        else:
            func(a,b)
    return inner

@smartDivision
def division(a,b):
    print(a/b)


division(10,2)
division(10,0)