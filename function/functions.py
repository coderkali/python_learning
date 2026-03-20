# a = 4
# b = 5 
# c = 1

# average = (a + b + c) / 3
# print(average)


def average(a,b,c):
    return (a+b+c)/3

print(average(3,5,1))

o1 = average(2,5,1)
print(o1)


def add(a,b,plus=0):
    rx = a + b + plus
    return rx

c = add(3,5,2)
print(c)

def subtract(a,b,minus=0):
    rx = a - b - minus
    return rx

c1 = subtract(b = 2, a = 3) 
print(c1)