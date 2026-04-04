n = int(input("Enter No of student"))

d = {}

for i in range(n):
    name = input("Enter Name of student")
    marks = int(input("Enter Marks Of student"))
    d[name] = marks

print("*"*30)
print("Name","\t\t", "Marks")
print("*"*30)
for name in d:
    print(name,"\t\t",d[name])