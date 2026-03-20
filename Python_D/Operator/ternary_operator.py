'''
 ~a -> This is unary operator 

 a + b -> Binary Operator 

 Ternary Operator -> 3 componenets 


'''


a = 10
b = 20

c = 30 if a >b else 40

print(c)

a = int(input("Enter First Number ::"))
b = int(input("Enter Second Number ::"))

min = a if a>b else b
print(min)