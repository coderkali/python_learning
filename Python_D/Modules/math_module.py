'''
factorial(x)
sqrt(x)
ceil(x)
floor(x)
fmod(s)


'''

# import math
# print(dir(math))

from math import *
print(factorial(4))
print(sqrt(4))
print(fabs(-10.6)) # 10.6
print(fabs(10.6))
print(ceil(10.5))

r = int(input("Enter radius ::"))
area = pi * pow(r,2)
print("Area of the circle ",area)


x = -12.893
y = fabs(x) # 12.893 # This removes the sign 
z = floor(y) # 12 , The integral part should be consider 
print(z)


