'''
Both aregument should be list oibject 

 cocanetation operator (+)
 repetition operator (*) 

'''


l1 = [10,20,30]
l2 = [40,50,60]

l = l1+l2

print(l)

#l = l + 40  #TypeError: can only concatenate list (not "int") to list
l2= l + [90]
print(l2)

#l4= l1 + (40,50,60) #TypeError: can only concatenate list (not "tuple") to list

# Must be one argument should be list and other argument should be int
list1 = [10,20,30]
lsit2 = list1 *2 
print(lsit2) #[10, 20, 30, 10, 20, 30]