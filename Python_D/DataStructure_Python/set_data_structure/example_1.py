'''
Duplicates are not alllowed
Order is not applicable 
indexing and slicing cocepts are not applicable 
{} -> Curly braces to represent the elements 
Hetreogenious Objects 
Mutable
Mathematical Operations possible 
'''


s = {} #-> Empty is not possible 
print(type(s)) # -> <class 'dict'> Its a dict type not set type 

s = set() # This is empty object 

s.add(10)
s.add('z')
s.add(200)

print(s)

#print(s[1]) # TypeError: 'set' object is not subscriptable

#print(s[1:2]) # TypeError: 'set' object is not subscriptable

'''
List 
   Duplicates
   Insertion Order
   [10,20,30]
   indexing and slicing 

set
   Duplicates not allowed 
   Insertion order is nlot oreserved
   {}
   Indexing and slicing ois not possible 

'''
