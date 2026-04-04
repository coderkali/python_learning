# List Merging
l = [ 10,20 ]
l1= [ 30,40 ]

l2= l+l1

print(l2)

l3 =[*l1, *l]

print(l3)

# tuple Merging 

t1 = (10,20)
t2 = (30,40)

t3 = t1+t2

print(t3)
t4 = (*t1,*t2)
print(t4)

# Set Merging 


s1 = {10,20}
s2 = {30,40}

#s3 = s1+s2 # TypeError: unsupported operand type(s) for +: 'set' and 'set'

s3 = (*s1,*s2)
print(s3)


# Dict Merging

d1 = {100:"A",200:"B"}
d2 = {300:"C",400:"D",100:"X"}

#d3 = d1 + d2 # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

d3 = {**d1, **d2}
print(d3)
