def say_hello():
    print("hello")

say_hello()




def deocrator(func):
    def wrapper():
        print("Function call is starting")
        func()
        print("Function call is emnding")
    return wrapper

def deocrator1(func):
    def wrapper1():
        print("Function call is starting")
        func()
        print("Function call is emnding")
    return wrapper1

f = deocrator(say_hello)
f()
print("------------------------")

@deocrator
def say_Hi():
    print("Hi")
    
say_Hi()


# f1 = deocrator1(say_Hi)
# f1()