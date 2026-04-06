count =0
def factorial(n):
    global count
    count = count +1
    #print("Executing Factorial Function With n Value ",n)
    if n == 0:
        result =1
    else:
        result = n * factorial(n-1)
    #print("Resturning result of factorial({}) is:{} ".format(n,result))   
    return result

print(factorial(1000)) # RecursionError: maximum recursion depth exceeded
print("Count ::",count) # 
# print(factorial(4))

# for i in range(11):
#     print("The factorial of {} is {} ".format(i,factorial(i)))