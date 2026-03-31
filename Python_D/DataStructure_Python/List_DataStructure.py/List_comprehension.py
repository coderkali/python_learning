

'''
 [ expression for each element in sequnece ]
 [ expression for each element in sequnece if condition ]

'''

l = [x for x in range(1,11)]

print(l)


l1 = [ x for x in range(1,11) if x%2==0]

print(l1)

# Creation of list with square values of range

l2 = [x*x for x in range(1,11)] 
print(l2)

# power of each x
l3 = [2**x for x in range(1,11)] 
print(l3)


