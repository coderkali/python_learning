#fileter(function, sequnce)

l =[0,1,2,3,4,5,6,7,8,9,10]

# Without Filter function 

def isEven(n):
    if n%2==0:
        return True
    else:
        return False
l1=[]
for n in l:
    if isEven(n) == True:
        l1.append(n)

print(l1)

# With Filter Function

l2 = list(filter(isEven,l))
print(l2)

# Filter With lamdba function 

l =[0,1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda n : n%2==0,l))

print(even)

odd = list(filter(lambda n : n%2!=0,l))

print(odd)

# Divisible 3 and odd
nby3Odd = list(filter(lambda n : n%3==0 and n%2!=0,l))
print(nby3Odd)


names = ["Kali","Meeta","Prasad","Rishi","Krithvik"]

divBy5 = list(filter(lambda name : len(name)%5==0,names))
print(divBy5)






