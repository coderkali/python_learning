# len()

t = (10,20,30,40,40)

print(len(t))

# count() # It returns no of occurenece of specfied elemenmts 

print(t.count(10))
print(t.count(40))


# index -> returns index of first elemenets of specfied element 

t = (10,20,30,40,10)

print(t.index(10)) # 0
print(t.index(100)) # ValueError: tuple.index(x): x not in tuple