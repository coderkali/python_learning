
# Order maintained
# Duplicate allowed
# The value within ( )
# Hetregeneous Object
# Indexing and slicing 
# Grawable in nature
# Imutable in nature -> This is different from List 
# Faster Access (Performance is good)



t = (10,20,30, "Kali")
print(type(t))
print(t)
print(t[0])
print(t[-1])
print(t[2])
print(t[1:4])

#t[0] = 7777 #TypeError: 'tuple' object does not support item assignment

#t.append(10) #AttributeError: 'tuple' object has no attribute 'append'
#t.remove(30) #AttributeError: 'tuple' object has no attribute 'remove'

t3 = () # Empty Tuple
t3 = (10)

print(type(t3)) # int type not a tuple type 

t4 = (30,)
print(type(t4)) # This is tuple type 
