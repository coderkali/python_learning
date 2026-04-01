'''
l.sort() -> Natural sorting order
number -> Ascending order
string -> Alphabetical order

sort() -> can use only same type of elemenmet only -> Not the hetrogenious elements 

l.sort(reverse=True)
reverse=True =>  Natiral Sorting order then reversed 


sorted() -> Python inbuilt function

l1 = sorted(l) -> It will create a new object 

'''

l =[20,5,30,40,1]

print("before Sorting ::",l)

l.sort()

print("After Sorting ::",l)

l1 = ["Banana", "Cat", "Apple"]

print("before Sorting ::",l1)

l1.sort()

print("After Sorting ::",l1)

print("*"*100)

#  TypeError: '<' not supported between instances of 'int' and 'str'

# l2 = ["Banana", 10, "Cat", 2, "Apple",1]

# print("before Sorting ::",l2)

# l2.sort() # TypeError: '<' not supported between instances of 'int' and 'str'

# print("After Sorting ::",l2)


l2 =[20,5,30,40,1]

print("before Sorting ::",l2)

l2.sort()#-> Natiral Sorting order  []
print("After Sorting With Natural Sorting Order ::",l2) # 1, 5, 20, 30, 40]
l2.sort(reverse=True) #-> natiral Sorting order with reveredd
print("After Sorting With Natural Sorting Order  With Reversed::",l2) # [40, 30, 20, 5, 1]

print("*"*100)

l1 = [20,10,30,40]

l2 = sorted(l1)

print("Original List ::",l1)
print("Original List ::",l2)



