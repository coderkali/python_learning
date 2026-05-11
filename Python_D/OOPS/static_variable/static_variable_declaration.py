'''
Three ways we can declare static varaiable 
1) At class level
2) Inside the COnsturctor
3) Inside instance method
4) Inside class method 
5) inside static method


'''

class Test:
    name = "Kali"
    
    def __init__(self):
        Test.b = 20
    
    def m1(self):
        Test.c = 30

    @classmethod    
    def m2(self):
        Test.d = 30
    
    @staticmethod    
    def m3():
        Test.f = 50


t = Test()
t.m1()
Test.m2()
Test.m3()
print(Test.__dict__)