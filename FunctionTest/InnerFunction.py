def outer():
    print("This is outer function")
    def inner():
        print("This is inner function")

    inner() # Inner function is local to Outer function
    print("Outer function execution completed")

outer()
