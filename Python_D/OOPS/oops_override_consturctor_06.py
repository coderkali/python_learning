class Test:
    def __init__(self):
        print("no-arg consturctor")
    
    def __init__(self,x):
        print("Inside one arg constructor")
t1 = Test() # TypeError: Test.__init__() missing 1 required positional argument: 'x'
t2 = Test(10)