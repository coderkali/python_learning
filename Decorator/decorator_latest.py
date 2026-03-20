

def div_deco(func):
    def wrap(a,b):
        if a<b:
            print("before ::", a, b)
            a,b =b,a
            print("after ::", a, b)
            return func(a,b)
    return wrap


@div_deco
def div(a,b):
    return a/b

print(div(2,4))
# print(div(4,2))


def add_sprinkle(func):
    def wrap(*args, **kwargs):
        print("You add sprinkle")
        func(*args, **kwargs)
    return wrap

def add_fudge(func):
    def wrap(*args, **kwargs):
        print("Args ", *args)
        print("KArgs ", *kwargs)
        print("you add a fudge")
        func(*args, **kwargs)
    return wrap



@add_sprinkle
@add_fudge
def get_ice_cream(flavor,isCone):
    print(f"You have a {flavor} ice cream, is Cone {isCone}")


get_ice_cream("Vanila",False)

