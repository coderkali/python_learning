age = 32

if(age > 18):
    print("You are an adult")
    print("You can vote")
else:
    print("You are a minor")

print("This will be printed regardless of the age")


age = int(input("Enter your age: "))
if(age > 18):
    print("You are an adult")
    print("You can vote")
elif(age == 18):
    print("You are 18 years old")
else:
    print("You are a minor")    