d = eval(input("Enter Dict ::"))

sum =0;

for item in d.items():
    sum = sum + item[1]

print("The sum of values ::", sum)


d1 = eval(input("Enter Dict ::"))

print("Sum of all values ", sum(d1.values()))
