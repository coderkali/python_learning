# eval will converts based on inouts
x = input("Enter Something")
print(type(x)) # This is always String type 

y = eval(input("Enter Something"))
print(type(y)) # This will be dynamically assigned the type base don user input 


z = eval("10+20+30")
print(z)
print(type(z))