d = {100:"Kali","A":200,300:"Meeta"}

print(d[100])
#print(d[200]) # KeyError: 200


d[400] = "Shiva"
print(d)

d[100] = "Test"
print(d)

# Delete the dict

del d[400]
print(d)

#del d[500] # KeyError: 500

del d[100],d["A"]
print(d)

