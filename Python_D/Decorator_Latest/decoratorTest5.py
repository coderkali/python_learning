def decor(func):
    def inner(name):
        names = ["Meeta", "Rishi"]
        if name in names:
            print('#' * 50)
            print(f"Hello {name} , Very Good Morning")
            print('#' * 50)
        else:
            func(name)
    return inner


@decor
def wish(name):
    print("Good Morning", name)


decorated_wish = decor(wish)

wish("Kali")
wish("Meeta")

print("---------------------------------")

decorated_wish("Kali")
decorated_wish("Rishi")