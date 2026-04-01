a = 10
b = 20
c= 30

t= a,b,c

print(t)
print(type(t))

t= (10,20,30,40)
w,x,y,z  = t

print(w)
print(x)
print(y)
print(z)

t1= (10,20,30,40)
#w,x,y,  = t1 # ValueError: too many values to unpack (expected 3, got 4)
# w,x,y,u,q  = t1 # ValueError: not enough values to unpack (expected 5, got 4)

a, *b = t
print(a)
print(b) # This is List 
