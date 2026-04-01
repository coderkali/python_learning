'''
order is applicable 
duplicate allowed
hetrogenous objects 
indexing and slicing 
immuatbale -> This is the difference from List 
() -> Parenthesis is optional 
'''


t = (10,"kali",20,30)
t1 = 10,"kali",20,30,10

print(type(t))
print(type(t1))

print(t[0]) #Order is preserved
print(t[-1]) #Order is preserved


l = [10,20,30,40]

l[0] = 7777

print(l)

t2 = (10,20,30,40)


# Immutable 

#t[0] = 7777 # TypeError: 'tuple' object does not support item assignment  



