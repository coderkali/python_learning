'''
global keyword
1) To make local variable witj same name act as a global variable 
2) To make the local variable explictly global variable 

'''


a = 10 # Global Variable
def f1():
    global a
    a=20 #Local Variable 
    print(a)

def f2():
    print(a)

f1() # 20
f2() # 10


def f3():
    global b 
    b =20
    print(b)

def f4():
    print(b) # NameError: name 'b' is not defined, SO we have to define gloabl keyword

f3()
f4()


x = 777

def f1():
    #print(x) # This Line hsould go to after global declarion 
    global x # SyntaxError: name 'x' is used prior to global declaration
    print(x)
    x =999
    print(x)

f1()

y = 888
def f1():
    y =999
    print(y) # 999 # Prioroty is local variable , If not then it will go to global variable
    print(globals())
    print(globals().get('y'))

    for k,v in globals().items():
        print("For Key ",k," Value is ",v)
        

f1()



