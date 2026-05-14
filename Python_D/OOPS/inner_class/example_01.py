class Outer:
    def __init__(self):
        print("Outer Object creation ")
    
    class Inner:
        def __init__(self):
            print("Inner class ")
        def m1(self):
            print("Inside m1 method")

# outer = Outer();
# inner = outer.Inner()
# inner.m1()
i = Outer().Inner().m1()