
'''
aliasing = create a new list pointing existing list 

l1 = [10,20,30,40]
l2 = l1

if changes into l1 then it reflect into l2 aswell

CLoning 

Creating exactly duplicate object There will be two differnt object
Cloning can be happend on two ways 
1) SLicing 
2) Copy()

'''

#Aliasing
l1 = [10,20,30,40]
l2 = l1

l1[1]= 777

print(l1)
print(l2)


# Cloning

list1 = [10,20,30,40]

#1  : Slic Operator 
list2 = list1[::]

# two differnet object 
print(id(list1))
print(id(list2))

list3 = [10,20,30,40]

list4 = list3.copy()

# two differnet object 
print(id(list3))
print(id(list4))





