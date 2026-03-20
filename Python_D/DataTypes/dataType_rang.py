# Rang object is immutable 

# Type 1::  
#   #range(n)
r = range(10) # 0 to 9 #0 to n-1

print(type(r))

print(r)

for x in r:
    print(x)

# Type 2:: 
#.   range(begin,end)

r = range(1,10)

for x in r:
    print(x)

print("*" * 100)
# Type 3:: 
#.   range(begin,end, increment/decrement)

r = range(1,21,1) # 1,2,3,4,5

for x in r:
    print("Increment By 1 ",x)

print("*" * 100)

r = range(1,21,3) # 1,4,7,10

for x in r:
    print("Increment By 3 ",x)


print("*" * 100)

r = range(20,1,-5) # 1,4,7,10

for x in r:
    print("Increment By 5 ",x)

print("*" * 100)

r = range(10,21)

print(r[0])
print(r[-1])

print("*" * 100)
r1 = r[1:5]

for x in r1:
    print(x)


print("*" * 100)

#r[1] = 1000 #TypeError: 'range' object does not support item assignment

