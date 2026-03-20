def sum(a, b):
    #and b are local variables
    global z #z is a global variable
    z = 12 # Update the global z value
    return a + b

z = 10
result = sum(3, 5)
print(result)  # Output: 8
print(z)  # Output: 10