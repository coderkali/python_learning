'''
==
1) No of elememts must be same 
2) order of elements must be same 
3) Content of elemnet must be same
'''

t1 = ('cat', 'rat','Dog')
t2 = ('cat', 'rat','Dog')
t3 = ('CAT', 'RAT','DOG')
t4 = ('rat', 'Dog','Cat')

print(t1==t2) # True
print(t1==t3) # False
print(t1==t4) # False

# Relational Operator 

t1 = (10,20,30)
t2 = (30,15,40)

print(t1<t2) # It always check the first elemenet and evaluates  # True
print(t1>t2) # False

t1 = (10,20,30)
t2 = (10,15,40)
print(t1<t2) # Here it checks the second elemenet as first element is same  # False


t1 = (10,20,30)
print(10 in t1) # true
print(10 not in t1) #false