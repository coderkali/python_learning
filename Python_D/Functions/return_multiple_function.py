def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum,sub

x,y = sum_sub(20,10)
print(x)
print(y)


def calc(a,b):
    sum = a+b
    sub= a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div

t = calc(20,10)
print(type(t))

for x in t:
    print(x)
