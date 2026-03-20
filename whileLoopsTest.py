i =1

while i<6:
    print(i)
    i  = i+1
print("======================") 


while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number entered. Exiting the loop.")
        break
    else:
        print("You entered:", num)