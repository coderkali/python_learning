 # Create a list with elememts present i l1 but not in l2 

l1 = [10,20,30,40]
l2 = [30,40,50,60]

l3 = [x for x in l1 if x not in l2]


print(l3)

l4  =  [x for x in l1 if x in l2]
print(l4)


list1 = ["Kali", "Meeta", "Krithvik"]
# Need to get the first letter of each word 

list2 = [word[0] for word in list1]
print(list2)


s = "the quick brown fox jumps over the lazy dog"

# [[The ,3], [Quick,5] ....]

words = s.split()

list5 = [[word.upper(), len(word)]for word in words ]
print(list5)


