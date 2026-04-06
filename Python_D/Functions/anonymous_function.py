def squareit(n):
    return n*n

# lambda input_argument : expression
s = lambda n : n*n

print(s(4))

t= lambda a,b:a+b

print(t(10,20))

bigger = lambda a,b: a if a>b else b

print(bigger(10,20))
print(bigger(-10,-20))


bigger_2 = lambda a,b,c: a if a>b and a>c else b if b>c else c

print(bigger_2(10,20,30))
print(bigger_2(-10,-20,-30))


