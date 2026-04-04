n = int(input("Enter No of Students :: "))

d ={}

for i in range(n):
    name = input("Enter Student Name :: ")
    marks = int(input("Enter Student Marks ::"))
    d[name] = marks

print("Student Data Insertions Completed ")
print("* "*30)
print("Name","\t\t","Marks")
print("* "*30)

for k,v in d.items():
    print(k,"\t\t",v)


print("Search Operation Started.....")
while True:
    name = input("Enter Student name to get marks ::")
    marks = d.get(name,-1)
    if marks ==-1:
        print("Student Not Found")
    else:
        print("Marks Of",name," are ",marks)
    option= input("Do you want to fund Another Student Marks(Yes/No) ")
    if option.lower() == 'no':
        break

