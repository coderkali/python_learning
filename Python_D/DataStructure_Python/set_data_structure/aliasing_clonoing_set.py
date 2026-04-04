s1 = {10,20,30}

s2 = s1

print(id(s1))
print(id(s2))

# cloning 

s3 = s1.copy()

#Comphresnsion

s4 = { x*2 for x in s1 }

print(s4)

