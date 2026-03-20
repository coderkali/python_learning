def decor1(func):
    def inner1():
        print("Decorator 1 Executed")
    return inner1

def decor2(func):
    def inner2():
        print("Decorator 2 Executed")
    return inner2


@decor2
@decor1
def f1():
    print("Original Function called")


f1()

# f1 (input)-> decor1 -> inner1 (outout) -> inner1(input) -> decor2 -> inner2 (Outoput)
# O/P: Decorator 2 Executed