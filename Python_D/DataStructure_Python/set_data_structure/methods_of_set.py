s = {10,20,30,40}

print(len(s))

s.add(50)

print(len(s))
print(s)

# To Add Multiple elements inside set , But all objects is iterable object 
#s.update(s1,s2) # s1 -> List, set, tuple ,string

s = {10,20}
l = {30,40}
s.update(l)

print(s) # {40, 10, 20, 30}

s.update(range(1,5))

print(s) # {1, 2, 3, 4, 40, 10, 20, 30}



# Find the valid 

s.add(10) # Valid
#s.add(10,20,30) # Not valid # TypeError: set.add() takes exactly one argument (3 given)

#s.update(40) # TypeError: 'int' object is not iterable

s.update(range(1,5),"Kali") # Valid 
print(s)