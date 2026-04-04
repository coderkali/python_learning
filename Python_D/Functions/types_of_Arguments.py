def f1(a,b):
    print(a+b)

f1(10,20)

'''
Four types of argument 
1) Positional argument 
2) KeyWord arguments 
3) Dwfualy arguments 
4) Variable length arguments
'''
# Positional argument
def sub(a,b):
    print(a-b)

sub(200,100) # a = 200, b =100

# KeyWord arguments 

def sub1(a,b):
    print(a-b)

sub1(a=200,b=100)
sub1(b=200,a=100)
# sub1(a=200) # TypeError: sub1() missing 1 required positional argument: 'b'
# sub1(c=200,d=100) # TypeError: sub1() got an unexpected keyword argument 'c'

sub1(200,b=100) # Valid 
#sub1(a=200,100) # Invalid. # SyntaxError: positional argument follows keyword argument

# Defualt arguments 

def wish(name ="Guest"):
    print("Good Morning ",name)

wish("Kali")
wish()

# Valid
def wish1(name,message):
    pass
# Valid
def wish1(name,message="Good Morning"):
    pass
#Invalid #SyntaxError: parameter without a default follows parameter with a default
# def wish1(name="Guest",message):
#     pass


#variable argument 

def f1(*n): # The n refernce is a Tuple 
    print(n)
    print(n[0])
    print(type(n))

f1(1,2,3,4,5)


def sum(*n):
    total =0
    for x in n:
        total = total +x
    print("The sum is ",total)

sum()
sum(10)
sum(20,12)

def function(*n):
    print(n)

function(10,20)
function((10,20,30),(30,40,50))

def f1(x,*y):
    print("X value is ",x)
    for y1 in y:
        print(y1)

f1(10,20,30,40,50)
f1(60)

def f2(*x,y):
    print("X value is ",x)
    print("Y value is ",y)

#f2(10,20,30,40) # TypeError: f2() missing 1 required keyword-only argument: 'y'
f2(10,20,30,y=40) # Valid

# def f3(*x, *y): # SyntaxError: * argument may appear only once
#     print(x)
#     print(y)