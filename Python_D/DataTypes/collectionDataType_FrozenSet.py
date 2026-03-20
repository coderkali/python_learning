# Order Not maintained
# Duplicate not allowed
# The value within { }
# Hetregeneous Object
# Indexing and slicing Not Applicable
# Grawable in nature
# Imutable in nature -> This is difference from Set 
# Faster Access (Performance is less)

s = {10,20,30,40}
fs = frozenset(s)

print(type(fs))

#fs.add(50) #AttributeError: 'frozenset' object has no attribute 'add'



