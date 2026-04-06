l =[1,2,3,4,5]

def squareIt(n):
    return n*n

l1 = list(map(squareIt,l))

print(l1)

l2 = list(map(lambda n : n*n,l))

print(l2)


l3 = [1,2,3,4,5]

l4 = [5,10,15,20,25,30] # Extar element will be ignored 

l5 = list(map(lambda x,y: x*y, l3,l4))

print(l5)