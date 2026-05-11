'''
We wanted to mdoify the static varaiable then we need cls or Class name 
We can't modify the static varaible using self

'''

class Test:
    a =10
    def __init__(self):
        Test.a = 20
    
    def m1(self):
        Test.a = 30

    @classmethod
    def m1(self):
        Test.a = 30
print(Test.a)    
t = Test()
print(Test.a)
t.m1()
print(Test.a)
