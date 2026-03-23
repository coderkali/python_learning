for i in range(3):
    for j in range(3):
        if(i==j):
            break
        print(i,j)
print("Completed ------")


for i in range(3):
    for j in range(3):
        if(i==j):
            continue
        print(i,j)
print("Completed ------")
'''
 0 1 
 0 2
 1 0
 1 2
 2 0
 2 1
'''      