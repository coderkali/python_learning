'''
*args 
 variable length areguments 
 f1(*n) => tuple

**kwargs
 variable length key-word arguments 
 f1(**kwargs) => dict
 



'''


def f1(**kwargs):
    print(kwargs)

f1()
f1(name="Kali",rollno=101)

def f2(*args,**kwargs):
    print(args)
    print(kwargs)

f2(10,20,A=100,B=100)

# def f3(**kwargs,*args): # SyntaxError: arguments cannot follow var-keyword argument
#     print(args)
#     print(kwargs)





