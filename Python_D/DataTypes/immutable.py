x = 10
print(id(x))

x = x+1
print(id(x))

y = 10
z = y

print(id(y))
print(id(z))

z = y +1

print(id(z))


a = 10
b= 10
c =10

print(id(a))
print(id(b))
print(id(c))

print(a is b is c) #True

e = 1000.234
f = 1000.234

print(e is f) #True

print(a is b is c is e) #False

s = "Kali"
s1 = "Kali"

print(s is s1)


#mutable 

l = [10,20,30]
print(l)
print(id(l))
l[0] =7777
print(l)
print(id(l))

l1 = [20,30,40,50]
l2 = l1
print(id(l1))
print(id(l2))

l1[0] = 200
print(id(l1))
print(id(l2))