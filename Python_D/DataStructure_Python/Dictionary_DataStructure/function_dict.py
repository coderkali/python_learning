d1 = {100:"A",200:"B"}

print(len(d1))

print(d1.get(100))
print(d1.get(700)) # None

# d.get(key, default_value)
print(d1.get(700,"C"))

d2 = {300:"C",400:"D",100:"X"}

d1.update(d2)

print(d1)

#Print Keys and values

k = d1.keys()
print(k) # dict_keys([100, 200, 300, 400])

v = d1.values()
print(v) # dict_values(['X', 'B', 'C', 'D'])

# Get each item from Dict

i = d1.items()

print(i) # dict_items([(100, 'X'), (200, 'B'), (300, 'C'), (400, 'D')])

for k,v in d1.items():
    print("key ::",k)
    print("Value ::",v)



