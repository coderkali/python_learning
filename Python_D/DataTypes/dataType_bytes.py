# if we add more than 300 we will get ValueError: bytes must be in range(0, 256)
# Immutable
# Ordering
# Indexing 
l = [10,20,30,40]


b = bytes(l)

print(type(b))

for x in b:
    print(x)

#b[0] = 20 #TypeError: 'bytes' object does not support item assignment