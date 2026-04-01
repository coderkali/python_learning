'''
reverse() -> List based method 
Existing list only the order will be rverse 


r = reversed(l) -> Which returns a new object iterator object 

'''

l = [10,20,30,40]

print("Before Reverse ", l)
l.reverse()
print("After Reverse ", l)

l1 = [10,30,50,70]

r = reversed(l1)

print(r) # <list_reverseiterator object at 0x109cb6aa0>

l2 = list(r)
print("After reverse and gets converted from r ",l2)

s = "kali"

r1 = reversed(s)

for x in r1:
    print(x)
