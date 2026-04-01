import collections


'''
List - Takes More memory
Tuple -> Takes less memory 

List -> Unhasahbale
Tuple -> Hashbale -> So we can able to add set and dict 


'''

l =[10,20,30,40]
t =(10,20,30,40)

# print(isinstance(l,collections.Hashable))
# print(isinstance(t,collections.Hashable))

print(hash(t))
print(hash(l)) # TypeError: unhashable type: 'list'