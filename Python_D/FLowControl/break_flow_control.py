for i in range(10):
    if(i==7):
        print("Breaking now")
        break
    print(i)
print("Outside the loop")

cart = [10,20,30,600,70,80]

for item in cart:
    if item > 500:
        print("Breaking now")
        break;
    print("Processing item:", item)
print()