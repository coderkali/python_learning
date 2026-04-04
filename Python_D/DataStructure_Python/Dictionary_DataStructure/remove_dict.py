# d.key(key)
d1 = {100:"A",200:"B"}

print(d1.pop(100)) # A
print(d1)

# print(d1.pop(700)) # KeyError: 700
#-----------------------------------------
# d.pop(key,value) -> if the specificed key is not available then provided value will be returned 

d2 = {100:"A",200:"B"}

print(d2.pop(300,"C"))

#popItem
print(d2.popitem())
print(d2.popitem())
print(d2)
#print(d2.popitem()) # KeyError: 'popitem(): dictionary is empty'

# Making Dict empty

d3 = {100:"A",200:"B"}
d3.clear()
print(d3)
