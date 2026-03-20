x = input("Can you enter 3 Float value")

print(x)

x = x.split(",")
print(x)

a,b,c = [float(x) for x in input("Can you enter 3 Float value").split(",")]
