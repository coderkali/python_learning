def decor(func):
    def inner():
        x = func()
        return x*x
    return inner


def decor2(func):
    def inner2():
        x = func()
        return 2*x
    return inner2

@decor
@decor2
def num():
    return 20

print(num())