l=[10,20,30]

l.reverse()

print(l) # [30, 20, 10]

#We don't have reverse function in tuple 

t = (10,20,30,40)

r = reversed(t)

t1 = tuple(r)

print(t1) # (40, 30, 20, 10)



# Sorting 

l = [20,5,10,15,0]
l.sort()
print(l)

#We don't have revsorterse function in tuple 

t = (120,5,10,15,0)
l = sorted(t)
print(type(l))
t1 = tuple(l)
print(t1)

t2 = (120,5,10,15,0)
l1 = sorted(t2,reverse=True)
print(type(l1))
t3 = tuple(l1)
print(t3)


# max and min 

t7 = (120,5,10,15,0)

print(min(t7))
print(max(t7))

# Tuple dones;t support  index() , insert() extend() , remove() , pop(), clear()
 