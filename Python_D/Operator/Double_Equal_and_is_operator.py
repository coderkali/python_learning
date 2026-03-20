# is operator reference comparison 
# == operator refernce for content operator 

l1 = [10,20,30]

l2 = [10,20,30]

print(id(l1))
print(id(l2))

print(l1 is l2) #false
print(l1==l2) #true

l3 =l1

print(l3 is l1) #true Both l3 and l1 pointing to same object 