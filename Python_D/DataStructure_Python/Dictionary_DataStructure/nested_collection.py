l1 = [(10,20,30),(30,40,50)]

print(l1)
print(l1[0])
print(l1[0][1])
print(l1[1][1])


d = {'cars':("Honda","Kia","Hyundai"), "Mobile":("Samsung","Iphone","Nokia")}

print(d)
print(d["cars"][1])
print(d.get("cars")[2])

for x in d.get("Mobile"):
    print(x)

