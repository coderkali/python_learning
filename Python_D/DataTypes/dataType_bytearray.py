# if we add more than 300 we will get ValueError: bytes must be in range(0, 256)
# Mutable
# Ordering
# Indexing 
l =[10,20,30,40]

b = bytearray(l)

print(b[0])
print(b[-1])
print(b[2])

print("#"*100)

b[2] = 200

for x in b:
    print(x)