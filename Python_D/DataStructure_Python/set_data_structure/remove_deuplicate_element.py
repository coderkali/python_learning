l = [10,10,20,30,40,50,60]

s = set(l)

print(s) # {40, 10, 50, 20, 60, 30}

l1 = list(s)

print(l1)


l1= [10,10,20,30,40,50,60]
l2= []
for x in l1:
    if x not in l2:
        l2.append(x)


print(l2)


# Print how many vowels in word

word = input("Enter any word :: ")

s = set(word)

print(s)

v = {'a','e','i','o','u'}

result = s.intersection(v)
print(result)
