d1 = {100:"A",200:"B"}

print(d1)
print(d1.setdefault(300,"C"))
print(d1)
print(d1.setdefault(100,"X")) # It won't replace 
print(d1)


# Alaising and cloning 

d2 = {100:"A",200:"B"}
d3 = d2 
print(d2)
print(d3)

# Clonong 

d4 = d2.copy()

print(id(d2))
print(id(d4))