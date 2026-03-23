x =10;

print("Before Delete ::",x)


del x

#print(x) # NameError: name 'x' is not defined

s1= "Kali"

s2 = s1

s3 =s2

del s1

print(s2)
print(s3)


'''
del vs immutable object 

'''


s = "Kali"

#del s # Here we delete the reference not the object as stirng are immutable 

#del s[0] # TypeError: 'str' object doesn't support item deletion


'''
del vs none

'''

x = 10

# del x  # We can't use the del after the use of del
# print(x) # NameError: name 'x' is not defined
x = None  # We can use the x value after assigning the None value
print(x) # print None 