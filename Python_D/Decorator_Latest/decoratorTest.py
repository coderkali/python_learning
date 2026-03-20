def decorator_function(inoput_func):
    def output_function():
        print("Add some extra code")
    
    return output_function


def decor(func):
    def inner():
        print("Send the person to beauty parlour")
        print("Showing the person With full of decorator")
    return inner


@decor
def display():
    print("Showing the function as it is")

display()

