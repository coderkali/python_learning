'''

remove(x)

if specifed element present at multiple times then the first elemeet will be rmeoved 


'''


l =[10,20,10,20,40]

l.remove(40)

print(l)

l.remove(10)

print(l)

#l.remove(50) #ValueError: list.remove(x): x not in list



# Remove all occurences

l = [1,1,1,1,2,2,2,2,3,3,3]
print("Before removal of l ::",l)
x = int(input("Enter any number ::"))

while True:
    if x in l:
        l.remove(x)
    else:
        break

print("After removal of l ::",l)
