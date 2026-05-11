class Student:

    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        print(self.a)
        print(self.b) 
    
    def delete(self):
        del self.a
    
s = Student()
s.m1()
del s.a,s.b
print(s.__dir__)
