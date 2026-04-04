def add(a,b):
    sum = a+b
    return sum

sum= add(10,20)
print(sum)

def f1():
    print("Hell0")

x = f1()
print(x) # Default return value of function is None



#Factorial of given number

def factorial(num):
    result =1 
    while num >=1:
        result = result*num
        num = num -1
    return result

print("Factorial Of 2 :: ",factorial(2))
print("Factorial Of 3 :: ",factorial(3))
print("Factorial Of 4 :: ",factorial(4))
 