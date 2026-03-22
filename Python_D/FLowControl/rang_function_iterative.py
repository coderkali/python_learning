'''
range(n) -> n number of times iteratte 
range(n,m) -> n , m-1 number of times iteratte 
range(n,m, increment and decremnet number)
'''


for x in range(10):
    print("x is ",x)

print("*"*10)

for x in range(1,11):
    print("x is ",x)
print("*"*10)

for x in range(21):
    if x%2 != 0:
        print(x)

print("*"*10)

for x in range(1,21,2):
    print(x)


list=  eval(input("Enter list of number"))

sum =0
for x in list:
    sum = sum+x
    print(sum)

list1=  eval(input("Enter list of number"))
print("Sum is :",sum(list1))
