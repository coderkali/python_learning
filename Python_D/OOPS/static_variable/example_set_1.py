class Test:
    a = 10
    def m1(self):
        self.a = 888

t = Test()
t.m1()
print(Test.a) # 10
print(t.a) # 888 As its referincing to instance variable not static varaibale