# EMpty tuple

t = ()


# Single Value Tuple 

t = (10,)

# Multi Valued Tuple 

t= (10,20,30)
t= (10,20,30,)


# By using tuple function 

# t = tuple(sequnce)

l = [10,20,30]

t = tuple(l)

print(t)
print(type(t))

# By using range 

t = tuple(range(1,11,2))

print(t)


# String to Tuple

s= "Kali"
t = tuple(s)
print(t) 

t = eval(input("Enter Tuple Values :: "))

print(type(t))