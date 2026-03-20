def repeat(n):
    def decorator(func):
        def warpper(a):
            for i in range(n):
                func(a)
        return warpper
    return decorator


def say_hello(arg):
    print(f"hello! {arg}")

f = repeat(7)(say_hello)
f("Kali")

def repeat1(n):
    def decorator(func):
        def warpper(a):
            for i in range(n):
                func(a)
        return warpper
    return decorator

@repeat(3)
def say_hi(arg):
    print(f"Hello {arg}")

say_hi("Kali")
