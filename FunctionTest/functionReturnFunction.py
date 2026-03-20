def outer():
    def inner():
        print("Print inner function completed")

    print("Outer function execution")   
    return inner

f = outer

print(outer)
print(f)


f1  = outer()



print(f1)
f1()