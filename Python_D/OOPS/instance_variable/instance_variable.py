class Student:

    def __init__(self):
        self.a = 10
        self.b = 20
    
    def m1(self):
        self.c = 30
    
t = Student()
t.m1()
print(t.__dict__)
t.d = 40
print(t.__dict__)
t1 = Student()
print(t1.__dict__)
