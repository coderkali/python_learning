'''

len -> Python inbuilt function 
append -> inside the list -> It will add the elemenets in last poition 
insert -> inside the list -> l.index(index,elemenet)
sorted -> Python inbuilt function 
count -> inside the list function 
index -> inside the list function  -> This looks for Where the value exist for the first occurenece 
extend -> To add all elements of given sequence to the list 



'''


l = [10,20,30,10]

print(len(l))
print(l.count(10))
print(l.count(50))


#print(l.index(1)) # ValueError: list.index(x): x not in list
print(l.index(10))


list1 = []

list1.append(10)
list1.append(20)
list1.append(30)

print(list1)

list1.insert(1,7777)
print(list1)

list1.insert(100,8888) # As specificed index is greater then length oif index 
print(list1) # [10, 7777, 20, 30, 8888]
list1.insert(-100,9999) 
print(list1) # [9999, 10, 7777, 20, 30, 8888]

l1 = [10,20,30]
l2 = ["Kali","Prasad", "Padhi"]


print(len(l1))
l1.extend(l2)

print(l1)
print(len(l1))

l3 = [10,20,30]
l4 = [40,50]

l3.append(l4) 
print(l3) # [10, 20, 30, [40, 50]]
print(len(l3)) 

l5 = [10,20,30]
l6 = ["ABC"]

l5.extend(l6)
print(l5)
print(len(l5))

l5.extend("XYZ")
print(l5)
print(len(l5))


