l1 = ["Dog","Cat","Rat"]

l2 = ["Dog","Cat","Rat"]

l3 = ["DOG","CAT","RAT"]

l4 = ["cat", "Rat", "Dog"]

'''
 To use == operator 
 1) The no of elements must be same 
 2) The order of elements must be same 
 3) The conenet must be same 

'''

print(l1 == l2) # true
print(l1 == l3) # False
print(l1 == l4) # False

# Relation operator 
# < <= < <=

l1 = [10,20,30,40]
l2 = [50,60]


'''
1) Conenet comparisoon one by elemenet
 l1 < l2 => 10 < 50 -> If it is true then it goes second element

'''

print(l1 < l2)
print(l1 <= l2)
print(l1 > l2)
print(l1 >= l2)

# Membership operator 
'''
 in 
 not in 
'''
l = [10,20,30,40]
print(10 in l1) 
print(20 in l1)
print(90 not in l1)