list =[0,1,2,3,4,5,6,7,8,9]

# Using while loop 

i =0
while i<len(list):
    print(list[i])
    i = i+1


print("*"*100)

# using For Loop

for i in list:
    print(i)


i = 0
while i < len(list):
    print("The Element present at +ve index : {} and at -ve index: {} is :{}".format(i,i-len(list),list[i]))
    i= i+1