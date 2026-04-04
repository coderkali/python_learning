s1 = {10,20,30,40}
s2 = {30,40,50,60}

s3 = s1.union(s2)

print(s3) # {40, 10, 50, 20, 60, 30}

s4 = s1 | s2

print(s4)

s5 = s1.intersection(s2)
print(s5)

s6 = s1 & s2

print(s6)


# The elememnts is preseny in s1 but not in s2
s7 = s1.difference(s2)
print(s7)

s8 = s1-s2
print(s8) 


# the elememts is present in s1 but not in s2 and present in s2 but not in s1
s9 = s1.difference(s2)
print(s9)

s10 = s1^s2
print(s10)

