'''
 2 to 10 -> Prime numbers 

 2 ,3, 5,7

'''

n = int(input("Enter n values"))

n1 = 2

while n1 <=n:
    is_prime = True
    for i in range (2, n1//2+1):
        if n1%i ==0:
            is_prime= False
            break
    if is_prime==True:
        print(n1)
    n1 = n1+1

