
# Order Not maintained
# Duplicate not allowed
# The value within { }
# Hetregeneous Object
# Indexing and slicing Not Applicable
# Grawable in nature
# mutable in nature
# Faster Access (Performance is less)
s = {10,20,"Kali",30,10}

print(s)

# print(s[0]) #TypeError: 'set' object is not subscriptable
# print(s[1:4]) #TypeError: 'set' object is not subscriptable

s.add(50)
s.remove(30)
print(s)

s1 = {} # Empty Dictionary 

print(type(s1))

s2 = set() # Empty Set 
print(type(s2))


