'''
Accessing teh static varaiable 
1) In side constrcutor using sel or class name
2) Inside instance method  usng self of class name
3) inside the class method using cls or class name
4) inside ststaic method by using class name
5) Outside the class usinng object refernce or class name
'''

class Test:
    a = 10
    def __init__(self):
        print(self.a)
        print(Test.a)
    
    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod    
    def m2(cls):
        print(cls.a)
        print(Test.a)
    
    @staticmethod    
    def m3():
        print(Test.a)

t = Test()
print()
t.m1()
Test.m2()
Test.m3()