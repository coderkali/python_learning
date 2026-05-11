'''
we have use class name or cls variable

'''

class Test:
    a = 10
    @classmethod
    def m1(cls):
        del Test.a
        #del cls.a


print(Test.__dict__)
Test.m1()
print(Test.__dict__)
