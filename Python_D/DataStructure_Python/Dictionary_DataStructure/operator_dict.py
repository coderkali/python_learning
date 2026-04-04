d1 = {100:"A",200:"B"}
d2 = {300:"C",400:"D"}

#d3 = d1 + d2 # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
#d4 = d1 *2  # TypeError: unsupported operand type(s) for *: 'dict' and 'int'

print(d1 == d2) # False

d3 = {200:"B",100:"A"}
print(d1 == d3) # True

#print(d1 < d2) # TypeError: '<' not supported between instances of 'dict' and 'dict'
#print(d1 > d2) # TypeError: '>' not supported between instances of 'dict' and 'dict'

# Membership operator (Only applicable to Key)

print(100 in d3) # True

print("B" in d3)
