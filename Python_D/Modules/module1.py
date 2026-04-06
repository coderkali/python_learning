print(__name__)

if __name__ == "__main__":
    print("Direct Execution ")
else:
    print("In-Direct Execution ")

def f1():
    print("f1 Executed")
def f2():
    print("f2 Executed")
def f3():
    print("f3 Executed")

# f1()
# f2()
# f3()

if __name__ == "__main__": # If somoen called this file directly then all the function will be exuected 
    f1()
    f2()
    f3()
