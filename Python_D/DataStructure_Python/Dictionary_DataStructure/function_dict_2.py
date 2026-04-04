d1 = {100:"A",200:"B"}

key = int(input("Enter any Key :: "))


if key in d1:
    print("key is available ",key)
else:
    print("key is not available ",key)


value = input("Enter any Value :: ")

is_available =False

for k,v in d1.items():
    if v == value:
        print("Value is available ",value)
        is_available = True

if is_available == True:
    print("Value is available ",value)


