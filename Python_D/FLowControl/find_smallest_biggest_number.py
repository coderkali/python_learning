a = int(input("Enter first number"))
b = int(input("Enter Second number"))

if a>b:
    print("Biggest Number is ",a)
else:
    print("Biggest number is ",b)


    # WAP to check the given number is in between 1 0r 100

n = int(input("Enter the number"))

if n >=1 and n<=100:
    print("Yes the number {} is between the 1 to 100 ".format(n))
else:
    print("No number {} is not between 1 to 100".format(n))