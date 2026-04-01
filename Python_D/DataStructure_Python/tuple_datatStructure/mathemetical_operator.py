'''
concatination operator (+) => Both are should be two tuples 
repetion operator (*) => Must be one tuple and one is int

'''

t1= (10,20,30,40)
t2= (40,50,60)

t3 = t1+t2

print(t3)

#t4 = t1 +10  # TypeError: can only concatenate tuple (not "int") to tuple


t4 = t1 *3

print(t4)

#t5 = t1 * t2 # TypeError: can't multiply sequence by non-int of type 'tuple'
