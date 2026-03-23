'''
if the number which has two factor either 1 or the same number
2,3,5,7,,11,13,17,19,23...
'''

n = int(input("Enter the number"))

if n <= 1:
    print("It is not a prime number")
else:
    is_prime=True
    for i in range(2,n):
        if n%i ==0:
            is_prime=False
            break
    if is_prime == True:
        print("It is a prime number")
    else:
         print("It is not a prime number")


if n <= 1:
    print("It is not a prime number")
else:
    is_prime=True
    for i in range(2,n//2+1):
        if n%i ==0:
            is_prime=False
            break
    if is_prime == True:
        print("It is a prime number")
    else:
         print("It is not a prime number")


