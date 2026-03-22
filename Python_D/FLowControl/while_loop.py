'''
Execute group of condition based on condition 

'''

i =1

while i<=10:
    print("I value is {}".format(i))
    i =i+1

print("*"*20)

x =1
while x<=20:
    if x %3 ==0:
        print(x)
    x = x+1
print("*"*20)

# Display sum of first n numbners

n = int(input("Enter n numbers"))
sum =0
i =1
while i<=n:
    sum = sum+i
    i = i+1
print(sum)

print("*"*20)

name = ""
while name!="Kali":
    name = input("Enter a Different Name")

print("Thanks for confirming")