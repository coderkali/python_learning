from sys import argv
print(type(argv))


x = argv[1:]

print("The Sum is :: ", x)  # String Type we will get it from Argument 

z =0

for y in x:
    z = z + int(y)
    print("The Sum is ",z)



