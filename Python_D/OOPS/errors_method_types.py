class Test:
    def m1():
        print("Some method")
    def m2(x):
        print("Some method")    
    
t = Test()
#t.m1() # TypeError: Test.m1() takes 0 positional arguments but 1 was given
#t.m2(10) # TypeError: Test.m2() takes 1 positional argument but 2 were given
Test.m1() # No Error
Test.m2(10) # No Error

