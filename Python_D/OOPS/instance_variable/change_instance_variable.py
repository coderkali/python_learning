class Student:

    def __init__(self):
        self.a = 10
        self.b = 20
    
s = Student()
s.a = 888
s.b = 999
s1 = Student()

print(s.__dict__)
print(s1.__dict__)