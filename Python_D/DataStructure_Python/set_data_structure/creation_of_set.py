s = set() # Empty object

s1 = {10,20,30,40}

l = [10,20,30,40]

s2 = set(l)

print(s2) # {40, 10, 20, 30}

s3 = set(range(0,100,10))

print(s3) # {0, 70, 40, 10, 80, 50, 20, 90, 60, 30}

s4 = set("Apple")

print(s4) # {'A', 'e', 'l', 'p'}

s5 = eval(input("Enter set of value:: ")) # Enter set of value:: {10,20,30,1,3,4}

print(s5)