l =[10,20,[30,40]]

print(l[0])
print(l[1])
print(l[2]) # [30, 40]

print(l[2][0]) # 30  
print(l[2][0]) # 40 


# Netsted List as Matrix

print("* "*100)


l1 = [[10,20,30],[40,50,60],[70,80,90]]

print(l1)

print("Pirnt elements row wise")
for x in l1:
    print(x)

print("Pirnt elements matrix wise")

for x in l1:
    for y in x:
        print(y,end =" ")